from flask import Flask, session, redirect, url_for, request, jsonify, render_template, send_file
from datetime import datetime

app = Flask(__name__)
app.secret_key = b'uIO@1_$31&*_1Haj.,$801AAx+991HJ1a'            #for session management ... session data is encrypted with this key


@app.route('/login', methods=['GET'])               # to display login form
def loadLoginPage():
#{
    return render_template('login.html')
#}




@app.route('/logout')                               # this is invoked when user clicks logout
def logout():
#{
    return redirect(url_for('loadLoginPage'))
#}




@app.route('/')                                     # for loading the main page (post-login page)
def loadMainPage():
#{
    return render_template('index.html')
#}


@app.route('/sample-page')
def loadSamplePage():
#{
    return render_template('sample_page.html')
#}


@app.route('/login', methods=['POST'])              # for processing data sent from login form .. invoked when login button is clicked
def processLoginForm():
#{
    username = request.form['username']
    password = request.form['password']

    if(username == "siteadmin" and password == "1234"):         # hard coded until we integrate with database
    #{
        session["logged_in_username"] = username
        return redirect(url_for('loadMainPage'))            # login success, redirect to main page
    #}
    else:
    #{
        return redirect(url_for('loadLoginPage'))           # login failure, redirect to login page again
    #}
#}

@app.route('/api/testdata', methods=['GET'])
def sampleApi1():
#{
    ## todo implement data fetch related stuff

    output = {        # ref: https://www.w3schools.com/python/python_dictionaries.asp
        "data" : [ 1, 2, 21, 10, 15 ]
    }
    output = jsonify(output)       # ref: https://stackoverflow.com/questions/45412228/sending-json-and-status-code-with-a-flask-response/45412576
    return output
#}


@app.route('/api/testdata', methods=['POST'])
def sampleApi2():
#{
    ## todo implement data insert related stuff

    returnValue = 1

    output = {        # ref: https://www.w3schools.com/python/python_dictionaries.asp
        "data" : returnedValue
    }
    output = jsonify(output)       # ref: https://stackoverflow.com/questions/45412228/sending-json-and-status-code-with-a-flask-response/45412576
    return output    
#}


"""
references:
1. https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application
2. https://flask.palletsprojects.com/en/1.1.x/quickstart/#rendering-templates
3. https://flask.palletsprojects.com/en/1.1.x/quickstart/#sessions
"""
