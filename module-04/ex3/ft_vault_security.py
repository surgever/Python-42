def secure_archive(filen: str, action: str = "r",
                   content: str = "") -> tuple[bool, str]:
    try:
        with open(filen, action) as vault_file:
            if action == "r":
                content: str = vault_file.read()
                return (True, content)
            elif action == "w":
                vault_file.write(content)
                return (True, "Content successfully written to file")
            else:
                return (False, "Function parameter error. Accepted: r or w.")
    except Exception as error:
        return (False, f"{error}")
    return (False, "Invalid action")


def main() -> None:
    print("\nUsing 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("this-file-does-not-exist.txt"))
    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("test.txt"))
    print("\nUsing 'secure_archive' to read from a regular file:")
    print(secure_archive("test2.txt"))
    print("\nUsing 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new_file.txt", "w", "text text text"))


if __name__ == "__main__":
    print("=== Cyber Archives Security ===")
    main()
