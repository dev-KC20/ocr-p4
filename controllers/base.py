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

        self.db = TinyDB('./data/db' + db_name + '.json', sort_keys=True)

    def save_tournament_players(self, db_name, known_players: Players):
        """ Save players added during tournament
             """
        for joueur in self.tournoi.players:
            known_players.players_known.append(joueur)

    def save_players(self, db_name, known_players: Players):
        """ Save players 
             """
        self.serialized_players = []
        self.use_database(db_name)
        self.players_table = self.db.table('players')
        self.players_table.truncate()
        for joueur in known_players:
            if joueur.__dict__.get('name'):
                self.serialized_players.append(joueur.__dict__)
        print(f' {len(self.serialized_players)} joueurs connus après tournoi')
        self.players_table.insert_multiple(self.serialized_players)

    def load_players(self, db_name, known_players: Players):
        """ Load saved players into Players()
             """
        self.de_serialized_players = []
        self.use_database(db_name)
        self.players_table = self.db.table('players')
        self.de_serialized_players = self.players_table.all()
        for joueur in self.de_serialized_players:
            known_players.append(
                Player(joueur['name'],
                       joueur['firstname'],
                       joueur['birthdate'],
                       joueur['gender'],
                       joueur['initial_ranking'],
                       joueur['point_earned'],
                       joueur['opponent_met']
# TODO: gérer son document id pour permettre la selection du joueur au tournoi
                    #    ,joueur['doc_id'])
               )   )
# TODO: créer une vue pour gérer les joueurs <> de tournament 
# qui devient ajout de joueur
  
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
        self.player_set = Players()
        self.load_players('test', self.player_set.players_known)
        print(f' {len(self.player_set.players_known)} joueurs connus initialement')
        self.tournoi = self.create_tournament()
        while True:
            player_new = Player(
             *TournamentView().prompt_for_player_tournament(self.player_set.players_known))
            if player_new is not None:
                self.tournoi.add_player_to_tournament(player_new)
            if TournamentView().prompt_to_exit():
                break
        self.save_tournament_players('test', self.player_set)
        self.save_players('test', self.player_set.players_known)

