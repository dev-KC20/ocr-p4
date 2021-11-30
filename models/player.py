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
        self.point_earned = 0
        self.opponent_met = []

    def update_ranking(self, score):
        """ The player rank is updated according to match result.
            """
        self.point_earned += score

    def __str__(self):
        
        self.formated_player = f""" {self.firstname} {self.name}, né\
             {self.birthdate} {self.initial_ranking} ELO, 
             score: {self.point_earned}"""
        return (self.formated_player)

# TODO: ranking rang general avant tournoi ; pdt le tournoi rang nul
# les points obtenus 


class Players:
    """ List of know chess players.
        """
    def __init__(self):
        self.known_players = []

    def add_player_to_list(self, new_player: Player):
        """register a player to the local list of player.
               """
        self.known_players.append(new_player)
        return True

