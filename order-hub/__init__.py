from flask import Flask
from flask import Flask, request, render_template, abort, session, redirect, url_for
from markupsafe import escape
from .database import init_app

app = Flask(__name__)
init_app(app)