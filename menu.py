class Menu:

    def __init__(self, pp_settings, screen):
        self.pp_settings = pp_settings
        self.screen = screen

        self.title = "PACMAN PORTAL"

    def start_sequence(self):
        print("""
            TODO:\n
            - show name of game\n
            - show animation of ghosts chasing Pacman\n
            - Pacman chasing the ghosts and eating them\n
            - ghosts being individually introduced\n
        """)

    def main_menu(self):
        print(self.title)
        print("""
            TODO:\n
            - menu for Start game and High scores\n
            - High scores stored on disk and displayed when high scores menu is selected or after each game\n
            - Menu is animated when mouse hovers over it\n
        """)

    def high_scores(self):
        print("HIGH SCORES")
