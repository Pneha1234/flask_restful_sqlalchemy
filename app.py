import uuid
from datetime import datetime

from flask import Flask, request, g, jsonify
from flask_restful import Api, Resource, abort
from flask_sqlalchemy import SQLAlchemy

from validator_methods import set_attributes

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///moru_blog.db'
db = SQLAlchemy(app)


class BaseModel(db.Model, Base):
    __tablename__ = 'base_model'
    __abstract__ = True

    id = db.Column(db.String, primary_key=True)
    created_at = db.Column(db.DateTime)
    created_by = db.Column(db.String())
    updated_at = db.Column(db.DateTime)
    updated_by = db.Column(db.String())

    def __init__(self, **kwargs):
        super(BaseModel, self).__init__(**kwargs)
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        user = g.get('user', None)
        if user is not None:
            self.created_by = user.get('user_id', None)


class BlogModel(BaseModel):
    text = db.Column(db.String(100))
    views = db.Column(db.Integer)
    likes = db.Column(db.Integer)

    allowed_keys = {'text', 'views', 'likes'}

    def __init__(self, **kwargs):
        super().__init__()
        set_attributes(self, **kwargs)

    def blog_json(self):
        return {
            "id": self.id,
            "text": self.text,
            "views": self.views,
            "likes": self.likes
        }


class Blog(Resource):
    def get(self, blog_id):
        result = BlogModel.query.filter_by(id=blog_id).first()
        if not result:
            abort(404, message="Could not find blog with that id")
        return result.blog_json()

    def put(self, blog_id):
        data = request.get_json()
        blog = BlogModel.query.filter_by(id=blog_id).first()
        if blog is None:
            abort(404, message="Could not find blog with that id")

        blog.text = data.get('text', None)
        blog.views = data.get('views', None)
        blog.likes = data.get('likes', None)
        db.session.add(blog)
        db.session.commit()
        return blog.blog_json(), 201

    def delete(self, blog_id):
        result = BlogModel.query.filter_by(id=blog_id).first()
        if not result:
            abort(404, message="Blog doesn't exist, cannot delete")
        db.session.delete(result)
        db.session.commit()
        return '', 204


class Blogs(Resource):
    def post(self):
        data = request.get_json()
        blog = BlogModel(**data)
        db.session.add(blog)
        db.session.commit()
        return blog.blog_json()

    def get(self):
        blogs = BlogModel.query.all()
        return jsonify([blog.blog_json() for blog in blogs])


api.add_resource(Blog, '/blogs/<blog_id>')
api.add_resource(Blogs, '/blogs')

if __name__ == "__main__":
    app.run(debug=True)
