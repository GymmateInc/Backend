import os


class EnvSettings:
    hostname: str = str(os.environ.get("HOSTNAME", "127.0.0.1")).strip()
    port: int = int(os.environ.get("PORT", 8080))

    database_url: str = str(os.environ.get("DATABASE_URL", "sqlite:///./gymmate.db"))


app_settings = EnvSettings()
