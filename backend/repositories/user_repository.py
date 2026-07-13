from models.user import User


class UserRepository:

    @staticmethod
    def create(
        db,
        full_name: str,
        email: str,
        password: str,
        role: str = "recruiter"
    ):

        user = User(
            full_name=full_name,
            email=email,
            password=password,
            role=role
        )

        db.add(user)
        db.commit()
        db.refresh(user)

        return user

    @staticmethod
    def get_by_email(
        db,
        email: str
    ):

        return (
            db.query(User)
            .filter(User.email == email)
            .first()
        )

    @staticmethod
    def get_by_id(
        db,
        user_id: int
    ):

        return (
            db.query(User)
            .filter(User.id == user_id)
            .first()
        )