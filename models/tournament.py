#! /usr/bin/env Python3
# coding: utf-8
""" tournament.
    """
import datetime
# import random
import constants
from .player import Player, Players
from .round import Round


class Tournament:
    def __init__(self, name, description, location,
                 date: datetime, round_number=constants.ROUND_DEFAULT,
                 time_control=constants.CONTROLS[0]):
        self.event_name = name
        self.event_location = location
        self.event_start_date = date
        self.event_closing_date = None
        self.round_number = int(round_number)
        self.rounds = []
        self.players = []
        self.time_control = time_control
        self.event_description = description

    def add_player_to_tournament(self, new_player: Player):
        """ask for and register a player to the tournament.
               """
        self.players.append(new_player)

    def add_player_to_players(self, new_player: Player, all_players: Players):
        """ask for and register a player to the tournament.
               """
        all_players.add_player_to_list(new_player)

    def close_tournament(self, name):
        self.event_closing_date = datetime.date.today()

    def add_round(self, name):
        """add a round to the tournament.
            """
        if len(self.rounds) <= self.round_number:
            self.rounds.append(Round(name))

