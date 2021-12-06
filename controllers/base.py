#! /usr/bin/env python
# coding: utf-8
"""Manage chess tournaments after swiss rules.

But also manage a list of known players
"""

from tinydb import TinyDB  # , Query

# import constants
from models.tournament import Tournament
from models.player import Player, Players
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

    def use_database(self, db_name):
        self._db = TinyDB('./data/db' + db_name + '.json', sort_keys=True)
        return self._db

    def save_tournament_players_in(self, db_name, known_players: Players):
        """ Save players added during tournament
             """
        for joueur in self.tournoi.players:
            known_players.players_known.append(joueur)

    def manage_player(self):
        """
             """
        self.player_set = Players()
        self.load_players('test', self.player_set.players_known)
        print(f' {len(self.player_set.players_known)} joueurs connus initialement')
        while True:
            player_new = Player(
                *TournamentView().prompt_for_player())
            if player_new is not None:
                self.player_set.add_player_to_list(player_new)
            if TournamentView().prompt_to_exit():
                break
        self.save_players('test', self.player_set.players_known)

    def run(self):
        """
             """
        db_name = 'test'
        db = self.use_database(db_name)
        self.player_set = Players()
        self.player_set.load_players(db, 'players')
        print(
            f' {self.player_set.get_number_of__players()} joueurs connus initialement')
        self.tournoi = self.create_tournament()
        while True:
            player_new = Player(
                *TournamentView().prompt_for_player_tournament())
            if player_new is not None:
                self.tournoi.add_player_to_tournament(player_new)
                self.tournoi.add_player_to_players(player_new, self.player_set)
            if TournamentView().prompt_to_exit():
                break
        print(
            f' {self.player_set.get_number_of__players()} joueurs connus avant sauvegarde')
        self.player_set.save_players(db, 'players')
