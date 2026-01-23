from app.storage.db import get_conn

def tx_get(tx_id: str):
    conn = get_conn()
    try:
        return conn.execute(
            "SELECT * FROM wallet_transactions WHERE tx_id = ?",
            (tx_id,),
        ).fetchone()
    finally:
        conn.close()

def tx_create(tx_id: str, user_id: str, currency: str, amount: float, reference_id: str, status: str, correlation_id: str | None):
    conn = get_conn()
    try:
        conn.execute(
            """
            INSERT INTO wallet_transactions (tx_id, user_id, currency, amount, reference_id, status, correlation_id)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (tx_id, user_id, currency, amount, reference_id, status, correlation_id),
        )
        conn.commit()
    finally:
        conn.close()

def tx_update(tx_id: str, **fields):
    if not fields:
        return
    allowed = {
        "status", "hold_id", "ledger_entry_id", "correlation_id", "error"
    }
    updates = {k: v for k, v in fields.items() if k in allowed}
    if not updates:
        return

    set_clause = ", ".join([f"{k} = ?" for k in updates.keys()])
    values = list(updates.values()) + [tx_id]

    conn = get_conn()
    try:
        conn.execute(
            f"""
            UPDATE wallet_transactions
            SET {set_clause}, updated_at = CURRENT_TIMESTAMP
            WHERE tx_id = ?
            """,
            tuple(values),
        )
        conn.commit()
    finally:
        conn.close()
