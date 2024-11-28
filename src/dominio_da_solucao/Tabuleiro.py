#!/usr/bin/python
# -*- coding: UTF-8 -*-
from dominio_da_solucao import Jogador
from dominio_da_solucao import QPixmap
from dominio_da_solucao import Estado
from dominio_da_solucao import Mesa
from dominio_da_solucao import Tabela
from Interface import PlayerInterface
from dominio_da_solucao import Dado
from typing import List

class Tabuleiro(object):
	def iniciar_partida(self, aJogadores : str, aId_jogador_local : int):
		pass

	def receber_movimento(self, aA_movimento : Dictionary):
		pass

	def receber_notificacao_abandono(self):
		pass

	def get_status(self) -> QPixmap:
		pass

	def atribuir_pontuacao_jogador(self, aPontos : int):
		pass

	def receber_selecao_de_dado(self, aDado : Dado):
		pass

	def get_turn_player(self) -> Jogador:
		pass

	def jogar_dados(self, aLista_dados : list):
		pass

	def dado_selecionado(self) -> int:
		pass

	def escolher_categoria(self, aCategoria_escolhida : int):
		pass

	def verifica_final(self, aRounds : int) -> int:
		pass

	def verifica_vencedor(self, aPontuacao, aPontuacao_remota) -> int:
		pass

	def atualizar_estado(self):
		pass

	def indentificar_area_acao(self) -> str:
		pass

	def __init__(self):
		self.___rounds : int = None
		self.___player_turn : int = None
		self.___jogador_local : Jogador = None
		self.___jogador_remoto : Jogador = None
		self._unnamed_QPixmap_ : QPixmap = None
		self._unnamed_Estado_ : Estado = None
		self._unnamed_Jogador_ = []
		"""# @AssociationMultiplicity 2
		# @AssociationKind Composition"""
		self._unnamed_Mesa_ : Mesa = None
		"""# @AssociationKind Composition"""
		self._unnamed_Tabela_ : Tabela = None
		"""# @AssociationKind Composition"""
		self._unnamed_PlayerInterface_ : PlayerInterface = None

