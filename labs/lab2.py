def print_area_of_rectangle():
    side1 = 2
    side2 = 1.5
    print("The area of a rectangle with sides of " + str(side1) + " km and " + str(side2) + " km is " + str(
        side1 * side2) + " km^2.")


def convert_spoon_to_cup(spoons_num):
    return spoons_num / 16


def mandrake_elixir(days_num, decibel_level):
    if days_num % 2 == 0 and decibel_level >= 200:
        return True
    return False


def calc_time_duration(broom_speed: float, is_monday: bool = False):
    distance = 500 if is_monday else 777
    return distance / broom_speed


def exp(base, power=2):
    return base ** power


def calc(num, val):
    if val == 'a':
        return exp(exp(num))
    elif val == 'b':
        res = exp(num, 3)
        if res <= 100:
            return res
    else:
        return 'Illegal value'


if __name__ == '__main__':
    print(not 'a' >= '5')

