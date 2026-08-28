
def secure_archive(
        filen: str, action: str = "r", content: str = "") -> tuple[bool, str]:
    try:
        with open(filen, action) as vault_file:
            if action == "r":
                read_content: str = vault_file.read()
                return (True, read_content)
            elif action == "w":
                vault_file.write(content)
                return (True, "Content successfully written to file")
    except Exception as error:
        return (False, f"{error}")
    return (False, "Invalid action")
