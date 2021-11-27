#! /usr/bin/env Python3
# coding: utf-8
""" Player who will participate to the tournament.
    """

# import constants    


class Player:
    """ Person attending a chess tournament.
        """
    def __init__(self, name, firstname, birthdate, gender, initial_ranking):
        self.name = name
        self.firstname = firstname
        self.birthdate = birthdate
        self.gender = gender
        self.initial_ranking = initial_ranking
        self.current_ranking = initial_ranking

    def update_ranking(self, score):
        """ The player rank is updated according to match result.
            """
        self.current_ranking += score

    def __str__(self):
        return (f" {self.firstname} {self.name}, né {self.birthdate} {self.initial_ranking} ELO -> {self.current_ranking}")
