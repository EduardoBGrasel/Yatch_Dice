#!/usr/bin/python
# -*- coding: UTF-8 -*-
from DOG import DOGPlayerInterface
from DOG import StartStatus
from typing import List

class DogActor(object):
	def inicialize(self, aPlayer_name : str, aPlayer_actor : DogPlayerInterface) -> str:
		pass

	def star_match(self, aNumber_of_players : int) -> StartStatus:
		pass

	def send_move(self, aMove_to_send : Dictionary):
		pass

	def start_status(self, aNumero_de_jogadores : int):
		pass

	def get_code(self) -> str:
		pass

	def get_message(self) -> str:
		pass

	def __init__(self):
		self._player_actor : DogPlayerInterface = None
		self._unnamed_DOGPlayerInterface_ : DOGPlayerInterface = None
		self._unnamed_StartStatus_ : StartStatus = None

