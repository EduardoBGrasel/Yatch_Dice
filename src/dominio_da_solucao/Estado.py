#!/usr/bin/python
# -*- coding: UTF-8 -*-
from dominio_da_solucao import Tabuleiro
from typing import List

class Estado(object):
	def informar_mensagem(self) -> str:
		pass

	def __init__(self):
		self.___mensagem = None
		self._unnamed_Tabuleiro_ : Tabuleiro = None

