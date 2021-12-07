#! /usr/bin/env python
# coding: utf-8
"""Manage chess tournaments after swiss rules.

But also manage a list of known players
"""
from tinydb import TinyDB  # , Query

from models.player import Player, Players
from models.tournament import Tournament
from utils.menu import Menu
from views.menuview import MenuView
from views.tournamentview import TournamentView


class AppController:
    def __init__(self):
        self.controller = None

    def start(self):
        self.controller = MenuController().run()
        while self.controller:
            self.controller = self.controller.run()


class MenuController:

    def run(self):
        """
            """
        self.menu = Menu()
        self.menu.add_menu("10", "Gérer les joueurs", MenuPlayerController())
        self.menu.add_menu("20", "Organiser un tournoi", MenuTournamentController())
        self.menu.add_menu("40", "Afficher les rapports", MenuReportsController())
        self.menu.add_menu("50", "Charger/Sauver les données", MenuDBController())
        self.menu.add_menu("90", "Quitter l'application", MenuExitController())
        chosen_option = MenuView(self.menu).get_user_input()
        next_menu = self.menu.get_action(chosen_option)
        return next_menu

class MenuPlayerController:

    def run(self):
        """
            """
        self.menu = Menu()
        self.menu.add_menu("10", "Afficher la liste des joueurs", MenuPlayerController())
        self.menu.add_menu("20", "Créer un joueur", MenuTournamentController())
        self.menu.add_menu("80", "Retour à l'accueil", MenuController())
        self.menu.add_menu("90", "Quitter l'application", MenuExitController())
        chosen_option = MenuView(self.menu).get_user_input()
        next_menu = self.menu.get_action(chosen_option)
        return next_menu


class MenuTournamentController:

    def run(self):
        """
            """
        self.menu = Menu()
        self.menu.add_menu("10", "Créer un tournoi", MenuPlayerController())
        self.menu.add_menu("20", "Mettre à jour les résultats", MenuTournamentController())
        self.menu.add_menu("80", "Retour à l'accueil", MenuController())
        self.menu.add_menu("90", "Quitter l'application", MenuExitController())
        chosen_option = MenuView(self.menu).get_user_input()
        next_menu = self.menu.get_action(chosen_option)
        return next_menu


class MenuReportsController:

    def run(self):
        """
            """
        self.menu = Menu()
        self.menu.add_menu("10", "Liste de tous les joueurs", MenuPlayerController())
        self.menu.add_menu("20", "Liste des joueurs d'un tournoi", MenuTournamentController())
        self.menu.add_menu("30", "Liste des tournois", MenuReportsController())
        self.menu.add_menu("40", "Liste des tours d'un tournoi", MenuDBController())
        self.menu.add_menu("50", "Liste des matchs d'un tournoi", MenuDBController())
        self.menu.add_menu("80", "Retour à l'accueil", MenuController())
        self.menu.add_menu("90", "Quitter l'application", MenuExitController())
        chosen_option = MenuView(self.menu).get_user_input()
        next_menu = self.menu.get_action(chosen_option)
        return next_menu

 
class MenuDBController:

    def run(self):
        """
            """
        self.menu = Menu()
        self.menu.add_menu("10", "Charger les joueurs", MenuPlayerController())
        self.menu.add_menu("20", "Charger les tournois", MenuTournamentController())
        self.menu.add_menu("11", "Sauver les joueurs", MenuPlayerController())
        self.menu.add_menu("21", "Sauver les tournois", MenuTournamentController())
        self.menu.add_menu("80", "Retour à l'accueil", MenuController())
        self.menu.add_menu("90", "Quitter l'application", MenuExitController())
        chosen_option = MenuView(self.menu).get_user_input()
        next_menu = self.menu.get_action(chosen_option)
        return next_menu

class MenuExitController:

    def run(self):
        """
            """
        self.menu = Menu()            
        return MenuView(self.menu).good_bye()


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