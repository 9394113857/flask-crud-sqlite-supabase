import os

class Config:
    # =========================
    # Database
    # =========================
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "sqlite:///local.db"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # =========================
    # SQLAlchemy Engine Options
    # (IMPORTANT for Supabase Pooler / PgBouncer)
    # =========================
    SQLALCHEMY_ENGINE_OPTIONS = {
        "pool_pre_ping": True,   # Check connection before using
        "pool_recycle": 300,     # Recycle connections every 5 min
    }
