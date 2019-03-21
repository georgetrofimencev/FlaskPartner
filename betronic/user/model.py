import uuid
from datetime import datetime
from betronic.base.model import BaseModel
from werkzeug.security import generate_password_hash, check_password_hash

from betronic import db


class UserModel(BaseModel):
    OWNER = '10'
    ADMIN = '5'
    PARTNER = '1'

    ROLES = {
        OWNER: "Владелец",
        ADMIN: "Администратор",
        PARTNER: "Партнер",
    }

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    login = db.Column(db.String(80), unique=True, nullable=False, index=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    phone = db.Column(db.String(100), nullable=False, unique=True)
    skype = db.Column(db.String(120))

    name = db.Column(db.String(128))
    surname = db.Column(db.String(128))

    is_active = db.Column(db.Boolean, default=False)

    password_hash = db.Column(db.String(128))

    verification_uuid = db.Column(db.String(length=36),
                                  default=uuid.uuid4, unique=True)

    last_seen = db.Column(db.DateTime(), default=datetime.utcnow)

    role = db.Column(db.String(3), default=PARTNER)

    country = db.Column(db.String(120))
    language = db.Column(db.String(10))
    currency = db.Column(db.String(5))
    note = db.Column(db.String(500))

    def __init__(self, **kwargs):
        super(UserModel, self).__init__(**kwargs)

    def __repr__(self):
        return '<User email with: %s>' % self.email

    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute')

    @property
    def is_verified(self):
        return True if not self.verification_uuid else False

    @property
    def full_name(self):
        if self.name and self.surname:
            return f"{self.name} {self.surname}"
        elif self.name and not self.surname:
            return f"{self.name}"
        elif not self.name and self.surname:
            return f"{self.surname}"
        else:
            return ""

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    @classmethod
    def get_by_email(cls, db, email):
        return db.session.query(cls)\
            .filter(cls.email == email).first()

    @classmethod
    def get_by_login(cls, db, login):
        return db.session.query(cls)\
            .filter(cls.login == login).first()
