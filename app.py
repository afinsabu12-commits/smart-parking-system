import boto3
from flask import Flask, render_template, request
from flask_mysqldb import MySQL
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
s3 = boto3.client(
    's3',
   
)

BUCKET_NAME = 'smart-parking-afin'

from flask import Flask, render_template, request
from flask_mysqldb import MySQL


app = Flask(__name__)
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["100 per hour"]
)
@app.after_request
def security_headers(response):
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    return response
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'afin@123'
app.config['MYSQL_DB'] = 'smartparking'

mysql = MySQL(app)

@app.route('/')
def home():

    cur = mysql.connection.cursor()

    cur.execute("SELECT * FROM parking_slots")

    slots = cur.fetchall()

    cur.close()

    return render_template(
        'index.html',
        slots=slots
    )

@app.route('/book', methods=['POST'])
def book():

    slot_id = request.form['slot_id']
    vehicle_number = request.form['vehicle_number']

    cur = mysql.connection.cursor()

    cur.execute(
    "INSERT INTO bookings (slot_id, vehicle_number) VALUES (%s,%s)",
    (slot_id, vehicle_number)
)

    cur.execute(
        "UPDATE parking_slots SET status='Booked' WHERE id=%s",
        (slot_id,)
    )

    mysql.connection.commit()

    cur.close()

    return render_template('success.html')
@app.route('/add_slot', methods=['POST'])
def add_slot():

    slot = request.form['slot']

    cur = mysql.connection.cursor()

    cur.execute(
        "INSERT INTO parking_slots(slot_number,status) VALUES(%s,%s)",
        (slot, 'Available')
    )

    mysql.connection.commit()

    cur.close()

    return admin()


@app.route('/admin')
def admin():

    cur = mysql.connection.cursor()

    users = []

    cur.execute("SELECT * FROM parking_slots")
    slots = cur.fetchall()

    cur.execute("SELECT * FROM bookings")
    bookings = cur.fetchall()

    cur.close()

    return render_template(
        'admin.html',
        users=users,
        slots=slots,
        bookings=bookings
    )
@app.route('/delete_slot/<int:id>', methods=['POST'])
def delete_slot(id):

    cur = mysql.connection.cursor()

    cur.execute(
        "DELETE FROM parking_slots WHERE id=%s",
        (id,)
    )

    mysql.connection.commit()

    cur.close()

    return admin()

@app.route('/update_slot/<int:id>', methods=['POST'])
def update_slot(id):

    cur = mysql.connection.cursor()

    cur.execute(
        "SELECT status FROM parking_slots WHERE id=%s",
        (id,)
    )

    slot = cur.fetchone()

    if slot[0] == "Available":
        new_status = "Booked"
    else:
        new_status = "Available"

    cur.execute(
        "UPDATE parking_slots SET status=%s WHERE id=%s",
        (new_status, id)
    )

    mysql.connection.commit()

    cur.close()

    return admin()
@app.route('/history')
def history():

    cur = mysql.connection.cursor()

    cur.execute("""
        SELECT
            bookings.id,
            bookings.vehicle_number,
            parking_slots.slot_number
        FROM bookings
        JOIN parking_slots
        ON bookings.slot_id = parking_slots.id
    """)

    history = cur.fetchall()

    cur.close()

    return render_template(
        'history.html',
        history=history
    )
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
