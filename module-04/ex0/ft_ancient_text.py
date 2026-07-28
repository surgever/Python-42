import sys


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
          + "=== Welcome to the Archaeological Museum basement ===" + c.ENDC)
    print(c.ITAL + "You now have access to our secret pieces." + c.ENDC)
    print(c.FAINT + f"...extracting piece known as '{filename}'..." + c.ENDC)

    try:
        fd = open(filename, "r")
        print(c.ORANGE + c.HEADER + "\n")
        text = fd.read()
        print(f"{text}")
        fd.close()
        print("\n" + c.HEADER + c.ENDC)
        print(c.FAINT + "...no more info remaining. Closing..." + c.ENDC)

    except Exception as error:
        print(f"Error when accessing piece '{filename}':\n" + c.ENDC
              + c.FAIL + f"{error}" + c.ENDC)


def main() -> None:
    if len(sys.argv) == 2:
        filename: str = sys.argv[1]
        access_epigraphy(filename)
    else:
        print("Usage: python3 ft_ancient_text.py <filename>")


if __name__ == "__main__":
    main()
