#! /usr/bin/env Python3
# coding: utf-8
""" tournament.
    """
import datetime
import random
from .player import Player, PLAYERS
from .round import Round

CONTROLS = ("bullet", "blitz", "fast")
TEST_FIRSTNAME_SLICE = 2
TEST_START_DATE = datetime.date(1940, 1, 1)
TEST_END_DATE = datetime.date(2000, 1, 1)


class Tournament:
    def __init__(self, name, description, location,
                 date: datetime, round_number=4,
                 time_control=CONTROLS[0]):
        self.event_name = name
        self.event_location = location
        self.event_start_date = datetime.date.today()
        self.event_closing_date = None
        self.round_number = round_number
        self.rounds = [Round]
        self.players = [Player]
        self.time_control = time_control
        self.event_description = description

    def add_player(self, name):
        """register a player to the tournament.
               """
        self.players.append(Player(name))

    def add_player_set(self):
        """register a player to the tournament.
               """
        # PLAYERS is a set of players for testing purpose
        for joueur in PLAYERS:
            self.players.append(Player(joueur, joueur[:TEST_FIRSTNAME_SLICE],
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
        birthdate = TEST_START_DATE + \
            datetime.timedelta(seconds=random.randint(
                0, (TEST_END_DATE-TEST_START_DATE).total_seconds()))
        return birthdate
