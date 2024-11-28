#!/usr/bin/python
# -*- coding: UTF-8 -*-
from dominio_da_solucao import Copo
from dominio_da_solucao import Mesa
from typing import List

class Dado(object):
	def definir_dado(self, aIndex_selecionado : int):
		pass

	def remover_destaque(self, aIndex : int):
		pass

	def adicionar_destaque(self, aIndex : int):
		pass

	def __init__(self):
		self.___number : int = None
		self.___index_dado : int = None
		self.___selecionado : int = None
		self._unnamed_Copo_ : Copo = None
		"""# @AssociationMultiplicity 1"""
		self._unnamed_Mesa_ : Mesa = None

