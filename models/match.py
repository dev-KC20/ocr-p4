#! /usr/bin/env Python3
# coding: utf-8
""" match.
    """


class Match:
    """ round.
        """
    def __init__(self):
        self.match_result = []

    def register_score(self, player_list, score_list):
        self.match_result = list(zip(player_list, score_list))
