"""
CSCI E-11 Lab 2:
Run a simple web server with an SQL injection vulnerability.
"""

import logging
import sqlite3

from flask import Flask, request, render_template_string

app = Flask(__name__)
app.logger.setLevel(logging.INFO)  # Set the logging level directly  

DB_FILE = '/home/ec2-user/students.db'

# HTML template with form for inputs
HTML_TEMPLATE = '''
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Search Student Database</title>
    <style>
        table {
            border-collapse: collapse;
            width: 100%;
        }
        th, td {
            border: 1px solid black;
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #f2f2f2;
        }
    </style>
  </head>
  <body>
    <h2>Search the Student Database</h2>
    <form method="POST">
      <label for="student_id">STUDENT ID:</label>
      <input id="student_id" name="student_id" required/><br><br>
      <input type="submit" value="Submit">
    </form>
    {% if rows is not none %}
      <p>Results</p>
        <table>
        {% for row in rows %}
            <tr>
                {% for cell in row %}
                <td>{{ cell }}</td>
                {% endfor %}
            </tr>
        {% endfor %}
        </table>
    {% endif %}
  </body>
</html>
'''


# Get the database connection
conn  = sqlite3.connect( DB_FILE )

def lookup(student_id):                                                                     
    """Lookup a student by id"""                                                           
    cur = conn.cursor()                                                                    
    cmd = 'select * from students where student_id = ?'                                     
    app.logger.info(cmd, student_id)                                                       
    return cur.execute(cmd, (student_id,)).fetchall() 

# Build the database
@app.route('/', methods=['GET', 'POST'])
def home_page():
    """Display the home page"""
    # Get client IP address
    if request.headers.getlist("X-Forwarded-For"):
        client_ip = request.headers.getlist("X-Forwarded-For")[0]
    else:
        client_ip = request.remote_addr

    result = None
    if request.method == 'POST':
        # Retrieve input values, convert to integers, and calculate the sum
        student_id = request.form.get('student_id', None)
        app.logger.info("client_ip=%s referrer=%s user_agent=%s student_id=%s",
                        client_ip,
                        request.headers.get("Referer", "-"),
                        request.headers.get("User-Agent", "-"),
                        student_id)

        if student_id is not None:
            result = lookup(student_id)

    # Render the HTML template with the result
    app.logger.info("result=%s",result)
    return render_template_string(HTML_TEMPLATE, rows=result)

if __name__ == '__main__':
    app.run(debug=True)