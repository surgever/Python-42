#!/usr/bin/python3

from typing import Any, Protocol
from abc import ABC, abstractmethod


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class CsvExport:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("CSV Output:")
        values: list[str] = [item[1] for item in data]
        csv_string: str = ",".join(values)
        print(csv_string)


class JsonExport:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("JSON Output:")
        json_parts: list[str] = []
        for rank, value in data:
            json_parts.append(f'"item_{rank}": "{value}"')
        json_string: str = "{" + ", ".join(json_parts) + "}"
        print(json_string)


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
            raise Exception("No data left to output")
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
            raise Exception("Improper numeric data")

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
            raise Exception("Improper text data")
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
            raise Exception("Improper log data")
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
                print("DataStream error: Can't "
                      f"process element in stream: {item}")

    def print_processors_stats(self) -> None:
        if len(self.registered_processors) == 0:
            print("No processor found, no data")
        else:
            for proc in self.registered_processors:
                proc_name: str = type(proc).__name__.replace("Processor",
                                                             " Processor")
                total_processed: int = proc._rank_counter
                remaining: int = len(proc._data)

                print(f"{proc_name}: total {total_processed} items processed, "
                      f"remaining {remaining} on processor")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self.registered_processors:
            data_to_export: list[tuple[int, str]] = []

            for _ in range(nb):
                if len(proc._data) > 0:
                    data_to_export.append(proc.output())
                else:
                    break
            if data_to_export:
                plugin.process_output(data_to_export)


def main() -> None:

    print("\nInitialize Data Stream...")
    stream = DataStream()

    print("\n== DataStream statistics ==")
    stream.print_processors_stats()

    print("\nRegistering Processors")
    n_processor = NumericProcessor()
    t_processor = TextProcessor()
    l_processor = LogProcessor()
    csv_plugin = CsvExport()
    json_plugin = JsonExport()
    stream.register_processor(n_processor)
    stream.register_processor(t_processor)
    stream.register_processor(l_processor)

    data = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message":
                "Telnet access! Use ssh instead"
            },
            {
                "log_level": "INFO",
                "log_message":
                "User wil is connected"
            }
        ],
        42,
        ["Hi", "five"]
    ]
    print("\nSend first batch of data on stream:", data)
    stream.process_stream(data)
    print("\n== DataStream statistics ==")
    stream.print_processors_stats()
    print(
        "\nSend 3 processed data "
        "from each processor to a CSV plugin:"
    )
    stream.output_pipeline(3, csv_plugin)
    print("\n== DataStream statistics ==")
    stream.print_processors_stats()

    second_batch = [
        21,
        [
            "I love AI",
            "LLMs are wonderful",
            "Stay healthy"
        ],
        [
            {
                "log_level": "ERROR",
                "log_message":
                "500 server crash"
            },
            {
                "log_level": "NOTICE",
                "log_message":
                "Certificate expires in 10 days"
            }
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello"
    ]
    print("\nSend another batch of data:", second_batch)
    stream.process_stream(second_batch)
    print("\n== DataStream statistics ==")
    stream.print_processors_stats()
    print(
        "\nSend 5 processed data "
        "from each processor to a JSON plugin:"
    )
    stream.output_pipeline(5, json_plugin)
    print("\n== DataStream statistics ==")
    stream.print_processors_stats()


if __name__ == "__main__":
    print("=== Code Nexus - Data Pipeline ===")
    main()
