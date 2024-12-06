#!/usr/bin/python
# -*- coding: UTF-8 -*-
#from Mesa import Mesa
from dominio_da_solucao.Dado import Dado


class Copo(object):
	def jogar_dados(self):
		dados = [Dado() for _ in range(5)]
		for i in range(len(dados)):
			if dados[i].dado_get_selecionado():
				dados[i].dado_set_numero()
		return dados

	def rejogar_dados(self, dados):
		for i in range(len(dados)):
			if dados[i].dado_get_selecionado():
				dados[i].dado_set_numero()
		return dados	

	def incrementa_jogada(self):
		self.jogadas += self.jogadas

	def get_jogadas(self) -> int:
		return self.jogadas

	def __init__(self):
		self.total_dices : int = None
		self.result : list = None
		self.jogadas : int = None



