import sys
import typing


class c:
    ORANGE = '\033[33m'
    YELLOWBG = '\033[43m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    FAINT = '\033[2m'
    ITAL = '\033[3m'
    UNDERLINE = '\033[4m'
    HEADER = 'nunununununununununununununununun'


def access_epigraphy(filename: str) -> None:
    print(c.BOLD + c.UNDERLINE + c.YELLOWBG + c.ORANGE
          + "=== Archives Recovery & Preservation ===" + c.ENDC)
    print(c.ITAL + "You now have access to our secret pieces." + c.ENDC)
    print(c.FAINT + f"...extracting piece known as '{filename}'..." + c.ENDC)

    try:
        fd: typing.IO[str] = open(filename, "r")
        print(c.ORANGE + c.HEADER + "\n")
        text: list[str] = []
        for line in fd:
            print(line, end="")
            text += [line]
        fd.close()
        print("\n" + c.HEADER + c.ENDC)
        print(c.FAINT + "...no more info remaining. Closing..." + c.ENDC)
        print(c.FAINT + "...adding modification..." + c.ENDC)
        print(c.ORANGE + c.HEADER + "\n")
        text_new: str = ""
        for line in text:
            new_line: str = ""
            if line.endswith("\n"):
                new_line = line[:-1] + "#\n"
            else:
                new_line = line + "#\n"
            print(new_line, end="")
            text_new += new_line
        print("\n" + c.HEADER + c.ENDC)
        print("Provide name for copied piece: ")
        sys.stdout.flush()
        input: str = sys.stdin.readline()
        file2 = input.strip()
        if file2 == "":
            print(c.FAIL + "The copy was not saved." + c.ENDC)
        else:
            print(c.FAINT + f"...saving piece data to '{file2}'..." + c.ENDC)
            new_file: typing.IO[str] = open(file2, "w")
            new_file.write(text_new)
            new_file.close()
            print(f"Data saved in file '{file2}'.")
    except Exception as error:
        print(f"[STDERR] Access error to piece '{filename}':\n" + c.ENDC
              + c.FAIL + f"{error}" + c.ENDC, file=sys.stderr)


def main() -> None:
    if len(sys.argv) == 2:
        filename: str = sys.argv[1]
        access_epigraphy(filename)
    else:
        print("Usage: python3 ft_ancient_text.py <filename>")


if __name__ == "__main__":
    main()
