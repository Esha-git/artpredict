from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Landing page
@app.route('/')
def about():
    return render_template('about.html', title='About Us')

# Login selection page
@app.route('/login')
def login():
    return render_template('login.html', title='Login')

# Data Scientist login
@app.route('/login/data_scientist', methods=['GET', 'POST'])
def login_data_scientist():
    if request.method == 'POST':
        if request.form['username'] == 'esha' and request.form['password'] == '123':
            return redirect(url_for('home'))
        else:
            return 'Invalid Credentials'
    return render_template('login.html', title='Login')

# Clinician login
@app.route('/login/clinician', methods=['GET', 'POST'])
def login_clinician():
    if request.method == 'POST':
        if request.form['username'] == 'eram' and request.form['password'] == '123':
            return redirect(url_for('home'))
        else:
            return 'Invalid Credentials'
    return render_template('login.html', title='Login')

# Home Page
@app.route('/home')
def home():
    return render_template('home.html', title='Home')

@app.route('/')
def index():
    return render_template('index.html')

# Services Page
@app.route('/services')
def services():
    return render_template('services.html', title='Services')

# View Patient Page
@app.route('/view_patient')
def view_patient():
    return render_template('view_patient.html', title='View Patient')

# Add Patient Page
@app.route('/add_patient')
def add_patient():
    return render_template('add_patient.html', title='Add New Patient')

if __name__ == '__main__':
    app.run(debug=True)
