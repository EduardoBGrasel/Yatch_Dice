#!/usr/bin/python
# -*- coding: UTF-8 -*-
from dominio_da_solucao.Jogador import Jogador
from dominio_da_solucao.Mesa import Mesa
from dominio_da_solucao.Tabela import Tabela
from dominio_da_solucao.Dado import Dado
from dominio_da_solucao.interface_image import InterfaceImage
from typing import List

class Tabuleiro(object):
	def __init__(self):
		self.rounds = 22
		self.local_player = Jogador()
		self.remote_player  = Jogador()
		self.local_player.initialize(1, "jogador1", "jogador_1")
		self.remote_player.initialize(2, "jogador2", "jogador_2")
		self.regular_move = True
		self.mesa = Mesa()
		self.tabela = Tabela()
		self.match_status = 1
		self.player_turn : int = None
		self.vencedor = ""


	def recieve_move(self, a_move):
		if a_move["type"] == "dados_jogados":
			pass
			

	def receive_withdrawal_notification(self):
		self.match_status = 6

	def get_status(self):
		interface = InterfaceImage()
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

	def atribuir_pontuacao_jogador(self, aPontos : int):
		pass

	def receber_selecao_de_dado(self, aDado : Dado):
		pass

	def get_turn_player(self) -> Jogador:
		if self.local_player.eh_seu_turno():
			return self.local_player
		elif self.remote_player.eh_seu_turno():
			return self.remote_player
	
	def get_regular_move(self):
		return self.regular_move


	def jogar_dados(self):
		jogador = self.get_turn_player()
		# if jogador.get_max_attempts() == jogador.get_current_attempts():
		# 	self.regular_move = False
		if self.match_status == 3:
			dados = self.mesa.jogar_dados()
			self.match_status = 4
			for i in range(len(dados)):
				dados[i].remover_destaque()
			move_to_send = {"dados": [dado.to_dict() for dado in dados]}
			move_to_send["match_status"] = "next"
			move_to_send["type"] = "dados_jogados"
			jogador.incrementa_current_attempts()
			return move_to_send
		elif self.match_status == 4:
			dados = self.mesa.get_dados()
			dados = self.mesa.copo.rejogar_dados(dados)
			for i in range(len(dados)):
				dados[i].remover_destaque()
			move_to_send = {"dados": [dado.to_dict() for dado in dados]}
			move_to_send["match_status"] = "next"
			move_to_send["type"] = "dados_jogados"
			jogador.incrementa_current_attempts()
			return move_to_send
		
			


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
			move_to_send["match_status"] = "next"
			return move_to_send

	def escolher_categoria(self, aCategoria_escolhida : int):
		pass

	def verifica_final(self, aRounds : int) -> int:
		pass

	def verifica_vencedor(self, aPontuacao, aPontuacao_remota) -> int:
		pass

	def get_vencedor(self):
		return self.vencedor

	def atualizar_estado(self):
		pass

	def indentificar_area_acao(self) -> str:
		pass

