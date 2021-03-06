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
from views.appview import TournamentView, PlayersView


class AppController:
    def __init__(self):
        self.controller = None
        self.db_name = "test"
        self.players_view = None
        self.tournament_view = None
        # self._player_set = None
        # start the menu loop
        self.controller = MenuController().run()

    def use_database(self, db_name):
        self._db = TinyDB("./data/db" + db_name + ".json", sort_keys=True)
        return self._db

    def save_tournament_players_in(self, db_name, known_players: Players):
        """Save players added during tournament"""
        for joueur in self.tournoi.players:
            known_players.players_known.append(joueur)

    def create_tournament(self):
        """ """
        self.tournoi = Tournament(*TournamentView().prompt_for_tournament())
        while True:
            player_new = Player(
                *TournamentView().prompt_for_player_tournament()
            )
            if player_new is not None:
                self.tournoi.add_player_to_tournament(player_new)
                self.tournoi.add_player_to_players(
                    player_new, self._player_set
                )
            if TournamentView().prompt_to_exit():
                break

    def start(self):
        # initialize DB and get players from DB
        self.db = self.use_database(self.db_name)
        self._player_set = Players()
        self._player_set.load_players(self.db, "players")

        # initialize app views
        self.players_view = PlayersView(self._player_set)
        # show loaded player list
        self.players_view.print_players()
        # manage menus
        while self.controller:
            self.controller = self.controller.run()
        # back up data
        self._player_set.save_players(self.db, "players")


class MenuController:
    def run(self):
        """ """
        self.menu = Menu()
        self.menu.add_menu("10", "G??rer les joueurs", MenuPlayerController())
        self.menu.add_menu(
            "20", "Organiser un tournoi", MenuTournamentController()
        )
        self.menu.add_menu(
            "40", "Afficher les rapports", MenuReportsController()
        )
        self.menu.add_menu(
            "50", "Charger/Sauver les donn??es", MenuDBController()
        )
        self.menu.add_menu("90", "Quitter l'application", MenuExitController())
        chosen_option = MenuView(self.menu).get_user_input()
        next_menu = self.menu.get_action(chosen_option)
        return next_menu


class MenuPlayerController:
    def run(self):
        """ """
        self.menu = Menu()
        self.menu.add_menu(
            "10", "Afficher la liste des joueurs", MenuPlayerController()
        )
        self.menu.add_menu("20", "Cr??er un joueur", MenuTournamentController())
        self.menu.add_menu("80", "Retour ?? l'accueil", MenuController())
        self.menu.add_menu("90", "Quitter l'application", MenuExitController())
        chosen_option = MenuView(self.menu).get_user_input()
        if chosen_option == "10":
            # TODO: solve
            print("acc??der ?? la view d'affichage")
        next_menu = self.menu.get_action(chosen_option)
        return next_menu


class MenuTournamentController:
    def run(self):
        """ """
        self.menu = Menu()
        self.menu.add_menu(
            "10", "Cr??er un tournoi", MenuTournamentController()
        )
        self.menu.add_menu(
            "20", "Mettre ?? jour les r??sultats", MenuTournamentController()
        )
        self.menu.add_menu("80", "Retour ?? l'accueil", MenuController())
        self.menu.add_menu("90", "Quitter l'application", MenuExitController())
        chosen_option = MenuView(self.menu).get_user_input()
        if chosen_option == "10":
            Tournament(*TournamentView().prompt_for_tournament())
        next_menu = self.menu.get_action(chosen_option)
        return next_menu


class MenuReportsController:
    def run(self):
        """ """
        self.menu = Menu()
        self.menu.add_menu(
            "10", "Liste de tous les joueurs", MenuReportsController()
        )
        self.menu.add_menu(
            "20", "Liste des joueurs d'un tournoi", MenuTournamentController()
        )
        self.menu.add_menu("30", "Liste des tournois", MenuReportsController())
        self.menu.add_menu(
            "40", "Liste des tours d'un tournoi", MenuDBController()
        )
        self.menu.add_menu(
            "50", "Liste des matchs d'un tournoi", MenuDBController()
        )
        self.menu.add_menu("80", "Retour ?? l'accueil", MenuController())
        self.menu.add_menu("90", "Quitter l'application", MenuExitController())
        chosen_option = MenuView(self.menu).get_user_input()
        next_menu = self.menu.get_action(chosen_option)
        return next_menu


class MenuDBController:
    def run(self):
        """ """
        self.menu = Menu()
        self.menu.add_menu("10", "Charger les joueurs", MenuPlayerController())
        self.menu.add_menu(
            "20", "Charger les tournois", MenuTournamentController()
        )
        self.menu.add_menu("11", "Sauver les joueurs", MenuPlayerController())
        self.menu.add_menu(
            "21", "Sauver les tournois", MenuTournamentController()
        )
        self.menu.add_menu("80", "Retour ?? l'accueil", MenuController())
        self.menu.add_menu("90", "Quitter l'application", MenuExitController())
        chosen_option = MenuView(self.menu).get_user_input()
        next_menu = self.menu.get_action(chosen_option)
        return next_menu


class MenuExitController:
    def run(self):
        """ """
        self.menu = Menu()
        return MenuView(self.menu).good_bye()
