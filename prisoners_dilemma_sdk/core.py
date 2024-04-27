"""
Core classes and functions for the Prisoner's Dilemma game.
"""

from abc import ABC, abstractmethod
from typing import List


class GameState:
    """
    Represents the state of the game.
    """

    round_number: int
    """The current round number."""

    my_history: List[bool]
    """The history of my decisions."""

    opponent_history: List[bool]
    """The history of the opponent's decisions."""

    def __init__(
        self,
        round_number: int,
        my_history: List[bool],
        opponent_history: List[bool],
    ):
        """
        Initialize the game state.

        :param round_number: The current round number.
        :param my_history: The history of my decisions.
        :param opponent_history: The history of the opponent's decisions.
        """
        self.round_number = round_number
        self.my_history = my_history
        self.opponent_history = opponent_history


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
