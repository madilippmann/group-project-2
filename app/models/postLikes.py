from .db import db

class PostLike(db.Model):
    __tablename__ = 'postLikes'

    id = db.Column(db.Integer, primary_key=True)
    postId = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)
    userId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    post = db.relationship('Post', back_populates='postLikes')
    user = db.relationship('User', back_populates='postLikes')
