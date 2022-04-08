from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "why?"

# render initial page, user fills out and submits form
@app.route('/')
def index():
    return render_template ('index.html')

# POST form submission and redirect to result
@app.route('/process', methods=['POST'])
def process_form():
    session['form']=request.form
    return redirect ('/result')

# render result and print out input
@app.route('/result', methods=['GET'])
def result():
    print(session['form'])
    return render_template ('result.html')

# clear session and return to initial page
@app.route('/end')
def end_session():
    session.clear()
    return redirect('/')

if __name__=="__main__":  
    app.run(debug=True, port=5001)  