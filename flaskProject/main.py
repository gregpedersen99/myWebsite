from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    output = ''
    if request.method == 'POST':
        action = request.form['action']
        if action == 'generate_text_1':  # "Back" button on the second page
            return redirect(url_for('login_page'))
        elif action == 'generate_text_2':  # "Submit" button on the first page
            output = 'You are not Gregory, go away!'
            return render_template('login.html', output=output)
    return render_template('login.html', output=output)

@app.route('/login_page', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        action = request.form['action']
        if action == 'generate_text_1':  # "Back" button on the second page
            return redirect(url_for('index'))
        elif action == 'generate_text_2':  # "Submit" button on the second page
            return redirect(url_for('index'))  # Adjust to show different message or behavior if needed
    return render_template('login2.html')





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
