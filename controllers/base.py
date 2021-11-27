#! /usr/bin/env python
# coding: utf-8
"""Manage chess tournaments after swiss rules.

bla bla.
"""

# import constants
from models.tournament import Tournament
from views.tournamentview import TournamentView


class Controller:
    def __init__(self, view, action):
        """
         """
        self.view = view
        self.action = action

    def create_tournament(self):
        # * pour unpack le tuple de parm renvoyé par prompt_.
        tournoi_un = Tournament(*TournamentView().prompt_for_tournament())
        # temporary solution ; will use use add_player_to_tournament()
        tournoi_un.generate_player_set()
        # tournoi_un.add_player_to_tournament(*TournamentView().prompt_for_player_tournament())
# TODO : link Prompt_for_player_tournament()
# Traceback (most recent call last):
#   File "C:\Local\dev\python\ocr\p4\ocr-p4\main.py", line 13, in <module>
#     manage_event.create_tournament()
#   File "C:\Local\dev\python\ocr\p4\ocr-p4\controllers\base.py", line 25, in create_tournament
#     tournoi_un.add_player_to_tournament(*TournamentView().prompt_for_player_tournament())
# TypeError: add_player_to_tournament() takes 2 positional arguments but 6 were given
        for invite in tournoi_un.players:
            print(f' Les joueurs invités sont {invite}')
        for tour in range(tournoi_un.round_number):
            tournoi_un.add_round("Ronde" + str(tour+1))
       
        for ronde in tournoi_un.rounds:
            print(ronde)
