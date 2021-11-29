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
        return (f" {self.firstname} {self.name}, né {self.birthdate} {self.initial_ranking} ELO, score: {self.point_earned}")

# TODO: ranking rang general avant tournoi ; pdt le tournoi rang nul
# les points obtenus 

# TODO: solve this introuced a asdict to get the serialized version of the players
# <class 'models.player.Player'>
# Traceback (most recent call last):
#   File "C:\Local\dev\python\ocr\p4\ocr-p4\main.py", line 13, in <module>
#     manage_event.run()
#   File "C:\Local\dev\python\ocr\p4\ocr-p4\controllers\base.py", line 46, in run
#     print(joueur.asdict(joueur).items())
#   File "C:\Local\dev\python\ocr\p4\ocr-p4\models\player.py", line 33, in asdict
#     player_dict = {'name': self.name,
# AttributeError: type object 'Player' has no attribute 'name'

    # def asdict():
    #     player_dict = {'name': Player.self.name, 
    #                    'firstname': Player.self.firstname,
    #                    'birthdate': Player.self.birthdate, 
    #                    'gender': Player.self.gender,
    #                    'initial_ranking': Player.self.initial_ranking, 
    #                    'point_earned': Player.self.point_earned, 
    #                    'opponent_met': Player.self.opponent_met}
    #     # print(player_dict)
    #     return player_dict
