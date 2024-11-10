def is_vormir_safe(floor_temp: float,
                   day_1_temp: float,
                   day_2_temp: float,
                   day_3_temp: float):
    days_above_floor_temp = [day_temp for day_temp in [day_1_temp, day_2_temp, day_3_temp] if day_temp > floor_temp]
    if len(days_above_floor_temp) >= 2:
        return True
    else:
        return False
