# coding:utf-8
from flask import Blueprint
import flask_restful as restful


blueprint = Blueprint('api', __name__)
api = restful.Api()
api.init_app(blueprint)

from . import view
from . import user
