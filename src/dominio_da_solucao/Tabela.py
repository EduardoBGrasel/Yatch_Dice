#!/usr/bin/python
# -*- coding: UTF-8 -*-
from typing import List

class Tabela(object):

	def soma_dados(self, n, dados) -> int:
		aux_dado_categoria = n
		aux_pontuacao_categoria = 0
		for dado in dados:
			dado_value = dado.dado_get_numero()
			if dado_value == aux_dado_categoria:
				aux_pontuacao_categoria += dado_value
		return aux_pontuacao_categoria

	def atribui_four_of_a_kind(self) -> int:
		return self.four_of_a_kind

	def atribui_full_house(self) -> int:
		return self.full_house
	
	def atribui_small_straight(self) -> int:
		return self.little_straight

	def atribui_big_straight(self) -> int:
		return self.big_straight

	def atribui_yatch(self) -> int:
		return self.yatch

	def atribui_zero(self) -> int:
		return self.zero;

	def __init__(self):
		self.yatch = 50
		self.big_straight = 35
		self.full_house = 25
		self.little_straight = 20
		self.four_of_a_kind = 40
		self.zero = 0


