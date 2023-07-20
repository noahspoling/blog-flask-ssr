from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import Config


db = SQLAlchemy()

post_tags = db.Table('post_tags',
    db.Column('post_id', db.Integer, db.ForeignKey('post.id'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True)
)

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    from app.main.routes import routesBlueprint
    app.register_blueprint(routesBlueprint)

    return app