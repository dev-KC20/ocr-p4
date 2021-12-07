from utils.menu import Menu
from views.menuview import MenuView

class AppController:
    def __init__(self):
        self.controller = None

    def start(self):
        self.controller = MenuController().run()
        while self.controller:
            self.controller = self.controller.run()


class MenuController:

    def run(self):
        """
            """
        self.menu = Menu()
        self.menu.add_menu("10", "Gérer les joueurs", MenuPlayerController())
        self.menu.add_menu("20", "Organiser un tournoi", MenuTournamentController())
        self.menu.add_menu("40", "Afficher les rapports", MenuReportsController())
        self.menu.add_menu("50", "Charger/Sauver les données", MenuDBController())
        self.menu.add_menu("90", "Quitter l'application", MenuExitController())
        chosen_option = MenuView(self.menu).get_user_input()
        next_menu = self.menu.get_action(chosen_option)
        return next_menu

class MenuPlayerController:

    def run(self):
        """
            """
        self.menu = Menu()
        self.menu.add_menu("10", "Afficher la liste des joueurs", MenuPlayerController())
        self.menu.add_menu("20", "Créer un joueur", MenuTournamentController())
        self.menu.add_menu("80", "Retour à l'accueil", MenuController())
        self.menu.add_menu("90", "Quitter l'application", MenuExitController())
        chosen_option = MenuView(self.menu).get_user_input()
        next_menu = self.menu.get_action(chosen_option)
        return next_menu


class MenuTournamentController:

    def run(self):
        """
            """
        self.menu = Menu()
        self.menu.add_menu("10", "Créer un tournoi", MenuPlayerController())
        self.menu.add_menu("20", "Mettre à jour les résultats", MenuTournamentController())
        self.menu.add_menu("80", "Retour à l'accueil", MenuController())
        self.menu.add_menu("90", "Quitter l'application", MenuExitController())
        chosen_option = MenuView(self.menu).get_user_input()
        next_menu = self.menu.get_action(chosen_option)
        return next_menu


class MenuReportsController:

    def run(self):
        """
            """
        self.menu = Menu()
        self.menu.add_menu("10", "Liste de tous les joueurs", MenuPlayerController())
        self.menu.add_menu("20", "Liste des joueurs d'un tournoi", MenuTournamentController())
        self.menu.add_menu("30", "Liste des tournois", MenuReportsController())
        self.menu.add_menu("40", "Liste des tours d'un tournoi", MenuDBController())
        self.menu.add_menu("50", "Liste des matchs d'un tournoi", MenuDBController())
        self.menu.add_menu("80", "Retour à l'accueil", MenuController())
        self.menu.add_menu("90", "Quitter l'application", MenuExitController())
        chosen_option = MenuView(self.menu).get_user_input()
        next_menu = self.menu.get_action(chosen_option)
        return next_menu

 
class MenuDBController:

    def run(self):
        """
            """
        self.menu = Menu()
        self.menu.add_menu("10", "Charger les joueurs", MenuPlayerController())
        self.menu.add_menu("20", "Charger les tournois", MenuTournamentController())
        self.menu.add_menu("11", "Sauver les joueurs", MenuPlayerController())
        self.menu.add_menu("21", "Sauver les tournois", MenuTournamentController())
        self.menu.add_menu("80", "Retour à l'accueil", MenuController())
        self.menu.add_menu("90", "Quitter l'application", MenuExitController())
        chosen_option = MenuView(self.menu).get_user_input()
        next_menu = self.menu.get_action(chosen_option)
        return next_menu

class MenuExitController:

    def run(self):
        """
            """
        self.menu = Menu()            
        return MenuView(self.menu).good_bye()

