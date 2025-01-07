from board import Board


class Game:
    """
    Add a class description here.
    Write briefly about the purpose of the class.
    """

    def __init__(self, board: Board) -> None:
        """
        Initialize a new Game object.
        :param board: An object of type board
        """
        self.board = board

    def __single_turn(self) -> bool:
        """
        Note - this function is here to guide you, and it is *not mandatory* to implement it.

        The function runs one round of the game:
            1. Get user's input of: what color car to move, and what direction to move it.
            2. Check if the input is valid.
            3. Try moving the car according to user's input.
        """
        finished_turn = False
        while not finished_turn:
            print(self.board)
            print('\n'.join(' '.join(car) for car in self.board.possible_moves()))
            print('\n')
            user_input = input(f"Choose a car and a direction\n")
            if user_input == '!':
                return False
            if len(user_input) != 3 and user_input[1] != ',':
                print('Invalid input. Please try again.\n')
                continue
            car = user_input.split(',')[0]
            move_key = user_input.split(',')[1]
            if not self.board.move_car(car, move_key):
                print(f"Invalid move. Try again.\n")
                continue
            finished_turn = True
        return True

    def _is_game_over(self) -> bool:
        for car in self.board.cars.values():
            for cords in car.car_coordinates():
                if cords[0] == self.board.target[0] and cords[1] == self.board.target[1]:
                    return True
        return False

    def play(self) -> None:
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """
        another_turn = True
        while (not self._is_game_over()) and another_turn:
            another_turn = self.__single_turn()
        if not another_turn:
            print("GAME OVER!")
        else:
            print("YOU WIN!")
