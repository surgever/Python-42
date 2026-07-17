def ft_count_harvest_iterative() -> None:
    start_day = 0
    harvest_day = int(input("Days until harvest: "))
    days = range(start_day, harvest_day)
    while start_day in days:
        start_day += 1
        print("Day", start_day)
    print("Harvest time!")
