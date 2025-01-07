import json
import sys
from typing import List, Union, Dict

from board import Board
from car import Car
from game import Game

JsonCoordinates = List[int]
CarConfiguration = List[Union[int, JsonCoordinates]]


def load_json(filename: str) -> Dict[str, CarConfiguration]:
    """
    This function opens a JSON file and loads its content.
    :param filename: path to the JSON file.
    :return: A dictionary containing the content of the JSON file.
    """
    with open(filename, 'r') as json_file:
        car_config: Dict[str, CarConfiguration] = json.load(json_file)
    # now car_config is a dictionary equivalent to the JSON file
    return car_config


if __name__ == "__main__":
    game = Game(Board())
    json_path = sys.argv[1]
    # json_path = "car_config.json"
    config = load_json(json_path)
    for car_name, car_data in config.items():
        game.board.add_car(Car(
            name=car_name,
            length=car_data[0],
            location=car_data[1],
            orientation=car_data[2],
        ))
    game.play()
