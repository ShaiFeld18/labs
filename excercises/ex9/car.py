from typing import Tuple, List, Dict

Coordinates = Tuple[int, int]


class Car:
    """
    Add a class description here.
    Write briefly about the purpose of the class.
    """

    def __init__(self, name: str, length: int, location: Coordinates, orientation: int) -> None:
        """
        A constructor for a Car object.
        :param name: A string representing the car's name.
        :param length: A positive int representing the car's length.
        :param location: A tuple representing the car's head location (row,col).
        :param orientation: One of either 0 (VERTICAL) or 1 (HORIZONTAL).
        """
        self.name = name
        self.length = length
        self.location = location
        self.orientation = orientation

    def car_coordinates(self) -> List[Coordinates]:
        """
        :return: A list of coordinates the car is in.
        """
        if self.orientation == 0:  # vertical
            return [(i, self.location[1]) for i in range(self.location[0], self.location[0] + self.length)]
        if self.orientation == 1:  # horizontal
            return [(self.location[0], i) for i in range(self.location[1], self.location[1] + self.length)]

    def possible_moves(self) -> Dict[str, str]:
        """
        :return: A dictionary of strings describing possible movements permitted by this car.
        """
        if self.orientation == 0:  # vertical
            return {"u": "cause the car to move up",
                    "d": "cause the car to move down"}
        if self.orientation == 1:  # horizontal
            return {"r": "cause the car to move right",
                    "l": "cause the car to move left"}

    def movement_requirements(self, move_key: str) -> List[Coordinates]:
        """ 
        :param move_key: A string representing the key of the required move.
        :return: A list of cell locations which must be empty in order for this move to be legal.
        """
        last_coordinate = self.car_coordinates()[self.length - 1]
        first_coordinate = self.location
        if self.orientation == 0:  # vertical
            if move_key == "u":
                return [(first_coordinate[0] - 1, first_coordinate[1])]
            elif move_key == "d":
                return [(last_coordinate[0] + 1, last_coordinate[1])]
        if self.orientation == 1:  # horizontal
            if move_key == "r":
                return [(last_coordinate[0], last_coordinate[1] + 1)]
            elif move_key == "l":
                return [(first_coordinate[0], first_coordinate[1] - 1)]

    def move(self, move_key: str) -> bool:
        """ 
        This function moves the car.
        :param move_key: A string representing the key of the required move.
        :return: True upon success, False otherwise
        """
        if move_key not in self.possible_moves().keys():
            return False
        if move_key == "u":
            self.location = (self.location[0] - 1, self.location[1])
        elif move_key == "d":
            self.location = (self.location[0] + 1, self.location[1])
        elif move_key == "r":
            self.location = (self.location[0], self.location[1] + 1)
        elif move_key == "l":
            self.location = (self.location[0], self.location[1] - 1)
        return True

    def get_name(self) -> str:
        """
        :return: The name of this car.
        """
        return self.name
