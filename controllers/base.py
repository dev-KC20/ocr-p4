#! /usr/bin/env python
# coding: utf-8
"""Manage chess tournaments after swiss rules.

bla bla.
"""
from tinydb import TinyDB, Query

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
        return Tournament(*TournamentView().prompt_for_tournament())
        # tournoi_un.generate_player_set()
        # for invite in tournoi_un.players:
        #     print(f' Les joueurs invités sont {invite}')
        # for tour in range(tournoi_un.round_number):
        #     tournoi_un.add_round("Ronde" + str(tour+1))

        # for ronde in tournoi_un.rounds:
        #     print(ronde)

    def use_database(self, name):

        self.db = TinyDB('db' + name + '.json')

    def run(self):
        """
             """
        self.tournoi = self.create_tournament()
        while True:
            player_new = Player(
             *TournamentView().prompt_for_player_tournament())
            if player_new.name != 'exit':
                self.tournoi.add_player_to_tournament(player_new)
            else:
                break

# TODO: prepare serialisation 
        for joueur in self.tournoi.players:
            print(joueur.__dict__)

