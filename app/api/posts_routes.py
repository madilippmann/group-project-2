from flask import Blueprint, render_template, session, redirect, url_for, request
from app.forms import CreatePostForm, EditPostForm
from app.models import db, Post
from app.api.utils import validation_errors_to_error_messages


posts_routes = Blueprint('posts', __name__)


@posts_routes.route('/')
def get_posts():
  posts = Post.query.all()
  # ??? do posts need to be converted to json ???
  return posts

@posts_routes.route('/<int:postId>')
def get_post(postId):
  post = Post.query.get(postId)
  # ??? do posts need to be converted to json ???
  return post

@posts_routes.route('/', methods=["POST"])
def create_post():
    # get the post from request body
    # create instance of post passing in info
    # save to session and send the new post from db back
    form = CreatePostForm()

    # Get the csrf_token from the request cookie and put it into the
    # form manually to validate_on_submit can be used
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        userId = session['_user_id']
        data = {
            "userId": session['user_id'],
            "postImageURL": form["postImageURL"].data,
            "caption": form["caption"].data
        }

        post = Post(**data)
        db.session.add(post)
        db.session.commit()
        return post

    return {'errors': validation_errors_to_error_messages(form.errors)}, 401


@posts_routes.route('/<int:postId>', methods=["PUT"])
def edit_post(postId):
  # get post from req body
  # query db for the existing post
  # set all properties equal to request's post
  # save to session
  # send back new post

    post = request.get_json()
    form = EditPostForm()

    # Get the csrf_token from the request cookie and put it into the
    # form manually to validate_on_submit can be used
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        userId = session['_user_id']

        post = Post.query.get(postId)
        post.caption = form['caption'].data
        db.session.commit()
        return post

    return {'errors': validation_errors_to_error_messages(form.errors)}, 401




@posts_routes.route('/<int:postId>', methods=["DELETE"])
def delete_post(postId):
  post = Post.query.get(postId)
  userId = request.get_json(force=True)["sessionUserId"]

  if post.userId == userId:
    db.session.delete(post)
    return postId
  else:
    return
