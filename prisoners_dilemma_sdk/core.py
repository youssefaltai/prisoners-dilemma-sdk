"""
Core classes and functions for the Prisoner's Dilemma game.
"""

from abc import ABC, abstractmethod
from typing import List


class GameState:
    """
    Represents the state of the game.
    """

    def __init__(
        self,
        round_number: int,
        player1_history: List[bool],
        player2_history: List[bool]
    ):
        """
        Initialize the game state.

        :param round_number: The current round number.
        :param player1_history: History of decisions made by player 1.
        :param player2_history: History of decisions made by player 2.
        """
        self.round_number = round_number
        self.player1_history = player1_history
        self.player2_history = player2_history


class PrisonersDilemmaStrategy(ABC):
    """
    Abstract base class for strategies in the Prisoner's Dilemma game.
    """

    @abstractmethod
    def cooperate(self, game_state: GameState) -> bool:
        """
        Decide whether to cooperate or defect in the next round.

        :param game_state: The current game state.
        :return: True to cooperate, False to defect.
        """
        pass
