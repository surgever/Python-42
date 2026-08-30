from sys import base_prefix, prefix, executable
from os import path
from site import getsitepackages


def virtual_environment_info() -> None:

    if base_prefix != prefix:

        print("\033[0;31m\nMATRIX STATUS: Welcome to the construct\n")

        print(f"\nCurrent Python: {executable}")
        print(f"Virtual Environment: {path.basename(prefix)}")
        print(f"Environment Path: {prefix}")
        print()
        print("\033[0;0mSUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")
        print()
        print("Package installation path:")
        print(getsitepackages()[0] + "\033[0m")

    else:
        print("\033[0;34m\nMATRIX STATUS: You're still plugged in\n")

        print(f"Current Python: {executable}")
        print("Virtual Environment: None detected\n")

        print("\033[0mTo enter the construct, run:")
        print("python3 -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate # On Windows")
        print()
        print("Then run this program again.")


if __name__ == "__main__":
    virtual_environment_info()
