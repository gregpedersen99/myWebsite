from flask import Flask, request, render_template, redirect, url_for
import os


app = Flask(__name__)

# Access the environment variables set on Heroku
CORRECT_USERNAME = os.getenv('USERNAME')
CORRECT_PASSWORD = os.getenv('PASSWORD')

@app.route('/', methods=['GET', 'POST'])
def index():
    output = ''
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'generate_text_1':  # "Back" button on the second page
            return redirect(url_for('login_page'))
        elif action == 'generate_text_2':  # "Submit" button on the first page
            return redirect(url_for('publicHome'))
    return render_template('login.html', output=output)

@app.route('/login_page', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
            return redirect(url_for('myHome'))
        else:
            # Handle incorrect credentials (e.g., show an error message)
            return render_template('login2.html', error="Invalid username or password.")
    return render_template('login2.html')

@app.route('/myHome')
def myHome():
    return render_template('myHome.html')

@app.route('/publicHome')
def publicHome():
    return render_template('publicHome.html')

if __name__ == '__main__':
    # Get the port from the environment variable, default to 5000 if not set
    port = int(os.environ.get("PORT", 5000))
    # Run the application on all network interfaces at the specified port
    app.run(host='0.0.0.0', port=port, debug=True)


  #Lmao the background photo is so shit but whatever Im going to change that next
  #Tod do List:
    #Format and add a good background photo
    #Change button formats 
    #Add password and username option for a Gregory Pederen = 'Yes' ubmission 
