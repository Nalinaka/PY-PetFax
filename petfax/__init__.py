# config                    
from flask import Flask
from flask_migrate import Migrate


# factory
def create_app():
    app = Flask(__name__)

    # database config 
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/petfax'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False   


   # index route
    @app.route('/')
    def index():

    # register pet blueprint
        from . import pet
        app.register_blueprint(pet.bp)

        # register fact blueprint
        from . import fact
        app.register_blueprint(fact.bp)

        from . import models
        models.db.init_app(app)
        migrate = Migrate(app, models.db)

        # return the app
        return app