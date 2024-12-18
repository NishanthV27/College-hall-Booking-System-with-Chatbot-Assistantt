from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Database setup function for classroom bookings (using database.db)
def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    
    # Create classroom bookings table (if needed)
    c.execute('''CREATE TABLE IF NOT EXISTS bookings (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    classroom_name TEXT NOT NULL,
                    booking_date TEXT NOT NULL,
                    start_time TEXT NOT NULL,
                    end_time TEXT NOT NULL,
                    purpose TEXT NOT NULL)''')
    conn.commit()
    conn.close()

# Database setup function for lab bookings (using la.db)
def init_lab_db():
    conn = sqlite3.connect('la.db')
    c = conn.cursor()
    
    # Create lab bookings table (if needed)
    c.execute('''CREATE TABLE IF NOT EXISTS lab_bookings (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    lab_name TEXT NOT NULL,
                    booking_date TEXT NOT NULL,
                    start_time TEXT NOT NULL,
                    end_time TEXT NOT NULL,
                    purpose TEXT NOT NULL)''')
    conn.commit()
    conn.close()

# Database setup function for seminar hall bookings (using seminar.db)
def init_seminar_db():
    conn = sqlite3.connect('seminar.db')
    c = conn.cursor()
    
    # Create seminar hall bookings table (if needed)
    c.execute('''CREATE TABLE IF NOT EXISTS seminar_bookings (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    seminar_name TEXT NOT NULL,
                    booking_date TEXT NOT NULL,
                    start_time TEXT NOT NULL,
                    end_time TEXT NOT NULL,
                    purpose TEXT NOT NULL)''')
    conn.commit()
    conn.close()

# Home route - Chat page
@app.route('/')
def home():
    return render_template('chat.html')

# Route to display classroom booking form
@app.route('/classroom-booking')
def classroom_booking_form():
    return render_template('classroom_booking_form.html')

# Route to handle classroom booking form submission
@app.route('/classroom-booking', methods=['POST'])
def book_classroom():
    classroom_name = request.form['classroomName']
    booking_date = request.form['date']
    start_time = request.form['startTime']
    end_time = request.form['endTime']
    purpose = request.form['purpose']
    
    # Insert classroom booking data into the database
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("INSERT INTO bookings (classroom_name, booking_date, start_time, end_time, purpose) VALUES (?, ?, ?, ?, ?)",
              (classroom_name, booking_date, start_time, end_time, purpose))
    conn.commit()
    conn.close()

    return redirect(url_for('home'))  # Redirect to home after form submission

# Route to display lab booking form
@app.route('/lab-booking')
def lab_booking_form():
    return render_template('lab_booking_form.html')

# Route to handle lab booking form submission (Store in la.db database)
@app.route('/lab-booking', methods=['POST'])
def book_lab():
    lab_name = request.form['labName']
    booking_date = request.form['date']
    start_time = request.form['startTime']
    end_time = request.form['endTime']
    purpose = request.form['purpose']

    # Insert lab booking data into the la.db database
    conn = sqlite3.connect('la.db')
    c = conn.cursor()
    c.execute("INSERT INTO lab_bookings (lab_name, booking_date, start_time, end_time, purpose) VALUES (?, ?, ?, ?, ?)",
              (lab_name, booking_date, start_time, end_time, purpose))
    conn.commit()
    conn.close()

    # Redirect to confirmation page or home
    return redirect(url_for('home'))  # Redirect to home after form submission

# Route to display seminar hall booking form
@app.route('/seminar-booking')
def seminar_booking_form():
    return render_template('seminar_booking_form.html')

# Route to handle seminar hall booking form submission (Store in seminar.db database)
@app.route('/seminar-booking', methods=['POST'])
def book_seminar():
    seminar_name = request.form['seminarName']
    booking_date = request.form['date']
    start_time = request.form['startTime']
    end_time = request.form['endTime']
    purpose = request.form['purpose']

    # Insert seminar hall booking data into the seminar.db database
    conn = sqlite3.connect('seminar.db')
    c = conn.cursor()
    c.execute("INSERT INTO seminar_bookings (seminar_name, booking_date, start_time, end_time, purpose) VALUES (?, ?, ?, ?, ?)",
              (seminar_name, booking_date, start_time, end_time, purpose))
    conn.commit()
    conn.close()

    # Redirect to confirmation page or home
    return redirect(url_for('home'))  # Redirect to home after form submission

# Route to view all classroom bookings
@app.route('/view-classroom-bookings')
def view_classroom_bookings():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM bookings")
    bookings = c.fetchall()
    conn.close()
    return render_template('view_bookings.html', bookings=bookings)

# Route to view all lab bookings (from la.db)
@app.route('/view-lab-bookings')
def view_lab_bookings():
    conn = sqlite3.connect('la.db')
    c = conn.cursor()
    c.execute("SELECT * FROM lab_bookings")
    bookings = c.fetchall()
    conn.close()
    return render_template('view_bookings.html', bookings=bookings)

# Route to view all seminar hall bookings (from seminar.db)
@app.route('/view-seminar-bookings')
def view_seminar_bookings():
    conn = sqlite3.connect('seminar.db')
    c = conn.cursor()
    c.execute("SELECT * FROM seminar_bookings")
    bookings = c.fetchall()
    conn.close()
    return render_template('view_bookings.html', bookings=bookings)

if __name__ == '__main__':
    init_db()         # Initialize classroom bookings database (creates table if not exists)
    init_lab_db()     # Initialize lab bookings database (creates table if not exists)
    init_seminar_db() # Initialize seminar hall bookings database (creates table if not exists)
    app.run(debug=True)
