# from utils.menu import Menu

class MenuView:
    def __init__(self, menu):
        self.menu = menu

    def show_menu(self):
        print('*** MENU ***')
        print()
        for option, description in self.menu.items():
            print(f"{option} {description[0]}")
            print()

    def get_user_input(self):
        while True:
            self.show_menu()
            prompt_result = input("Votre choix: ")
            if prompt_result in self.menu:
                return prompt_result

    def good_bye(self):
        """
         """
        print()
        print("Merci d'avoir utilisé notre application")
        print("A bientôt, ocr")
        print()
        return None
