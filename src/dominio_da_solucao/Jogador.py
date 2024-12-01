#!/usr/bin/python
# -*- coding: UTF-8 -*-
from dominio_da_solucao.Tabela import Tabela
from typing import List

class Jogador(object):
	def atribuir_pontuacao(self, pontos : int) -> int:
		pass

	def eh_seu_turno(self) -> bool:
		if self.turno == 1:
			return True
		else:
			return False

	def inverter_turno(self):
		if self.turno == 1:
			self.turno == 0
		else:
			self.turno == 1

	def informar_vez(self) -> int:
		return self.turno

	def informa_vencedor(self) -> int:
		return self.vencedor

	def informa_jogador(self) -> str:
		self.nome_jogador 

	def reiniciar(self):
		# ???
		pass

	def initialize(self, aSymbol : int, aIdentifier : str, aName : str):
		self.name = aName
		self.symbol = aSymbol
		self.indentifier = aIdentifier

	def get_name(self):
		return self.name

	def toogle_turn(self):
		if self.turno == False:
			self.turno = True
		elif self.turno == True:
			self.turno == False

	def pontuacao_atribuida(self):
		# ???
		pass

	def get_rounds_finalizados(self) -> int:
		return self.rounds_finalizados

	def get_vencedor(self) -> int:
		return self.rounds_finalizados

	def verifica_pontuacao_diferente(self) -> int:
		# [TODO] - Pensar como pegar a pontuacao do oponente
		pass

	def __init__(self):
		self.attempts : int = None
		self.total_points : int = None
		self.nome_jogador : str = None
		self.rounds_finalizados : int = None
		self.vencedor : int = None
		self.turno = False
		self.pontuacao_round_atribuida : int = None
		self.jogada_finalizada : int = None
