import os

from dino.game import Game

if __name__ == '__main__':
    app = Game()

    # Normal game start
    # app.game_loop()

    # NEAT start
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config=feedforward')
    app.run_neat(config_path)
