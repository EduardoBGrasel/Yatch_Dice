#!/usr/bin/python
# -*- coding: UTF-8 -*-
from dominio_da_solucao import Mesa
from typing import List

class Copo(object):
	def tem_dado(self, aQuantidade_dados : int):
		pass

	def tem_jogadas(self, aQuantidade_jogadas : int) :
		pass

	def retira_dados_lista(self):
		pass

	def dados_jogados(self) -> int:
		pass

	def adicionado_dado_lista(self, aIndex_dado : int):
		pass

	def incrementa_jogada(self):
		self.___jogadas += self.___jogadas

	def get_jogadas(self) -> int:
		return self.___jogadas

	def remove_dado_lista(self, aIndex_dado : int):
		pass

	def __init__(self):
		self.___total_dices : int = None
		self.___result : list = None
		self.___jogadas : int = None
		self._unnamed_Mesa_ : Mesa = None
		self._unnamed_Dado_ = []
		"""# @AssociationMultiplicity 1..5
		# @AssociationKind Aggregation"""

