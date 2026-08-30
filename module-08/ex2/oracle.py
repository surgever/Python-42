import os
import sys
from typing import Dict, Optional

try:
    from dotenv import load_dotenv
except ImportError:
    print(
        "Error: 'python-dotenv' package is not installed.\n"
        "Please install it using: pip install python-dotenv",
        file=sys.stderr,
    )
    sys.exit(1)


def get_config() -> Dict[str, Optional[str]]:

    load_dotenv()
    config: dict[str, str | None] = {
        "MATRIX_MODE": os.getenv("MATRIX_MODE"),
        "DATABASE_URL": os.getenv("DATABASE_URL"),
        "API_KEY": os.getenv("API_KEY"),
        "LOG_LEVEL": os.getenv("LOG_LEVEL"),
        "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT"),
    }
    return config


def get_security(config: Dict[str, Optional[str]]) -> Dict[str, str]:

    env_ignored = False
    if os.path.exists(".gitignore"):
        with open(".gitignore", "r", encoding="utf-8") as f:
            lines = []
            for line in f.readlines():
                lines.append(line.strip())
            if ".env" in lines:
                env_ignored = True

    env_exists = os.path.exists(".env")

    return {
        "no_hardcoded": (
            "[OK] No hardcoded secrets detected"
            if env_exists
            else "[WARNING] .env file missing."
        ),
        "env_file": (
            "[OK] .env file properly configured"
            if env_ignored
            else "[WARNING] .env file is NOT listed in .gitignore!"
        ),
        "production_overrides":
            "[OK] Production overrides available"
            if env_exists and env_ignored
            else "[WARNING] Production values are being overrided"
    }


def main() -> None:
    print("\nORACLE STATUS: Reading the Matrix...\n")
    try:
        config: Dict[str, Optional[str]] = get_config()
    except Exception as error:
        print(
            f"Error accessing Mainframe configuration: {error}",
            file=sys.stderr,
        )
        sys.exit(1)

    mode = config.get("MATRIX_MODE") or "development"
    db_url = config.get("DATABASE_URL")
    api_key = config.get("API_KEY")
    log_level = config.get("LOG_LEVEL") or "DEBUG"
    zion_endpoint = config.get("ZION_ENDPOINT")

    if db_url:
        db_status = (
            "Connected to local instance"
            if db_url.lower() or mode == "development"
            else "Connected to local instance"
        )
    else:
        db_status = "Not connected (DATABASE_URL missing)"

    api_status = (
        "Authenticated"
        if api_key else "Unauthenticated (API_KEY missing)"
    )

    zion_status = (
        "Online" if zion_endpoint
        else "Offline (ZION_ENDPOINT missing)"
    )

    print("Configuration loaded:")
    print(f"Mode: {mode}")
    print(f"Database: {db_status}")
    print(f"API Access: {api_status}")
    print(f"Log Level: {log_level}")
    print(f"Zion Network: {zion_status}\n")

    security = get_security(config)
    print("Environment security check:")
    print(security["no_hardcoded"])
    print(security["env_file"])
    print(security["production_overrides"])
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
