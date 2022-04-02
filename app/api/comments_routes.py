from flask import Blueprint, render_template, session, redirect, url_for, request, jsonify
from app.forms import CreatePostForm, EditPostForm
from app.models import db, Post
from app.api.utils import validation_errors_to_error_messages

comments_routes = Blueprint('posts', __name__)


# ROUTES #############################################################################
@comments_routes.route('/<int:postId>/comments/')
def get_comments(postId):
  pass
