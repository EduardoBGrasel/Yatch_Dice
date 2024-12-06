#!/usr/bin/python
# -*- coding: UTF-8 -*-
from dominio_da_solucao.Copo import Copo

class Mesa(object):

	def jogar_dados(self):
		self.dados_jogados = self.copo.jogar_dados()
		return self.dados_jogados

	def dado_selecionado(self, index, dados):
		self.copo.dado_selecionado(index, dados)

	def get_dados(self):
		return self.dados_jogados

	def get_dados_selecionados(self):
		return self.dados_selecionados

	def __init__(self):
		self.dados_selecionados : list = None
		self.dados_jogados : int = None
		self.copo = Copo()

