from ..models import db

batches_courses = db.Table('batches_courses',
    db.Column('batch_fk', db.Integer, db.ForeignKey('batches.id')),
    db.Column('course_fk', db.Integer, db.ForeignKey('courses.id'))
)