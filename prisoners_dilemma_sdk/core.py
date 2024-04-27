import json
from abc import ABC, abstractmethod


class GameState:
    round_number: int
    player1_history: list[bool]
    player2_history: list[bool]

    def __init__(self, game_state_json: str):
        decoded_json = json.loads(game_state_json)
        self.round_number = decoded_json["round_number"]
        self.player1_history = decoded_json["player1_history"]
        self.player2_history = decoded_json["player2_history"]


class PrisonersDilemmaStrategy(ABC):
    @abstractmethod
    def cooperate(self, game_state: GameState) -> bool:
        """
        Decide whether to cooperate or defect in the next round.
        :param game_state: The current game state.
        :return: True to cooperate, False to defect.
        """
        pass
