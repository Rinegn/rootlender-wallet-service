from app.db import get_db

def wallet_request_exists(key: str):
    db = next(get_db())
    try:
        return db.execute(
            "SELECT response FROM wallet_requests WHERE idempotency_key = ?",
            (key,),
        ).fetchone()
    finally:
        db.close()


def save_wallet_request(key: str, response: str):
    db = next(get_db())
    try:
        db.execute(
            "INSERT INTO wallet_requests (idempotency_key, response) VALUES (?, ?)",
            (key, response),
        )
        db.commit()
    finally:
        db.close()
