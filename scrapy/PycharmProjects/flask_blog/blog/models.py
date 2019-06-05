from blog import db
ROLE_USER = 0
ROLE_ADMIN = 1


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    neckname = db.Column(db.String(50), index=True, unique=True, nullable=False)
    email = db.Column(db.String(100), index=True, unique=True)
    role = db.Column(db.SmallInteger, default=ROLE_ADMIN)
    posts = db.relationship('Post', backref='user', lazy='dynamic')

    def __repr__(self):
        return '<User %s>' % self.neckname


class Post(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(30))
    body = db.Column(db.String(50))
    timestamp = db.Column(db.DateTime())
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    comments = db.relationship('Comment', backref='post', lazy='dynamic')

    def __repr__(self):
        return '<Post %s>' % self.title


class Comment(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    text = db.Column(db.Text())
    data = db.Column(db.DateTime())
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))

    def __repr__(self):
        return '<Comment %s>' % self.name