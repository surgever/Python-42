#!/usr/bin/python3w

from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._data: list = []
        self._rank_counter: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if len(self._data) == 0:
            raise IndexError("No data left to output")
        return self._data.pop(0)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return (
            isinstance(data, (int, float))
            or (
                isinstance(data, list)
                and all(isinstance(i, (int, float)) for i in data)
            )
        )

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")

        if isinstance(data, (int, float)):
            data_str: str = str(data)
            self._data.append((self._rank_counter, data_str))
            self._rank_counter += 1
        elif isinstance(data, list):
            for item in data:
                item_str: str = str(item)
                self._data.append((self._rank_counter, item_str))
                self._rank_counter += 1


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return (
            isinstance(data, str)
            or (
                isinstance(data, list)
                and all(isinstance(i, str) for i in data)
            )
        )

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        if isinstance(data, str):
            self._data.append((self._rank_counter, data))
            self._rank_counter += 1
        elif isinstance(data, list):
            for item in data:
                self._data.append((self._rank_counter, item))
                self._rank_counter += 1


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return (
            (
                isinstance(data, dict)
                and all(
                    isinstance(key, str) and isinstance(value, str)
                    for key, value in data.items()
                )
            )
            or (
                isinstance(data, list)
                and all(
                    isinstance(i, dict)
                    and all(
                        isinstance(key, str) and isinstance(value, str)
                        for key, value in i.items()
                    )
                    for i in data
                )
            )
        )

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")

        if isinstance(data, dict):
            log_str: str = f"{data['log_level']}: {data['log_message']}"

            self._data.append((self._rank_counter, log_str))
            self._rank_counter += 1

        elif isinstance(data, list):
            for item in data:

                log_str = f"{item['log_level']}: {item['log_message']}"
                self._data.append((self._rank_counter, log_str))
                self._rank_counter += 1


class DataStream:
    def __init__(self) -> None:
        self.registered_processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.registered_processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for item in stream:
            processed: bool = False
            for proc in self.registered_processors:
                if proc.validate(item):
                    proc.ingest(item)
                    processed = True
                    break
            if not processed:
                print("DataStream error: "
                      f"Can't process element in stream: {item}")

    def print_processors_stats(self) -> None:
        if len(self.registered_processors) == 0:
            print("No processor found, no data\n")
        else:
            for proc in self.registered_processors:
                proc_name: str = type(proc).__name__.replace("Processor",
                                                             " Processor")
                total_processed: int = proc._rank_counter
                remaining: int = len(proc._data)
                print(f"{proc_name}: total {total_processed} items processed,"
                      f" remaining {remaining} on processor")


def main() -> None:
    print("Initialize Data Stream...")
    stream = DataStream()
    print("== DataStream statistics ==")
    stream.print_processors_stats()

    print("Registering Numeric Processor\n")
    n_processor = NumericProcessor()
    stream.register_processor(n_processor)
    batch_1: list = [
        'Hello world',
        [3.14, 1, 2.71],
        [{'log_level': 'WARNING', 'log_message':
          'Telnet access! Use ssh instead'},
         {'log_level': 'INFO', 'log_message': 'User wil is connected'}],
        42,
        ['Hi', 'five']
    ]
    print(f"Send first batch of data on stream: {batch_1}")
    stream.process_stream(batch_1)
    print("== DataStream statistics ==")
    stream.print_processors_stats()

    print("\nRegistering other data processors...")
    t_processor = TextProcessor()
    l_processor = LogProcessor()
    stream.register_processor(t_processor)
    stream.register_processor(l_processor)
    print("Send the same batch again...")
    stream.process_stream(batch_1)
    print("== DataStream statistics ==")
    stream.print_processors_stats()
    print("\nConsume some elements from the data processors:"
          " Numeric 3, Text 2, Log 1")
    for _ in range(3):
        n_processor.output()
    for _ in range(2):
        t_processor.output()
    for _ in range(1):
        l_processor.output()
    print("== DataStream statistics ==")
    stream.print_processors_stats()


if __name__ == "__main__":
    print("=== Code Nexus Data Stream ===\n")
    main()
