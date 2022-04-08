from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "why?"

@app.route('/')
def index():
    return render_template ('index.html')

@app.route('/process', methods=['POST'])
def process_form():
    session['form']=request.form
    return redirect ('/result')

@app.route('/result', methods=['GET'])
def result():
    print(session['form'])
    return render_template ('result.html')

@app.route('/end')
def end_session():
    session.clear()
    return redirect('/')

if __name__=="__main__":  
    app.run(debug=True, port=5001)  