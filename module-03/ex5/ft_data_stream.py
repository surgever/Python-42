#!/usr/bin/env python3

from typing import Generator
import random


def gen_event() -> Generator[tuple[str, str], None, None]:
    players = ["alice", "bob", "charlie", "dylan"]
    actions = [
        "run", "eat", "sleep", "grab", "move",
        "climb", "swim", "use", "release"
    ]
    while True:
        yield (random.choice(players), random.choice(actions))


def consume_event(
        events: list[tuple[str, str]]
        ) -> Generator[tuple[str, str], None, None]:
    while len(events) > 0:
        index = random.randrange(len(events))
        yield events.pop(index)


def ft_data_stream() -> None:
    generator = gen_event()
    for i in range(1000):
        player, action = next(generator)
        print(f"Event {i}: Player {player} did action {action}")
    ten_events: list[tuple[str, str]] = []
    for _ in range(10):
        ten_events.append(next(generator))
    print(f"Built list of 10 events: {ten_events}")
    for event in consume_event(ten_events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {ten_events}")


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    ft_data_stream()
