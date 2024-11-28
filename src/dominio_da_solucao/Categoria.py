#!/usr/bin/python
# -*- coding: UTF-8 -*-
from dominio_da_solucao import Tabela
from dominio_da_solucao import Mesa
from dominio_da_solucao import Prisao
from typing import List

class Categoria(object):
	def atribuir_pontuacao(self, aCategoria_escolhida : int):
		pass

	def valida_for_of_a_kind(self, dados : list) -> int:
		return any(dados.count(dado) >= 4 for dado in set(dados))

	def calcular_pontuacao(self, aCategoria_escolhida : int, aDados : list) -> int:
		pass

	def valida_full_house(self, dados : list) -> int:
		contagens = []
		contagens = [dados.count(dado) for dado in set(dados)]
		return sorted(contagens) == [2, 3]

	def valida_small_straight(self, dados : list) -> int:
		sequencias = [{1, 2, 3, 4}, {2, 3, 4, 5}, {3, 4, 5, 6}]
		return any(seq.issubset(set(dados)) for seq in sequencias)

	def valida_big_staight(self, dados : list) -> int:
		lista_ordenada = sorted(dados)
		
		if lista_ordenada == list(range(lista_ordenada[0], lista_ordenada[0] + 5)):
			return True
		
		return False

	def valida_yatch(self, dados : list) -> int:
		return all(numero == dados[0] for numero in dados)

	def atualizar_categoria(self, aPontos : int):
		pass

	def __init__(self):
		self.___categoria_escolhida : int = None
		self.___categoty_points : int = None
		self._unnamed_Tabela_ : Tabela = None
		"""# @AssociationMultiplicity 1"""
		self._unnamed_Mesa_ : Mesa = None
		self._unnamed_Prisao_ : Prisao = None

