#! /usr/bin/env Python3
# coding: utf-8
""" round.
    """

import datetime
from .match import Match


class Round:
    """ round.
        """
    def __init__(self, name):
        self.round_name = name
        self.round_start_date = datetime.date.today()
        self.round_start_time = datetime.datetime.now().time()
        self.round_end_date = None
        self.round_end_time = None
        self.matchs = [Match]

    def close_round(self):
        """ closing a round.
            """
        self.round_end_date = datetime.date.today()
        self.round_end_time = datetime.datetime.now().time()

    def add_match(self, match):
        """ adding a match to a round.
            """
        self.matchs.append(self.Match())

    def __str__(self):
        return (f" Ronde {self.round_name} débuté le {self.round_start_date} à {self.round_start_time} ")
