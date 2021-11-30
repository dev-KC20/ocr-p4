#! /usr/bin/env python
# coding: utf-8
"""Manage chess tournaments after swiss rules.

bla bla.
"""
from tinydb import TinyDB  # , Query

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

    def use_database(self, db_name):

        self.db = TinyDB('./data/db' + db_name + '.json', sort_keys=True)

    def save_players(self, db_name):
        """
             """
        self.serialized_players = []
        self.use_database(db_name)
        self.players_table = self.db.table('players')
        print(f""" Nombre de joueurs présents en base {db_name}: 
              {len(self.players_table)}""")
        # self.players_table.truncate()
        # prompted players to be serialized        
        for joueur in self.tournoi.players:
            # DONE: Players were serialized using built-in method __dict__
            if joueur.__dict__.get('name'):
                self.serialized_players.append(joueur.__dict__) 
        self.players_table.insert_multiple(self.serialized_players)

    def load_players(self, db_name):
        """
             """
        self.de_serialized_players = []
        self.use_database(db_name)
        self.players_table = self.db.table('players')
        self.de_serialized_players = self.players_table.all()
        # print(f' loaded players: {self.de_serialized_players}')
        # prompted players to be serialized        
        # for joueur in self.tournoi.players:
        #     print(joueur.__dict__)
        #     if joueur.__dict__.get('name'):
        #         self.serialized_players.append(joueur.__dict__) 
        # self.players_table.insert_multiple(self.serialized_players)

    def run(self):
        """
             """
        self.load_players('test')
        self.tournoi = self.create_tournament()
        while False:
            player_new = Player(
             *TournamentView().prompt_for_player_tournament())
            self.tournoi.add_player_to_tournament(player_new)
            if self.prompt_to_exit():
                break
        self.save_players('test')

