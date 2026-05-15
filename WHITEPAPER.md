# EventDate: Design Decisions & Rationale

## Overview
This document explains the design decisions behind **EventDate**, a minimal open-source tool for finding and joining events to meet new people.

## Tech Stack Choices
### 1. **Backend: Flask + SQLite (Python)**
   - **Why?** Lightweight, easy to deploy, and integrates well with SQLite for local storage.
   - **Alternatives Considered:** Django (overkill for MVP), FastAPI (less mature for simple projects).

### 2. **Frontend: HTML/CSS/JS + Bootstrap**
   - **Why?** Simple, no build step, and works out of the box with Flask.
   - **Alternatives Considered:** React/Vue (unnecessary complexity for MVP).

### 3. **Database: SQLite**
   - **Why?** Lightweight, file-based, and requires no setup.
   - **Future Work:** Replace with PostgreSQL for scalability.

## Key Design Decisions
### 1. **Mock Data for MVP**
   - **How?** Hardcoded mock data to simulate user profiles and events.
   - **Why?** Simplifies the MVP and avoids user authentication.
   - **Limitations:** No real-time updates or dynamic content.
   - **Future Work:** Add user authentication and real event data.

### 2. **Event-Centric Design**
   - **How?** Focuses on events as the primary way to meet people.
   - **Why?** Differentiates from traditional dating apps.
   - **Future Work:** Add event discovery and recommendations.

### 3. **No Chat Backend (MVP)**
   - **Why?** Focuses on event discovery and RSVPs first.
   - **Future Work:** Add real-time chat with WebSockets.

## Challenges & Workarounds
### 1. **Database Initialization**
   - **Issue:** SQLite database was empty on first run.
   - **Workaround:** Added mock data initialization in `app.py`.

### 2. **Port Conflicts**
   - **Issue:** Flask server failed to start due to port 5000/5001/5002/5003 being in use.
   - **Workaround:** Switched to port 5004.

### 3. **Frontend Styling**
   - **Issue:** Events were not displaying correctly.
   - **Workaround:** Updated the frontend to dynamically load events.

## License
MIT