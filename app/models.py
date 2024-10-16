from app import db
from datetime import datetime

class User(db.Model):
    __tablename__ = "Users"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(200), nullable = False)
    password = db.Column(db.String(24), nullable = False)
    user = db.relationship("Task", back_populates="Users")
    created_at = db.Column(db.DateTime, default=datetime.now(datetime.timezone.utc))

    def __repr__(self):
        return f"<User {self.name}>"

class Task(db.Model):
    __tablename__ = "Tasks"
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    description = db.Column(db.String(200), nullable = False)
    is_done = db.Column(db.Boolean(200), default = False)
    user_id = db.Column(db.Integer(200), db.ForeignKey("Users.id"))
    user = db.relationship("User", back_populates = "Tasks")

def __repr__(self):
    return f"<User {self.title}>"
