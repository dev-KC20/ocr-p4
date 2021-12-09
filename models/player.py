#! /usr/bin/env Python3
# coding: utf-8
""" Player who will participate to the tournament.
    """
# import constants
# from tinydb import TinyDB  # , Query


class Player:
    """Person attending a chess tournament."""

    def __init__(
        self,
        name,
        firstname,
        birthdate,
        gender,
        initial_ranking,
        point_earned=0,
        opponent_met=[],
        doc_id=None,
    ):
        self._name = name
        self._firstname = firstname
        self._birthdate = birthdate
        self._gender = gender
        self._initial_ranking = initial_ranking
        self._point_earned = point_earned
        self._opponent_met = opponent_met
        self._doc_id = doc_id

    def update_ranking(self, score):
        """The player rank is updated according to match result."""
        self._point_earned += score

    def __str__(self):
        self._formated_player = f""" {self._firstname} {self._name}, né\
             {self._birthdate} {self._initial_ranking} ELO,
             score: {self._point_earned}"""
        return self._formated_player


# TODO: ranking rang general avant tournoi ; pdt le tournoi rang nul
# les points obtenus
class Players:
    """List of know chess players."""

    def __init__(self):
        self._players_known = []

    def add_player_to_list(self, new_player: Player):
        """register a player to the local list of player."""
        self._players_known.append(new_player)
        return True

    def get_number_of_players(self):
        """number of player."""
        return len(self._players_known)

    def get_list_of_players(self):
        """list of all players"""
        return self._players_known

    # def __str__(self):
    #     return self.__str__()
    def load_players(self, db, db_table):
        """Load saved players into Players()"""
        self.de_serialized_players = []
        self.players_table = db.table(db_table)
        self.de_serialized_players = self.players_table.all()
        for joueur in self.de_serialized_players:
            self._players_known.append(
                Player(
                    joueur["_name"],
                    joueur["_firstname"],
                    joueur["_birthdate"],
                    joueur["_gender"],
                    joueur["_initial_ranking"],
                    joueur["_point_earned"],
                    joueur["_opponent_met"]
                    # TODO: gérer son document id pour permettre la selection
                    # du joueur au tournoi
                    #    ,joueur['doc_id'])
                )
            )
        print(f" {len(self._players_known)} joueurs chargés")

    def save_players(self, db, db_table):
        """Save players
        Save uses the fact that a class has a description as dictionnary
        the meta structure record is avoided.
        """
        self.serialized_players = []
        self.players_table = db.table(db_table)
        self.players_table.truncate()
        for joueur in self._players_known:
            # only append data records
            if joueur.__dict__.get("_name"):
                self.serialized_players.append(joueur.__dict__)
        self.players_table.insert_multiple(self.serialized_players)
        print(f" {len(self.serialized_players)} joueurs sauvés")
        # self.players_table.update_multiple(self.serialized_players)
