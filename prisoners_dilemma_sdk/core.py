import json


class GameState:
    def __init__(self, game_state_json):
        decoded_json = json.loads(game_state_json)
        self.round = decoded_json['round']
        self.player1_history = decoded_json['player1_history']
        self.player2_history = decoded_json['player2_history']
