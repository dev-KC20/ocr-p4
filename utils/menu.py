class Menu:
    def __init__(self):

        self._options = {}

    def add_menu(self, number, description, action):
        self._options[number] = (description, action)

    def items(self):
        return self._options.items()

    def get_action(self, number):
        description, action = self._options[number]
        return action

    def __contains__(self, option):
        return str(option) in self._options
