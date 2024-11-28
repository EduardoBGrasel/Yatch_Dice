#!/usr/bin/python
# -*- coding: UTF-8 -*-
from DOG import DogActor
from DOG import StartStatus
from typing import List

class DOGPlayerInterface(object):
	def receive_start(self, aStart_status : StartStatus):
		pass

	def receive_move(self, aA_move : Directionary):
		pass

	def receive_withdrawal_notification(self):
		pass

	def start_match(self):
		pass

	def atualiza_gui(self):
		pass

	def __init__(self):
		self._dog_server_interface : DogActor = None
		self.___askyesno = None
		self._unnamed_DogActor_ : DogActor = None
		self._unnamed_StartStatus_ : StartStatus = None

