from app.storage.db import get_conn

def wallet_request_exists(key: str):
    conn = get_conn()
    try:
        return conn.execute(
            "SELECT response FROM wallet_requests WHERE idempotency_key = ?",
            (key,),
        ).fetchone()
    finally:
        conn.close()

def save_wallet_request(key: str, response: str):
    conn = get_conn()
    try:
        conn.execute(
            "INSERT INTO wallet_requests (idempotency_key, response) VALUES (?, ?)",
            (key, response),
        )
        conn.commit()
    finally:
        conn.close()
