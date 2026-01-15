# RootLender Wallet Service

The **RootLender Wallet Service** is a core internal microservice responsible for managing user wallets, balances, and ledger-safe transactions across the RootLender ecosystem.

## Responsibilities
- Wallet creation and lifecycle
- Balance tracking
- Credit and debit transactions
- Idempotent transaction handling
- Internal service-to-service wallet operations

## Tech Stack
- Python 3.11+
- FastAPI
- SQLAlchemy
- PostgreSQL

## Local Development

### Create virtual environment
```bash
python -m venv venv
