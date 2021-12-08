#! /usr/bin/env Python3
# coding: utf-8
""" match.
    """


class Match:
    """Match is the result of 2 players during one round."""

    def __init__(self):
        self._match_result = []

    def register_score(self, player_list, score_list):
        """Attach players and scores to the match."""
        self._match_result = list(zip(player_list, score_list))


# TODO: Possibilité d'ins"rer des tests unitaire
# saisir plusieurs matchs exemples et vérifier le resultat attendu
# les scores sont liés si joueur1 =1 => joueur2 =0
