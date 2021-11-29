#! /usr/bin/env python
# coding: utf-8
"""Manage chess tournaments after swiss rules.

bla bla.
"""

# import constants
from models.tournament import Tournament
from models.player import Player
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
        tournoi_un.generate_player_set()
        tournoi_un.add_player_to_tournament(Player(
            *TournamentView().prompt_for_player_tournament()))

        for invite in tournoi_un.players:
            print(f' Les joueurs invités sont {invite}')
        for tour in range(tournoi_un.round_number):
            tournoi_un.add_round("Ronde" + str(tour+1))

        for ronde in tournoi_un.rounds:
            print(ronde)
