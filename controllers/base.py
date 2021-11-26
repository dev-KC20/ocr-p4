#! /usr/bin/env python
# coding: utf-8
"""Manage chess tournaments after swiss rules.

bla bla.
"""
from models.tournament import Tournament


class Controller:
    def __init__(self):
        """
         """

        tournoi_un = Tournament("Blitz d'echec",
                                "organisé par le club de Paris10e",
                                "Paris",
                                2021-10-10
                                )
        tournoi_un.add_player_set()
        for invite in tournoi_un.players:
            print(f' Les joueurs invités sont {invite}')

        tournoi_un.add_round("Ronde1")
        tournoi_un.add_round("Ronde2")
        tournoi_un.add_round("Ronde3")
        tournoi_un.add_round("Ronde4")
        tournoi_un.add_round("Ronde5")

        for ronde in tournoi_un.rounds:
            print(ronde)
