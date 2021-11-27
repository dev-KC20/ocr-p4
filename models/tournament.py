#! /usr/bin/env Python3
# coding: utf-8
""" tournament.
    """
import datetime
import random
import constants
from .player import Player
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
        self.rounds = [Round]
        self.players = [Player]
        self.time_control = time_control
        self.event_description = description

    def add_player_to_tournament(self, Player):
        """ask for and register a player to the tournament.
               """
        self.players.append(Player)

    def generate_player_set(self):
        """register a player to the tournament.
               """
        # PLAYERS is a set of players for testing purpose
        for joueur in constants.PLAYERS:
            self.players.append(Player(joueur,
                                       joueur[:constants.TEST_FIRSTNAME_SLICE],
                                self.get_random_birthdate(), 'Neutral',
                                random.randint(1, 2000)))

    def close_tournament(self, name):
        self.event_closing_date = datetime.date.today()

    def add_round(self, name):
        """add a round to the tournament.
            """
        if len(self.rounds) <= self.round_number:
            self.rounds.append(Round(name))

    def get_random_birthdate(self):
        """generate random birthdate.
            """
        birthdate = constants.TEST_START_DATE + \
            datetime.timedelta(seconds=random.randint(
                0, (constants.TEST_END_DATE -
                    constants.TEST_START_DATE).total_seconds()))
        return birthdate
