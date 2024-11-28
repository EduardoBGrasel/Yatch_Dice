#!/usr/bin/python
# -*- coding: UTF-8 -*-
from dominio_da_solucao import Tabuleiro
from dominio_da_solucao import Tabela
from dominio_da_solucao import QPixmap
from typing import List

class Jogador(object):
	def atribuir_pontuacao(self, aPontos : int) -> int:
		pass

	def eh_seu_turno(self) -> int:
		pass

	def inverter_turno(self):
		pass

	def informar_vez(self) -> int:
		pass

	def informa_vencedor(self) -> int:
		pass

	def informa_jogador(self) -> str:
		pass

	def reiniciar(self):
		pass

	def initialize(self, aSymbol : int, aIdentifier : str, aName : str):
		pass

	def toogle_turn(self):
		pass

	def iniciar_partida(self):
		pass

	def atualiza_gui(self, aEstado_jogo : QPixmap):
		pass

	def pontuacao_atribuida(self):
		pass

	def get_rounds_finalizados(self) -> int:
		pass

	def get_vencedor(self) -> int:
		pass

	def verifica_pontuacao_diferente(self) -> int:
		pass

	def __init__(self):
		self.___attempts : int = None
		self.___total_points : int = None
		self.___nome_jogador : str = None
		self.___rounds_finalizados : int = None
		self.___vencedor : int = None
		self.___turno : int = None
		self.___pontuacao_round_atribuida : int = None
		self.___jogada_finalizada : int = None
		self._unnamed_Tabuleiro_ : Tabuleiro = None
		self._unnamed_Tabela_ : Tabela = None

