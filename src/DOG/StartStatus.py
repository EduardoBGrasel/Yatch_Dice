#!/usr/bin/python
# -*- coding: UTF-8 -*-
from DOG import DogActor
from DOG import DOGPlayerInterface
from typing import List

class StartStatus(object):
	def get_code(self) -> str:
		pass

	def get_message(self) -> str:
		pass

	def get_local_id(self) -> str:
		pass

	def get_players(self) -> str*:
		pass

	def __init__(self):
		self._local_id : str = None
		self._code : str = None
		self._message : str = None
		self._players : str* = None
		self._unnamed_DogActor_ : DogActor = None
		self._unnamed_DOGPlayerInterface_ : DOGPlayerInterface = None

