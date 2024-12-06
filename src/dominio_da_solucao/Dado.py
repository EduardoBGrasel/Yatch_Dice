#!/usr/bin/python
# -*- coding: UTF-8 -*-
#from dominio_da_solucao import Mesa
from random import randint
from typing import List

class Dado(object):
	def definir_dado(self, aIndex_selecionado : int):
		pass

	def remover_destaque(self):
		self.selecionado = False

	def adicionar_destaque(self):
		self.selecionado = True
	
	def get_destaque(self):
		return self.selecionado

	def dado_set_numero(self):
		self.number = randint(1, 6)
	
	def dado_get_selecionado(self):
		return self.selecionado

	def dado_get_numero(self):
		return self.number

	def to_dict(self):
		"""
		Copia as informações do objeto para um dicionário.
		"""
		return {
			"number": self.number,
			"index_dado": self.index_dado,
			"selecionado": self.selecionado,
		}

	def __init__(self):
		self.number : int = None
		self.index_dado : int = None
		self.selecionado = True


