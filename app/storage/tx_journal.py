from sqlalchemy import text
from app.db.session import get_engine

def ensure_tx_tables():
    engine = get_engine()

    with engine.begin() as conn:
        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS wallet_tx_journal (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tx_id TEXT NOT NULL,
            state TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """))
