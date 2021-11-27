#! /usr/bin/env Python3
# coding: utf-8
""" tournament view.
    """
import datetime
import constants


class TournamentView:

    def prompt_for_tournament(self):
        """Prompt for details."""
        while True:
            name = input("tapez le nom du tournoi : ")
            if name:
                break
        while True:
            description = input("tapez une description du tournoi : ")
            if description:
                break
        while True:
            location = input("le lieu du tournoi : ")
            if location:
                break
        while True:
            date = input("la date du tournoi (JJ/MM/AAAA): ")
            try:
                jj, mm, aaaa = date.split('/')
                datetime.datetime(int(aaaa), int(mm), int(jj))
            except ValueError:
                print("Cette date n'est pas valide, Merci de recommencer.")
            else:
                break
        round_number = input("le nombre de ronde (défaut=4): ")
        if len(round_number) == 0:
            round_number = 4
        else:
            while True:
                try:
                    round_number = int(input("le nombre de ronde : "))
                except ValueError:
                    print("Merci de saisir un entier positif.")
                else:
                    if round_number > 0:
                        break
        while True:
            time_control = input("le type de partie bullet, blitz ,rapide : ")
            if time_control in constants.CONTROLS:
                break

        return name, description, location, date, round_number, time_control

    def prompt_for_player_tournament(self):
        """Prompt for details."""
        while True:
            name = input("tapez le nom du joueur : ")
            if name:
                break
        while True:
            firstname = input("tapez le prénom du joueur : ")
            if firstname:
                break
        while True:
            birthdate = input("sa date de naissance (JJ/MM/AAAA): ") 
            try:
                jj, mm, aaaa = birthdate.split('/')
                datetime.datetime(int(aaaa), int(mm), int(jj))
            except ValueError:
                print("Cette date n'est pas valide, Merci de recommencer.")
            else:
                # tester son age mini serait un plus
                break
        while True:
            gender = input("si indispensable Merci de préciser son genre (sans, M, F, tous): ")
            if gender in constants.GENDER:
                break
        while True:
            try:
                initial_ranking = int(input("son classement ELO : "))
            except ValueError:
                print("Merci de saisir un entier positif.")
            else:
                if initial_ranking > 0:
                    break

        return name, firstname, birthdate, gender, initial_ranking
