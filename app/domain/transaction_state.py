from enum import Enum

class TransactionState(str, Enum):
    INITIATED = "initiated"
    HOLD_PLACED = "hold_placed"
    ENTRY_POSTED = "entry_posted"
    COMPLETED = "completed"
    FAILED = "failed"
