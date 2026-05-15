# EventDate: Reproducible Tutorial

This tutorial guides you through setting up and running **EventDate** locally.

## Prerequisites
- Linux environment (tested on Ubuntu 22.04).
- Python 3.10+.
- `pip` and `virtualenv`.

## Step 1: Clone the Repository
```bash
 git clone https://github.com/fairyfemirins/eventdate.git
 cd eventdate
```

## Step 2: Set Up a Virtual Environment
```bash
 python3 -m venv venv
 source venv/bin/activate
```

## Step 3: Install Dependencies
```bash
 pip install -r requirements.txt
```

**Note:** If `requirements.txt` is missing, create it with:
```bash
 pip freeze > requirements.txt
```

## Step 4: Run the Flask Server
```bash
 python app.py
```

The server will start at `http://localhost:5004`.

## Step 5: Test the App
1. Open `http://localhost:5004` in your browser.
2. Browse mock events (Sunset Hiking Trip, Tech Conference 2026, Beach Cleanup).
3. Click "RSVP" to join an event.

## Step 6: Verify the Database
- The SQLite database (`eventdate.db`) is created in the `instance/` directory.
- To inspect it, use:
  ```bash
  sqlite3 instance/eventdate.db "SELECT * FROM event;"
  ```

## Troubleshooting
### 1. **Port 5004 in Use**
   - **Solution:** Kill the conflicting process:
     ```bash
     pkill -f "python app.py"
     ```
   - **Alternative:** Change the port in `app.py`:
     ```python
     if __name__ == '__main__':
         app.run(host='0.0.0.0', port=5005, debug=True)
     ```

### 2. **No Events Displayed**
   - **Solution:** Ensure the database is initialized:
     ```bash
     rm instance/eventdate.db
     python app.py
     ```

### 3. **Frontend Not Loading**
   - **Solution:** Clear your browser cache or try a different browser.

## License
MIT