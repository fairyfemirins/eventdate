# EventDate - Event-Based Dating App

A minimal open-source tool for finding and joining events to meet new people.

## Features
- Post events you are attending.
- Browse and join events posted by others.
- RSVP and confirm attendance.
- Mock data for testing (replace with real user data in production).

## Tech Stack
- **Backend:** Python + Flask + SQLite
- **Frontend:** HTML/CSS/JS + Bootstrap

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/fairyfemirins/eventdate.git
   cd eventdate
   ```

2. Install dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. Run the server:
   ```bash
   python app.py
   ```

4. Open `http://localhost:5004` in your browser.

## Usage
- Browse events and click "RSVP" to join.
- In a real app, you would chat and match with other attendees.

## License
MIT