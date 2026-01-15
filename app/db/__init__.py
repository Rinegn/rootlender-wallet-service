from app.db.session import SessionLocal, get_engine


def get_db():
    engine = get_engine()
    SessionLocal.configure(bind=engine)

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
