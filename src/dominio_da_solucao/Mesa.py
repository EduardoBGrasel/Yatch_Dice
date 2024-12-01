#!/usr/bin/python
# -*- coding: UTF-8 -*-
from dominio_da_solucao.Copo import Copo
from dominio_da_solucao.Categoria import Categoria
from dominio_da_solucao.Jogador import Jogador
from typing import List

class Mesa(object):
	def receber_lista_dados(self, aDados : List):
		pass

	def receber_dado_selecionado(self):
		pass

	def get_turn_player(self) -> Jogador:
		pass

	def embaralhar_dados(self, aDados : List) -> List:
		pass

	def dados_jogados(self, aJogador : Jogador, aDados_selecioandos : list):
		self.dados_jogados = self.copo.jogar_dados()

	def dado_selecionado(self, aJogador : Jogador) -> int:
		pass

	def escolher_categoria(self, aCategoria_escolhida : int):
		pass

	def informar_jogada_de_dados(self) -> int:
		pass

	def informar_dados_jogados(self) -> int:
		pass

	def informar_jogada_selecao(self) -> int:
		pass

	def informar_dado_selecionado(self) -> int:
		pass

	def get_dados(self) -> list:
		return self.dados_jogados

	def get_dados_selecionados(self):
		return self.dados_selecionados

	def get_if_jogados(self) -> int:
		pass

	def get_if_selecionado(self) -> int:
		pass

	def get_maximo_selecao_atingido(self) -> int:
		pass

	def get_if_categoria_escolhida(self) -> int:
		pass

	def atualiza_dado(self, aDado):
		pass

	def atualiza_dados(self, aDados : list):
		pass

	def __init__(self):
		self.dados_selecionados : list = None
		self.dados : list = None
		self.dados_jogados : int = None
		self.dado_selecionado : int = None
		self.maximo_selecao_atingido : int = None
		self.player_turn : int = None
		self.categoria_escolhida : int = None
		self.copo = Copo()

