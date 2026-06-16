from flask import Flask
from models import db 
from controllers.cinema_controller import cinema_bp
from dados_iniciais import popular_dados

app = Flask(__name__, template_folder="views/templates")

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cinema.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  

db.init_app(app)
app.register_blueprint(cinema_bp)

with app.app_context():
    db.create_all()
    popular_dados()

if __name__ == "__main__":
    app.run(debug=True)
