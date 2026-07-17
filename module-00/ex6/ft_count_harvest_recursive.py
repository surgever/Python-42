def ft_count_harvest_recursive_day(current_day: int, harvest_day: int) -> None:
    if current_day > harvest_day:
        print("Harvest time!")
    else:
        print("Day", current_day)
        ft_count_harvest_recursive_day(current_day + 1, harvest_day)


def ft_count_harvest_recursive() -> None:
    start_day = 1
    harvest_day = int(input("Days until harvest: "))
    ft_count_harvest_recursive_day(start_day, harvest_day)
