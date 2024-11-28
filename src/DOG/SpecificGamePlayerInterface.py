#!/usr/bin/python
# -*- coding: UTF-8 -*-
from DOG import DOGPlayerInterface
from typing import List

class SpecificGamePlayerInterface(DOGPlayerInterface):
	def receive_start(self, aStart_status : StatuStatus):
		pass

	def receive_move(self, aA_move : Dictionary):
		pass

	def receive_withdrawal_notification(self):
		pass

	def request_player_name(self) -> str:
		pass

	def notify_result(self, aMessage : str):
		pass

	def proceed_start(self, *aPlayers : str*, aLocal_player_id : str):
		pass

	def askyesno(self, aParameter : str = 'START', aParameter2 : str = 'Deseja iniciar nova partida?'):
		pass

