from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    output = ''
    if request.method == 'POST':
        if request.form['action'] == 'generate_text_1':
            output = 'Hello Gregory!'
        elif request.form['action'] == 'generate_text_2':
            output = 'You are not Gregory, go away!'
    return render_template('login.html', output=output)

if __name__ == '__main__':
    # Get the port from the environment variable, default to 5000 if not set
    port = int(os.environ.get("PORT", 5000))
    # Run the application on all network interfaces at the specified port
    app.run(host='0.0.0.0', port=port, debug=True)


  #Lmao the background photo is so shit but whatever Im going to change that next
  #Tod do List:
    #Format and add a good background photo
    #Change button formats 
    #Add password and username option for a Gregory Pederen = 'Yes' submission 
    