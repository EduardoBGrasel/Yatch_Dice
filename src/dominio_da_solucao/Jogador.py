#!/usr/bin/python
# -*- coding: UTF-8 -*-
from dominio_da_solucao.Tabela import Tabela
from typing import List

class Jogador(object):
	def __init__(self):
		self.max_attempts = 4
		self.current_attempts = 0
		self.total_points = 0
		self.name = ""
		self.symbol = None
		self.indentifier = 0
		self.rounds_finalizados = False
		self.vencedor = False
		self.turno = False
		self.pontuacao_round_atribuida = 0
		self.jogada_finalizada = False
	
	def incrementa_current_attempts(self):
		self.current_attempts = self.current_attempts + 1

	def get_current_attempts(self):
		return self.current_attempts

	def zera_attempts(self):
		self.current_attempts = 0;
	
	def get_max_attempts(self):
		return self.max_attempts

	def atribuir_pontuacao(self, pontos : int) -> int:
		self.total_points += pontos

	def eh_seu_turno(self) -> bool:
		if self.turno == 1:
			return True
		else:
			return False
	
	def reset(self):
		self.attempts = 0
		self.total_points = 0
		self.name = ""
		self.symbol = None
		self.indentifier = 0
		self.rounds_finalizados = False
		self.vencedor = False
		self.turno = False
		self.pontuacao_round_atribuida = 0
		self.jogada_finalizada = False
	
	def get_symbol(self):
		return self.symbol

	def informar_vez(self) -> int:
		return self.turno

	def informa_vencedor(self) -> int:
		return self.vencedor

	def informa_jogador(self) -> str:
		self.name

	def get_pontuacao_total(self):
		return self.total_points

	def initialize(self, aSymbol : int, aIdentifier : str, aName : str):
		self.reset()
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


