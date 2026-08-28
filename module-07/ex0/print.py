
from .secure_archive import secure_archive
from ex0 import Creature


class Pallete:
    yl = "\x1b[48;2;255;195;50m"
    blF = "\x1b[38;2;30;30;30m"  # black fg
    reset = "\x1b[0m"  # reset


p = Pallete()


def PokeInfo(
        description: str, left: bool = True, health: int = 100) -> list[str]:
    return [
        f"  {p.blF}▐{p.yl}{'▀'*22}{p.reset}{p.blF}▌  ",
        f"  {p.blF}▐{p.yl} " + description + f" {p.reset}{p.blF}▌  ",
        f"  {p.blF}▐{p.yl}{('▀'*16):>21} {p.reset}{p.blF}▌  ",
        f"  {p.blF} {'▀'*22}{p.reset}   "
    ]


def print_msgbox(msg: str = "", opt: list[str] = []) -> None:
    limit = 33
    msg_words = msg.split()
    msg1 = ""
    msg2 = ""
    for w in msg_words:
        if len(msg1) + 1 + len(w) <= limit:
            msg1 += " " + w
        else:
            msg1 = f"{msg1:<33}"
            msg2 += " " + w
    opt = (opt + [""] * 4)[:4]
    # 56 - 2 >> 54 = 30 + 24 >> | 1 msg 1 | 9 1 9 |
    print(f"{p.blF}▐{p.yl}{'▀'*34}▛{'▀'*19}▜{p.reset}")
    print(f"{p.blF}▐{p.yl}{msg1:<33} ▌{opt[0]:<9} {opt[1]:<9}▐{p.reset}")
    print(f"{p.blF}▐{p.yl}{msg2:<33} ▌{opt[2]:<9} {opt[3]:<9}▐{p.reset}")
    print(f"{p.blF}▐{p.yl}{'▄'*34}▙{'▄'*19}▟{p.reset}")


def print_screen(
        pok1: Creature | None, pok2: Creature | None,
        msg: str, opt: list[str] = [],
        fg: str = "f1", noinput: bool = False) -> None:
    
    print("\033[H\033[J", end="")
    if pok1:
        try:
            sprite_file_1 = secure_archive(pok1.render(fg))
            if pok2:
                sprite_file_2 = secure_archive(pok2.render("b"))
        except Exception as e:
            print("Error reading sprites.", e)
            return
        sprite_1 = sprite_file_1[1].splitlines()
        if pok2:
            sprite_2 = sprite_file_2[1].splitlines()
        else:
            print(" \n" * 4, end="")

        pki1 = PokeInfo(pok1.info())
        print(pki1[0] + sprite_1[0])
        print(pki1[1] + sprite_1[1])
        print(pki1[2] + sprite_1[2])
        print(pki1[3] + sprite_1[3])

        if pok2:
            for i in range(6):
                print(sprite_2[0 + i] + sprite_1[4 + i])
            pki2 = PokeInfo(pok2.info())
            print(sprite_2[6] + pki2[0])
            print(sprite_2[7] + pki2[1])
            print(sprite_2[8] + pki2[2])
            print(sprite_2[9] + pki2[3])
        else:
            for i in range(6):
                print(" "*28 + sprite_1[4 + i])
    else:
        print("\n" * 14, end="")

    print_msgbox(msg, opt)
    if not noinput:
        input()
