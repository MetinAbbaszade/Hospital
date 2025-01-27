def get_db():
    from app import engine
    from sqlalchemy.orm import sessionmaker
    sessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()