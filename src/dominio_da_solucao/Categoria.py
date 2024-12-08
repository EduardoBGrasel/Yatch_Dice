#!/usr/bin/python
# -*- coding: UTF-8 -*-
from dominio_da_solucao.Tabela import Tabela

class Categoria(object):

	def atribuir_pontuacao(self, categoria_escolhida, dados):

		if categoria_escolhida in [1,2,3,4,5,6]:
			return self.tabela.soma_dados(categoria_escolhida, dados)

		if categoria_escolhida == 7: # four of a kind
			if self.valida_for_of_a_kind(dados):
				return self.tabela.atribui_four_of_a_kind()
			else:
				return self.tabela.atribui_zero()

		if categoria_escolhida == 8: # full house
			if self.valida_full_house(dados):
				return self.tabela.atribui_full_house()
			else:
				return self.tabela.atribui_zero()

		if categoria_escolhida == 9: # small straight
			if self.valida_small_straight(dados):
				return self.tabela.atribui_small_straight()
			else:
				return self.tabela.atribui_zero()	

		if categoria_escolhida == 10: # big straight
			if self.valida_big_staight(dados):
				return self.tabela.atribui_big_straight()
			else:
				return self.tabela.atribui_zero()

		if categoria_escolhida == 11: # yatch
			if self.valida_yatch(dados):
				return self.tabela.atribui_yatch()
			else:
				return self.tabela.atribui_zero()

	def valida_for_of_a_kind(self, dados : list) -> int:
		if any(dados.count(dado) >= 4 for dado in set(dados)):
			aux_valido = True
		else: aux_valido = False

		return aux_valido

	def valida_full_house(self, dados : list) -> int:
		contagens = []
		contagens = [dados.count(dado) for dado in set(dados)]

		if sorted(contagens) == [2, 3]:
			aux_valido = True
		else: aux_valido = False

		return aux_valido

	def valida_small_straight(self, dados : list) -> int:
		sequencias = [{1, 2, 3, 4}, {2, 3, 4, 5}, {3, 4, 5, 6}]    

		if any(seq.issubset(set(dados)) for seq in sequencias):
			aux_valido = True
		else: aux_valido = False

		return aux_valido

	def valida_big_staight(self, dados : list) -> int:
		lista_ordenada = sorted(dados)
		aux_valido = False
		
		if lista_ordenada == list(range(lista_ordenada[0], lista_ordenada[0] + 5)):
			aux_valido = True
		else: aux_valido = False

		return aux_valido

	def valida_yatch(self, dados : list) -> int:
		return all(numero == dados[0] for numero in dados)

	def __init__(self):
		self.categoria_escolhida : int = None
		self.tabela = Tabela()
