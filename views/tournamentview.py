#! /usr/bin/env Python3
# coding: utf-8
""" tournament view.
    """
import datetime
import constants


class TournamentView:

    def prompt(self, text, type_response, default_response=None, closed_response=None):
        """Attend une réponse conforme de l'utilisateur à l'input.

        text: le texte d'invite à afficher à l'utilisateur
        type_response: si test de valeur (int)>0 ou (date) attendu
        default_response:  si rien n'est saisi, cette valeur sera retournée
        closed_response: la réponse doit être une des valeurs de la liste
            """

        if not isinstance(text, str):
            raise("Merci de vérifier le texte passé à prompt()")
            return
        if closed_response is not None and not isinstance(closed_response,
                                                          list):
            raise("Merci de vérifier la liste passée à prompt()")
            return

        input_text = text + ' (defaut:' + str(default_response) +\
            '):' if default_response is not None else ' :'

        while True:
            prompt_result = input(input_text)
            if default_response is not None and len(prompt_result) == 0:
                return default_response
            if len(prompt_result) != 0:
                if type_response == 'int':
                    try:
                        if int(prompt_result) > 0:
                           break
                    except ValueError:
                        raise("Ce chiffre n'est pas valide, Merci de recommencer.")
                if type_response == 'date':
                    try:
                        jj, mm, aaaa = prompt_result.split('/')
                        datetime.datetime(int(aaaa), int(mm), int(jj))
                    except ValueError:
                        raise("Cette date n'est pas valide, Merci de recommencer.")
                    else:
                        break
                if closed_response is not None:
                    if prompt_result in closed_response:
                        break
                if type_response == 'str' and isinstance(prompt_result, str):
                    break
        return prompt_result

    def prompt_for_tournament(self):
        """Prompt for details."""
        name = self.prompt("tapez le nom du tournoi : ", "str", "Paris grand\
                            tournoi")
        description = self.prompt("tapez une description du tournoi : ", "str",
                                  "Nous acceuillons nos voisins du 20eme.")
        location = self.prompt("le lieu du tournoi : ", "str", "Paris 18e")
        date = self.prompt("la date du tournoi (JJ/MM/AAAA): ", "date",
                           29/12/2021)
        round_number = self.prompt("le nombre de ronde (défaut=4): ", "int", 4)
        time_control = self.prompt("le type de partie bullet, blitz ,rapide :\
                                   ", "str", "Blitz", constants.CONTROLS)
        return name, description, location, date, round_number, time_control
# TODO: retourner une list et dans le constructeur __init__ input[]
# TODO: utiliser les decorateurs pour le controle des types

    def prompt_for_player_tournament(self):
        """Prompt for details."""
        name = self.prompt("tapez le nom du joueur ou exit pour quitter ", "str", "Martin")
        if name != 'exit':
            firstname = self.prompt("tapez le prénom du joueur : ", "str", "Paul")
            birthdate = self.prompt("sa date de naissance (JJ/MM/AAAA): ", "date", "01/01/2000") 
            gender = self.prompt("si indispensable, préciser le genre: ", "str", "F", constants.GENDER)
            initial_ranking = self.prompt("son classement ELO : ", "int", 100)
        else:
            firstname = ''
            birthdate = 0
            gender = ''
            initial_ranking = 0
        return name, firstname, birthdate, gender, initial_ranking
