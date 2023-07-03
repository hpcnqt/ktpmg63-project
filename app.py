from flask import Flask
from config import AppConfig as Config
from controller.dashboard import dashboard_bp
from controller.household import household_bp
from controller.population import population_bp
from controller.asset import asset_bp
from controller.authentication import authentication_bp

app = Flask(__name__)

app.register_blueprint(authentication_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(household_bp)
app.register_blueprint(population_bp)
app.register_blueprint(asset_bp)


app.config.from_object(Config)
app.jinja_env.auto_reload = True


if __name__ == "__main__":
    app.run(debug=True, port='5096')