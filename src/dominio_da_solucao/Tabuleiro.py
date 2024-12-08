#!/usr/bin/python
# -*- coding: UTF-8 -*-
from dominio_da_solucao.Jogador import Jogador
from dominio_da_solucao.Mesa import Mesa
from dominio_da_solucao.Categoria import Categoria
from dominio_da_solucao.Dado import Dado
from dominio_da_solucao.interface_image import InterfaceMessage

class Tabuleiro(object):
	def __init__(self):
		self.finished = False
		self.local_player = Jogador()
		self.remote_player  = Jogador()
		self.local_player.initialize(1, "jogador1", "jogador_1")
		self.remote_player.initialize(2, "jogador2", "jogador_2")
		self.regular_move = True
		self.mesa = Mesa()
		self.categoria = Categoria()
		self.match_status = 1
		self.player_turn : int = None
		self.vencedor = ""
		self.rounds = 22

	def receive_withdrawal_notification(self):
		self.match_status = 6

	def get_status(self):
		interface = InterfaceMessage()
		turn_player = self.get_turn_player()
		if not self.regular_move:
			interface.set_message(turn_player.get_name() + ", jogada irregular!")
		else:
			if self.match_status == 1:
				interface.set_message("Yatch Dice")
			elif self.match_status == 2:
				interface.set_message("Vencedor = " + self.get_vencedor())
			elif self.match_status == 3:
				interface.set_message(turn_player.get_name() + ", jogue os dados!")
			elif self.match_status == 4:
				interface.set_message(turn_player.get_name() + ", selecione os dados, case deseje!, ou selecione categoria")
			elif self.match_status == 5:
				interface.set_message("Aguarando lance do adversário: " + self.remote_player.get_name())
			elif self.match_status == 6:
				interface.set_message("Adversário abandonou a partida")
		return interface

	def get_match_status(self):
		return self.match_status

	def start_match(self, players, local_id):
		playerA_name = players[0][0]
		playerA_id = players[0][1]
		playerA_order = players[0][2]
		playerB_name = players[1][0]
		playerB_id = players[1][1]
		self.local_player.reset()
		self.remote_player.reset()
		self.local_player.initialize(1, playerA_id, playerA_name)
		self.remote_player.initialize(2, playerB_id, playerB_name)
		if playerA_order == "1":
			self.local_player.toogle_turn()
			self.match_status = 3  #    waiting piece or origin selection (first action)
		else:
			self.remote_player.toogle_turn()
			self.match_status = 5  #    waiting remote action

	def get_player_symbol(self):
		player = self.get_turn_player()
		symbol = player.get_symbol()
		return symbol

	def get_turn_player(self) -> Jogador:
		if self.local_player.get_turno():
			return self.local_player
		elif self.remote_player.get_turno():
			return self.remote_player

	def jogar_dados(self):
		jogador = self.get_turn_player()
		if jogador.get_max_attempts() == jogador.get_current_attempts():
			self.regular_move = False
		elif self.match_status == 3:
			dados = self.mesa.jogar_dados()
			self.match_status = 4
			for i in range(len(dados)):
				dados[i].remover_destaque()
			move_to_send = {"dados": [dado.to_dict() for dado in dados]}
			move_to_send["match_status"] = ""
			move_to_send["type"] = "dados_jogados"
			jogador.incrementa_current_attempts()
			return move_to_send
		elif self.match_status == 4:
			dados = self.mesa.get_dados()
			dados = self.mesa.rejogar_dados(dados)
			for i in range(len(dados)):
				dados[i].remover_destaque()
			move_to_send = {"dados": [dado.to_dict() for dado in dados]}
			move_to_send["match_status"] = ""
			move_to_send["type"] = "dados_jogados"
			jogador.incrementa_current_attempts()
			return move_to_send
		return 1

	def dado_selecionado(self, index, str):
		if self.match_status == 4:
			dados = self.mesa.get_dados()
			move_to_send = {}
			if  str == "add":
				dados[index].adicionar_destaque()
			elif str == "remove":
				dados[index].remover_destaque()
			move_to_send["type"] = "dado_selecionado"
			move_to_send["index"] = index
			move_to_send["destaque"] = dados[index].get_destaque()
			move_to_send["match_status"] = ""
			return move_to_send

	def escolher_categoria(self, str1):
		dados = self.mesa.get_dados()
		dados_valores = []
		for i in range(len(dados)):
			dados_valores.append(dados[i].dado_get_numero())
		move_to_send = {}
		move_to_send["vencedor"] = ""
		pontos = 0
		jogador = self.get_turn_player()
		if self.match_status == 4 or self.match_status == 3:
			if "Ones" in str1:
				pontos = self.categoria.atribuir_pontuacao(1, dados)
				move_to_send["category"] = str1
				move_to_send["pontuacao"] = pontos
				move_to_send["match_status"] = ""
				move_to_send["type"] = "categoria"

			elif "Twos" in str1:
				pontos = self.categoria.atribuir_pontuacao(2, dados)
				move_to_send["category"] = str1
				move_to_send["pontuacao"] = pontos
				move_to_send["match_status"] = ""
				move_to_send["type"] = "categoria"

			elif "Threes" in str1:
				pontos = self.categoria.atribuir_pontuacao(3, dados)
				move_to_send["category"] = str1
				move_to_send["pontuacao"] = pontos
				move_to_send["match_status"] = ""
				move_to_send["type"] = "categoria"

			elif "Fours" in str1:
				pontos = self.categoria.atribuir_pontuacao(4, dados)
				move_to_send["category"] = str1
				move_to_send["pontuacao"] = pontos
				move_to_send["match_status"] = ""
				move_to_send["type"] = "categoria"

			elif "Fives" in str1:
				pontos = self.categoria.atribuir_pontuacao(5, dados)
				move_to_send["category"] = str1
				move_to_send["pontuacao"] = pontos
				move_to_send["match_status"] = ""
				move_to_send["type"] = "categoria"

			elif "Sixes" in str1:
				pontos = self.categoria.atribuir_pontuacao(6, dados)
				move_to_send["category"] = str1
				move_to_send["pontuacao"] = pontos
				move_to_send["match_status"] = ""
				move_to_send["type"] = "categoria"

			elif "Full_House" in str1:
				pontos = self.categoria.atribuir_pontuacao(8, dados_valores)
				move_to_send["category"] = str1
				move_to_send["pontuacao"] = pontos
				move_to_send["match_status"] = ""
				move_to_send["type"] = "categoria"

			elif "S_Straight" in str1:
				pontos = self.categoria.atribuir_pontuacao(9, dados_valores)
				move_to_send["category"] = str1
				move_to_send["pontuacao"] = pontos
				move_to_send["match_status"] = ""
				move_to_send["type"] = "categoria"

			elif "B_Straight" in str1:
				pontos = self.categoria.atribuir_pontuacao(10, dados_valores)
				move_to_send["category"] = str1
				move_to_send["pontuacao"] = pontos
				move_to_send["match_status"] = ""
				move_to_send["type"] = "categoria"

			elif "Yatch" in str1:
				pontos = self.categoria.atribuir_pontuacao(11, dados_valores)
				move_to_send["category"] = str1
				move_to_send["pontuacao"] = pontos
				move_to_send["match_status"] = ""
				move_to_send["type"] = "categoria"

			elif "Four_Of" in str1:
				pontos = self.categoria.atribuir_pontuacao(7, dados_valores)
				move_to_send["category"] = str1
				move_to_send["pontuacao"] = pontos
				move_to_send["match_status"] = ""
				move_to_send["type"] = "categoria"
			

			self.regular_move = True
			jogador.zera_attempts()
			jogador.atribuir_pontuacao(pontos)
			
			self.decrementa_rounds()
			
			self.local_player.toogle_turn()
			self.remote_player.toogle_turn()

			if self.local_player.get_turno():
				self.match_status = 5
			else:
				self.match_status = 3
			
			# Sincronização dos decrementos
			if self.rounds == 0:
				self.finished = True
				self.match_status = 2
				if self.local_player.get_pontuacao_total() > self.remote_player.get_pontuacao_total():
					self.set_vencedor(self.local_player.get_name())
				elif self.local_player.get_pontuacao_total() < self.remote_player.get_pontuacao_total():
					self.set_vencedor(self.remote_player.get_name())
				else:
					self.set_vencedor("empate")
				move_to_send["vencedor"] = self.get_vencedor()
		return move_to_send
	
	def recieve_category(self, a_move):
		if a_move["type"] == "categoria":
			# Sincronização dos decrementos
			pontos = a_move["pontuacao"]
			self.decrementa_rounds()
			self.remote_player.atribuir_pontuacao(pontos)
			self.local_player.toogle_turn()
			self.remote_player.toogle_turn()
			jogador = self.get_turn_player()
			if jogador.get_turno():
				self.match_status = 3
			else:
				self.match_status = 5
			if self.rounds == 0:
				self.finished = True
				self.match_status = 2
				vencedor = a_move["vencedor"]
				self.set_vencedor(vencedor)
	
	def decrementa_rounds(self):
		self.rounds = self.rounds - 1
				

	def get_finished(self):
		return self.finished

	def verifica_vencedor(self):
		local_points = self.local_player .get_pontuacao_total()
		remote_points = self.remote_player.get_pontuacao_total()
		if local_points > remote_points:
			self.vencedor = self.local_player.get_name()
		elif local_points < remote_points:
			self.vencedor = self.remote_player.get_name()
		else:
			self.vencedor = "Empatou!"

	def get_vencedor(self):
		return self.vencedor

	def set_vencedor(self, name):
		self.vencedor = name

