from ..models import db

users_skills = db.Table('users_skills',
    db.Column('user_fk', db.Integer, db.ForeignKey('users.id')),
    db.Column('skill_fk', db.Integer, db.ForeignKey('skills.id'))
)