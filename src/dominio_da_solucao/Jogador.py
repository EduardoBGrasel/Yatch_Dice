#!/usr/bin/python
# -*- coding: UTF-8 -*-
from dominio_da_solucao import Tabuleiro
from dominio_da_solucao import Tabela
from typing import List

class Jogador(object):
	def atribuir_pontuacao(self, pontos : int) -> int:
		pass

	def eh_seu_turno(self) -> bool:
		if self.___turno == 1:
			return True
		else:
			return False

	def inverter_turno(self):
		if self.___turno == 1:
			self.___turno == 0
		else:
			self.___turno == 1

	def informar_vez(self) -> int:
		return self.___turno

	def informa_vencedor(self) -> int:
		return self.___vencedor

	def informa_jogador(self) -> str:
		self.___nome_jogador 

	def reiniciar(self):
		# ???
		pass

	def initialize(self, aSymbol : int, aIdentifier : str, aName : str):
		# [TODO] - @Dudu
		pass

	def toogle_turn(self):
		# [TODO] - @Dudu
		pass

	def iniciar_partida(self):
		# [TODO] - @Dudu
		pass

	def atualiza_gui(self, aEstado_jogo):
		# [TODO] - @Dudu
		pass

	def pontuacao_atribuida(self):
		# ???
		pass

	def get_rounds_finalizados(self) -> int:
		return self.___rounds_finalizados

	def get_vencedor(self) -> int:
		return self.___rounds_finalizados

	def verifica_pontuacao_diferente(self) -> int:
		# [TODO] - Pensar como pegar a pontuacao do oponente
		pass

	def __init__(self):
		self.___attempts : int = None
		self.___total_points : int = None
		self.___nome_jogador : str = None
		self.___rounds_finalizados : int = None
		self.___vencedor : int = None
		self.___turno : int = None
		self.___pontuacao_round_atribuida : int = None
		self.___jogada_finalizada : int = None
		self._unnamed_Tabuleiro_ : Tabuleiro = None
		self._unnamed_Tabela_ : Tabela = None

