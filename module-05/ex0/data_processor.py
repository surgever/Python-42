#!/usr/bin/python3

from typing import Any, Sequence
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._data: list[tuple[int, str]] = []
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

    def ingest(self, data: int | float | Sequence[int | float]) -> None:
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

    def ingest(self, data: str | list[str]) -> None:
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

    def ingest(
        self,
        data: dict[str, str] | list[dict[str, str]]
    ) -> None:
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


def nexusDataProcessor() -> None:
    print("\nTesting Numeric Processor...")
    n_processor = NumericProcessor()
    print(f"Trying to validate input '42': {n_processor.validate(42)}")
    print(f"Trying to validate input 'Hello': {n_processor.validate('Hello')}")
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        n_processor.ingest("foo")  # type: ignore[arg-type]
    except Exception as error:
        print(f"Got exception: {error}")
    numbers: list[int] = [1, 2, 3, 4, 5]
    print(f"Processing data: {numbers}")
    n_processor.ingest(numbers)
    print("Extracting 3 values...")
    for i in range(3):
        num_range, num_val = n_processor.output()
        print(f"Numeric value {num_range}: {num_val}")

    print("\nTesting Text Processor...")
    t_processor = TextProcessor()
    print(f"Trying to validate input '42': {t_processor.validate(42)}")
    texts: list[str] = ['Hello', 'Nexus', 'World']
    print(f"Processing data: {texts}")
    t_processor.ingest(texts)
    print("Extracting 1 value...")
    key, value = t_processor.output()
    print(f"Text value {key}: {value}")

    print("\nTesting Log Processor...")
    l_processor = LogProcessor()
    print(f"Trying to validate input 'Hello': {l_processor.validate('Hello')}")
    dicts: list[dict[str, str]] = [
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!!'}
    ]
    print(f"Processing data: {dicts}")
    l_processor.ingest(dicts)
    print("Extracting 2 values...")
    for i in range(2):
        key, value = l_processor.output()
        print(f"Log entry {key}: {value}")


if __name__ == "__main__":
    print("=== Code Nexus Data Processor ===")
    nexusDataProcessor()
