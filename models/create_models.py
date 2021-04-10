from models import User


def run_models():
    User.database.Base.metadata.create_all(User.database.engine)
