import http.client
from flask_restplus import Namespace, Resource, fields
from stat_backend.models import StatisticsModel, UpdatesModel
from stat_backend.db import db
from flask import abort


api_namespace = Namespace("api", descriptions="Available API operations")
