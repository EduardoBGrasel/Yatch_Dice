#!/usr/bin/python
# -*- coding: UTF-8 -*-
#from Mesa import Mesa
from dominio_da_solucao.Dado import Dado
from typing import List

class Copo(object):
	def tem_dado(self, aQuantidade_dados : int):
		pass

	def tem_jogadas(self, aQuantidade_jogadas : int) :
		pass

	def retira_dados_lista(self):
		pass

	def jogar_dados(self):
		dados = [Dado() for _ in range(5)]
		for i in range(len(dados)):
			if dados[i].dado_get_selecionado() == True:
				dados[i].dado_set_numero()
		return dados

	def adicionado_dado_lista(self, aIndex_dado : int):
		pass

	def incrementa_jogada(self):
		self.jogadas += self.jogadas

	def get_jogadas(self) -> int:
		return self.jogadas

	def remove_dado_lista(self, aIndex_dado : int):
		pass


	def __init__(self):
		self.total_dices : int = None
		self.result : list = None
		self.jogadas : int = None

if __name__ == "__main__":
	copo = Copo()
	copo.jogar_dados()

