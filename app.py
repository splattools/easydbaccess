from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from config import SQLALCHEMY_DATABASE_URI

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.before_request
def before_request():
    db.create_all()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"User('{self.name}', '{self.email}')"

@app.route("/")
def index():
    users = User.query.all()
    return render_template("index.html", users=users)

@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        db_type = request.form.get('db_type')
        if db_type == 'postgresql':
            app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://{user}:{password}@{host}/{db-name}'.format(**{
                'user': os.getenv('USERNAME'),
                'password': os.getenv('PASSWORD'),
                'host': os.getenv('HOST'),
                'db-name': os.getenv('DB_NAME'),
            })
        else:
            app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{user}:{password}@{host}/{db-name}?charset=utf8'.format(**{
                'user': os.getenv('USERNAME'),
                'password': os.getenv('PASSWORD'),
                'host': os.getenv('HOST'),
                'db-name': os.getenv('DB_NAME'),
            })
        db.create_all()
        user = User(name=name, email=email)
        db.session.add(user)
        db.session.commit()

    users = User.query.all()
    return render_template('index.html', users=users)

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
