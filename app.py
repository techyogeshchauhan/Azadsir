# from flask import Flask, request, render_template, redirect, url_for
# import mysql.connector

# app = Flask(__name__)

# # Database connection
# def get_db_connection():
#     conn = mysql.connector.connect(
#         host='localhost',
#         user='root',  # Default XAMPP MySQL username
#         password='',  # Default XAMPP MySQL password (leave blank if not set)
#         database='calc'
#     )
#     return conn

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     sum_result = None  # Initialize sum_result to None

#     if request.method == 'POST':
#         num1 = request.form['num1']
#         num2 = request.form['num2']
#         sum_result = int(num1) + int(num2)

#         # Store result in the database only if the user confirms
#         if 'store' in request.form:
#             # Store result in the database
#             conn = get_db_connection()
#             cursor = conn.cursor()
#             cursor.execute("INSERT INTO result (num1, num2, sum) VALUES (%s, %s, %s)", (num1, num2, sum_result))
#             conn.commit()
#             cursor.close()
#             conn.close()

#             return redirect(url_for('index'))  # Redirect after storing

#     return render_template('index.html', sum_result=sum_result)  # Pass sum_result to the template

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, request, render_template, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Database connection
def get_db_connection():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',  # Default XAMPP MySQL username
        password='',  # Default XAMPP MySQL password (leave blank if not set)
        database='calc'
    )
    return conn

@app.route('/', methods=['GET', 'POST'])
def index():
    sum_result = None  # Initialize sum_result to None

    if request.method == 'POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
        sum_result = int(num1) + int(num2)

        # Store result in the database only if the user confirms
        if 'store' in request.form:
            # Store result in the database
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO result (num1, num2, sum) VALUES (%s, %s, %s)", (num1, num2, sum_result))
            conn.commit()
            cursor.close()
            conn.close()

            return redirect(url_for('index'))  # Redirect after storing

    return render_template('index.html', sum_result=sum_result)  # Pass sum_result to the template

@app.route('/records')
def records():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM result")
    records = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template('records.html', records=records)

if __name__ == '__main__':
    app.run(debug=True)
