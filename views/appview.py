#! /usr/bin/env Python3
# coding: utf-8
""" tournament view.
    """
import datetime
import constants

# from models.player import Player, Players


class View:
    def prompt(
        text, type_response, default_response=None, closed_response=None
    ):
        """Attend une réponse conforme de l'utilisateur à l'input.

        text: le texte d'invite à afficher à l'utilisateur
        type_response: si test de valeur (int)>0 ou (date) attendu
        default_response:  si rien n'est saisi, cette valeur sera retournée
        closed_response: la réponse doit être une des valeurs de la liste
        """

        if not isinstance(text, str):
            raise ("Merci de vérifier le texte passé à prompt()")
            return
        if closed_response is not None and not isinstance(
            closed_response, list
        ):
            raise ("Merci de vérifier la liste passée à prompt()")
            return
        if isinstance(default_response, str):
            default_response_print = default_response
        else:
            default_response_print = str(default_response)

        input_text = (
            text + " (defaut:" + default_response_print + "):"
            if default_response is not None
            else " :"
        )

        while True:
            prompt_result = input(input_text)
            if default_response is not None and len(prompt_result) == 0:
                return default_response
            if len(prompt_result) != 0:
                if type_response == "int":
                    try:
                        if int(prompt_result) > 0:
                            break
                    except ValueError:
                        raise (
                            "Ce chiffre n'est pas valide, \
                            Merci de recommencer."
                        )
                if type_response == "date":
                    try:
                        jj, mm, aaaa = prompt_result.split("/")
                        datetime.datetime(int(aaaa), int(mm), int(jj))
                    except ValueError:
                        raise (
                            "Cette date n'est pas valide, \
                                Merci de recommencer."
                        )
                    else:
                        break
                if closed_response is not None:
                    if prompt_result in closed_response:
                        break
                if type_response == "str" and isinstance(prompt_result, str):
                    break
        return prompt_result

    def prompt_to_exit():
        exit_reply = View.prompt(
            "Voulez-vous quittez? (Y/N)\
                                   ",
            "str",
            "N",
            constants.YESORNO,
        )

        return True if exit_reply == "Y" else False


class TournamentView(View):
    def prompt_for_tournament(self):
        """Prompt for details."""
        name = View.prompt(
            "tapez le nom du tournoi : ", "str", "Paris grand tournoi"
        )
        description = View.prompt(
            "tapez une description du tournoi : ",
            "str",
            "Nous acceuillons nos voisins du 20eme.",
        )
        location = View.prompt("le lieu du tournoi : ", "str", "Paris 18e")
        date = View.prompt(
            "la date du tournoi (JJ/MM/AAAA): ",
            "date",
            datetime.date(2021, 12, 29).strftime("%d/%m/%Y"),
        )
        round_number = View.prompt("le nombre de ronde (défaut=4): ", "int", 4)
        time_control = View.prompt(
            "le type de partie : ",
            "str",
            constants.CONTROLS[0],
            constants.CONTROLS,
        )
        return name, description, location, date, round_number, time_control

    # TODO: retourner une list et dans le constructeur __init__ input[]
    # TODO: utiliser les decorateurs pour le controle des types

    def prompt_for_player_tournament(self):
        """Prompt for details."""

        name = View.prompt("tapez le nom du joueur", "str", "Martin")
        firstname = View.prompt("tapez le prénom du joueur : ", "str", "Paul")
        birthdate = View.prompt(
            "sa date de naissance (JJ/MM/AAAA): ",
            "date",
            datetime.date(2000, 1, 1).strftime("%d/%m/%Y"),
        )
        gender = View.prompt(
            "si indispensable, préciser le genre: ",
            "str",
            constants.GENDER[0],
            constants.GENDER,
        )
        initial_ranking = View.prompt("son classement ELO : ", "int", 100)
        return name, firstname, birthdate, gender, initial_ranking


class PlayerView(View):
    def prompt_for_player(self):
        """Prompt for details."""

        name = View.prompt("tapez le nom du joueur", "str", "Martin")
        firstname = View.prompt("tapez le prénom du joueur : ", "str", "Paul")
        birthdate = View.prompt(
            "sa date de naissance (JJ/MM/AAAA): ",
            "date",
            datetime.date(2000, 1, 1).strftime("%d/%m/%Y"),
        )
        gender = View.prompt(
            "si indispensable, préciser le genre: ",
            "str",
            constants.GENDER[0],
            constants.GENDER,
        )
        initial_ranking = View.prompt("son classement ELO : ", "int", 100)
        return name, firstname, birthdate, gender, initial_ranking

class PlayersView(View):
    
    def __init__(self, player_set):

        self._player_set = player_set


    def print_players(self):
        """
        """
        print(" Liste des joueurs de la base")
        print()
        self._player_set
        print()
        return 
