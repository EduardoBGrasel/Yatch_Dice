#!/usr/bin/python
# -*- coding: UTF-8 -*-
from dominio_da_solucao import Tabuleiro
from dominio_da_solucao import Jogador
from dominio_da_solucao import QPixmap
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

	def inicia_partida(self, aJogadores : string__, aId_jogador_local : str):
		pass

	def recebe_status(self) -> QPixmap:
		pass

	def soma_dados(self, aDados : list, aN : int) -> int:
		pass

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
		self.___entries : list = None
		self._unnamed_Tabuleiro_ : Tabuleiro = None
		self._unnamed_Jogador_ : Jogador = None
		self._unnamed_Categoria_ = []
		"""# @AssociationMultiplicity 11
		# @AssociationKind Aggregation"""

