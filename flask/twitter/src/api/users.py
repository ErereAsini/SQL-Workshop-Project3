# pylint: disable=E1101
# pylint: disable=E0402
from flask import Blueprint, jsonify, abort, request
from ..models import User, db, Tweet, likes_table
import hashlib
import secrets
import sqlalchemy

def scramble(password: str):
    """Hash and salt the given password"""
    salt = secrets.token_hex(16)
    return hashlib.sha512((password + salt).encode('utf-8')).hexdigest()

bp = Blueprint('users', __name__, url_prefix='/users')

@bp.route('', methods=['GET']) # decorator takes path and list of HTTP verbs
def index():
    users = User.query.all() # ORM performs SELECT query
    result = []
    for t in users:
        result.append(t.serialize()) # build list of Users as dictionaries
    return jsonify(result) # return JSON response

@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    t = User.query.get_or_404(id)
    return jsonify(t.serialize())

@bp.route('', methods=['POST'])
def create():
    username=request.json['username'],
    password=scramble(request.json['password'])
    # req body must contain username and password
    if 'user_id' not in request.json or 'content' not in request.json:
        return abort(400)
    if (len(username) < 3) or (len(password) < 8):
        return abort(400)
    # user with id of user_id must exist
    # construct User
    u = User(
        username=request.json['username'],
        password=scramble(request.json['password'])        
    )
    db.session.add(u) # prepare CREATE statement
    db.session.commit() # execute CREATE statement
    return jsonify(u.serialize())

@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    u = User.query.get_or_404(id)
    try:
        db.session.delete(u) # prepare DELETE statement
        db.session.commit() # execute DELETE statement
        return jsonify(True)
    except:
        # something went wrong :(
        return jsonify(False)

@bp.route('/<int:id>', methods=['PATCH', 'PUT'])
def update(id: int):
    u = User.query.get_or_404(id)
    if ('username') not in request.json and ('password') not in request.json:
        return abort(400)
    if 'username' in request.json:
        username=request.json['username']
        if (len(username) < 3):
            return abort(400)
        u.username = username
    if 'password' in request.json:
        password=scramble(request.json['password'])
        if (len(password) < 8):
            return abort(400)
        u.password = scramble(password)
    try:
        db.session.commit() # execute UPDATE statement
        return jsonify(u.serialize())
    except:
        # something went wrong :(
        return jsonify(False)
    
@bp.route('/<int:id>/liked_tweets', methods=['GET'])
def liked_tweets(id: int):
    u = User.query.get_or_404(id)
    result = []
    for u in u.liked_tweets:
        result.append(u.serialize())
    return jsonify(result)

@bp.route('/<int:id>/like', methods=['GET'])
def like(id: int):
    if 'tweet_id' not in request.json:
        return abort(400)
    if 'tweet_id' in request.json:
        t = Tweet.query.get_or_404(id)
    if 'user_id' in request.json:
        u = User.query.get_or_404(id)
    result = []
    for u, t in u.like, t.like:
        result.append(u.serialize())
        result.append(t.serialize())
    return jsonify(result)

stmt = sqlalchemy.insert(likes_table).values(name='spongebob', fullname="Spongebob Squarepants")