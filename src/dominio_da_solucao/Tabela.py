#!/usr/bin/python
# -*- coding: UTF-8 -*-
from dominio_da_solucao import Tabuleiro
from dominio_da_solucao import Jogador
from typing import List

class Tabela(object):
	def pontuacao_atribuida(self, aPontuacao : int):
		pass

	def informar_jogada_categoria(self) -> int:
		pass

	def informar_pontuacao(self) -> int:
		pass

	def recebe_status_partida_(self) -> int:
		pass

	def inicia_partida(self, aJogadores : str, aId_jogador_local : str):
		pass

	def recebe_status(self):
		pass

	def soma_dados(self, n, dados) -> int:
		aux_dado_categoria = n
		aux_pontuacao_categoria = 0
		for dado in dados:
			dado_value = dado.dado_get_numero()
			if dado_value == aux_dado_categoria:
				aux_pontuacao_categoria += dado_value
		return aux_pontuacao_categoria

	def atribui_four_of_a_kind(self) -> int:
		pass

	def atribui_zero(self) -> int:
		pass

	def atribui_full_house(self) -> int:
		pass

	def atribui_small_straight(self) -> int:
		pass

	def atribui_big_straight(self) -> int:
		pass

	def atribui_yatch(self) -> int:
		pass

	def __init__(self):
		self.yatch = 50
		self.big_straight = 35
		self.full_house = 25
		self.little_straight = 20
		self.four_of_a_kind = 40


