#!/usr/bin/python
# -*- coding: UTF-8 -*-
from dominio_da_solucao import Tabuleiro
from dominio_da_solucao import Dado
from dominio_da_solucao import Copo
from dominio_da_solucao import Prisao
from dominio_da_solucao import Categoria
from dominio_da_solucao import Jogador
from typing import List

class Mesa(object):
	def receber_lista_dados(self, aDados : List) -> List:
		pass

	def receber_dado_selecionado(self) -> Dado:
		pass

	def get_turn_player(self) -> Jogador:
		pass

	def embaralhar_dados(self, aDados : List) -> List:
		pass

	def jogar_dados(self, aJogador : Jogador, aDados_selecioandos : list):
		pass

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
		pass

	def get_if_jogados(self) -> int:
		pass

	def get_if_selecionado(self) -> int:
		pass

	def get_maximo_selecao_atingido(self) -> int:
		pass

	def get_if_categoria_escolhida(self) -> int:
		pass

	def atualiza_dado(self, aDado : Dado):
		pass

	def atualiza_dados(self, aDados : list):
		pass

	def __init__(self):
		self.___dados_selecionados : list = None
		self.___dados : list = None
		self.___dados_jogados : int = None
		self.___dado_selecionado : int = None
		self.___maximo_selecao_atingido : int = None
		self.___player_turn : int = None
		self.___categoria_escolhida : int = None
		self._unnamed_Tabuleiro_ : Tabuleiro = None
		self._unnamed_Dado_ : Dado = None
		self._unnamed_Copo_ : Copo = None
		self._unnamed_Prisao_ : Prisao = None
		"""# @AssociationKind Composition"""
		self._unnamed_Categoria_ : Categoria = None
		"""# @AssociationKind Composition"""

