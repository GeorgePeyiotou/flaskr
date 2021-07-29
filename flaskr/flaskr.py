from flask import Flask, render_template, request, flash, redirect, url_for, session, g


import os

app = Flask(__name__)


@app.route('/')
def flaskr():
    return render_template('mainapp/index.html')

@app.route('/echo', methods=['GET','POST'])
def echo():
    if request.method == 'GET':
        return render_template('mainapp/echo.html')
    else:
        echoText = request.form['echoText']
        echoCmd = 'echo ' + echoText
        #echoCmd = 'dir'
        stream = os.popen(echoCmd)
        output = stream.read()
        for outline in output.split('\n'):
            if outline != '':
                flash(outline)
        return render_template('mainapp/echo.html')

@app.route('/dir', methods=['GET','POST'])
def dir():
    if request.method == 'GET':
        return render_template('mainapp/dir.html')
    else:
        dirText = request.form['dirText']
        dirCmd = 'dir ' + dirText
        stream = os.popen(dirCmd)
        output = stream.read()
        for outline in output.split('\n'):
            if outline != '':
                flash(outline)
        return render_template('mainapp/dir.html')



app.env = 'development'
app.secret_key = 'super secret key'
app.templates_auto_reload = True

if __name__ == '__main__':
    app.run()
