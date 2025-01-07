from copy import deepcopy
from typing import Tuple, List, Optional, Dict

import numpy as np

from car import Car

Coordinates = Tuple[int, int]


def _is_capital_letter(name: str) -> bool:
    if len(name) == 1 and name.upper() == name:
        return True
    return False


class Board:
    """
    Add a class description here.
    Write briefly about the purpose of the class.
    """

    def __init__(self, size: Coordinates = (7, 7), target_location: Coordinates = (3, 7)) -> None:
        """
        Initialize the class.
        :param target_location:
        """
        self.size = size
        self.target = target_location
        self.cars: Dict[str, Car] = {}

    def __str__(self) -> str:
        """
        This function is called when a board object is to be printed.
        :return: A string representing the current status of the board.
        """
        board_matrix = np.full(self.size, 'ם')
        board_matrix = np.pad(board_matrix, 1, mode='constant', constant_values='')
        for car in self.cars.values():
            for coordinate in car.car_coordinates():
                board_matrix[coordinate[0] + 1][coordinate[1] + 1] = car.name
        board_matrix[self.target[0] + 1][self.target[1] + 1] = "X"
        return '\n'.join(' '.join(map(str, row)) for row in board_matrix)

    def cell_list(self) -> List[Coordinates]:
        """
        This function returns the coordinates of cells in this board.
        :return: list of coordinates.
        """
        return [(row, col) for row in range(self.size[0]) for col in range(self.size[1])] + [self.target]

    def possible_moves(self) -> List[Tuple[str, str, str]]:
        """ 
        This function returns the legal moves of all cars in this board.
        :return: list of tuples in the form (name, move_key, description)
                 representing legal moves. The description should briefly
                 explain what is the movement represented by move_key.
        """
        return [(car_name, key, val) for car_name, car in self.cars.items()
                for key, val in car.possible_moves().items()]

    def target_location(self) -> Coordinates:
        """
        This function returns the coordinates of the location that should be filled for victory.
        :return: (row, col) of the goal location.
        """
        return self.target

    def cell_content(self, coordinates: Coordinates) -> Optional[str]:
        """
        Checks if the given coordinates are empty.
        :param coordinates: tuple of (row, col) of the coordinates to check.
        :return: The name of the car in "coordinates", None if it's empty.
        """
        for car in self.cars.values():
            for car_cords in car.car_coordinates():
                if car_cords[0] == coordinates[0] and car_cords[1] == coordinates[1]:
                    return car.name

    def _coordinates_in_board(self, car: Car) -> bool:
        for cords in car.car_coordinates():
            if not (0 <= cords[0] < self.size[0] and 0 <= cords[1] < self.size[1]):
                if cords != self.target:
                    return False
        return True

    def _in_car(self, car: Car) -> bool:
        for cords in car.car_coordinates():
            cell_content = self.cell_content(cords)
            if cell_content is not None and cell_content != car.name:
                return True
        return False

    def _is_valid_car(self, car: Car) -> bool:
        if (
                (not self._coordinates_in_board(car))
                or self._in_car(car)
                or (not _is_capital_letter(car.name))
        ):
            return False
        return True

    def add_car(self, car: Car) -> bool:
        """
        Adds a car to the game.
        :param car: car object to add.
        :return: True upon success, False if failed.
        """
        if not self._is_valid_car(car) or car.name in self.cars.keys():
            return False
        self.cars[car.name] = car
        return True

    def move_car(self, name: str, move_key: str) -> bool:
        """
        Moves car one step in a given direction.
        :param name: name of the car to move.
        :param move_key: the key of the required move.
        :return: True upon success, False otherwise.
        """
        copy_of_car = deepcopy(self.cars[name])
        copy_of_car.move(move_key)
        if self._is_valid_car(copy_of_car):
            self.cars[name].move(move_key)
            return True
        return False


if __name__ == '__main__':
    a = Board()
    print(a.cell_list())
