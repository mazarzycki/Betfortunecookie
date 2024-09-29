from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///counter.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)  # Initialize Flask-Migrate

class CookieCounter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer, default=0)

def create_db():
    with app.app_context():  # Use app context here
        db.create_all()
        if CookieCounter.query.count() == 0:
            initial_counter = CookieCounter(count=0)
            db.session.add(initial_counter)
            db.session.commit()

@app.route('/')
def index():
    counter = CookieCounter.query.first().count
    return render_template('index.html', counter=counter)

@app.route('/accept')
def accept_tip():
    return render_template('accept_tip.html')

@app.route('/get_tip')
def get_tip():
    counter_entry = CookieCounter.query.first()
    counter_entry.count += 1
    db.session.commit()

    matches = [
        ('Manchester United', 'Arsenal'),
        ('Liverpool', 'Chelsea'),
        ('Manchester City', 'Tottenham Hotspur'),
        ('Barcelona', 'Real Madrid'),
        ('Bayern Munich', 'Borussia Dortmund'),
    ]
    
    score_predictions = [
        '2-1', '1-1', '3-0', '0-2', '2-2', '1-0', '0-1', '2-0', '3-1'
    ]

    random_match = random.choice(matches)
    random_score = random.choice(score_predictions)

    match_display = f"{random_match[0]} - {random_match[1]}"
    
    return jsonify({'match': match_display, 'tip': f"Predicted score: {random_score}"})

if __name__ == '__main__':
    create_db()  # Call to initialize the database
    app.run(debug=True)
