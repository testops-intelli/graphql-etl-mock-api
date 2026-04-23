from pathlib import Path
import shutil

def main():
    root = Path(__file__).resolve().parent
    env_example = root / ".env.example"
    env_file = root / ".env"

    if not env_example.exists():
        print("ERROR: .env.example not found")
        return

    if env_file.exists():
        print(".env already exists. No changes made.")
        return

    shutil.copy(env_example, env_file)
    print("Created .env from .env.example")
    print("Please open .env and fill in your real PostgreSQL credentials.")


if __name__ == "__main__":
    main()
