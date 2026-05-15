#!/usr/bin/env python3
"""
EventDate - Event-Based Dating App

Features:
- Post events you are attending.
- Browse and join events posted by others.
- Chat and match with people attending the same event.
"""

import os
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///eventdate.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    events = db.relationship('Event', backref='organizer', lazy=True)
    rsvps = db.relationship('RSVP', backref='user', lazy=True)


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(50), nullable=False)
    organizer_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    rsvps = db.relationship('RSVP', backref='event', lazy=True)


class RSVP(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)
    status = db.Column(db.String(20), nullable=False, default='pending')  # pending/attending


@app.route('/')
def index():
    # Add mock data if database is empty
    if User.query.count() == 0:
        mock_users = [
            User(username="Alice", email="alice@example.com"),
            User(username="Bob", email="bob@example.com"),
            User(username="Charlie", email="charlie@example.com")
        ]
        db.session.bulk_save_objects(mock_users)
        db.session.commit()
        
        mock_events = [
            Event(
                title="Sunset Hiking Trip",
                description="Join us for a relaxing hike at sunset!",
                location="Griffith Park, LA",
                date="2026-06-15",
                organizer_id=1
            ),
            Event(
                title="Tech Conference 2026",
                description="Annual tech conference with keynote speakers and workshops.",
                location="San Francisco, CA",
                date="2026-07-20",
                organizer_id=2
            ),
            Event(
                title="Beach Cleanup",
                description="Help clean up Santa Monica Beach and meet like-minded people!",
                location="Santa Monica, CA",
                date="2026-06-30",
                organizer_id=3
            )
        ]
        db.session.bulk_save_objects(mock_events)
        db.session.commit()
    
    return render_template('index.html')


@app.route('/api/events', methods=['GET'])
def get_events():
    events = Event.query.all()
    return jsonify([{
        'id': event.id,
        'title': event.title,
        'description': event.description,
        'location': event.location,
        'date': event.date,
        'organizer': event.organizer.username
    } for event in events])


@app.route('/api/rsvp', methods=['POST'])
def create_rsvp():
    data = request.json
    user_id = data.get('user_id')
    event_id = data.get('event_id')
    
    if not user_id or not event_id:
        return jsonify({'error': 'Missing user_id or event_id'}), 400
    
    rsvp = RSVP(user_id=user_id, event_id=event_id, status='attending')
    db.session.add(rsvp)
    db.session.commit()
    
    return jsonify({'message': 'RSVP created successfully'}), 201


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5004, debug=True)