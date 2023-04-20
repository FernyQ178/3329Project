from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/dietary_restrictions', methods=['GET', 'POST'])
def dietary_restrictions():
    if request.method == 'POST':
        # process the form data here
        return render_template('dietary_restrictions.html')

    return render_template('dietary_restrictions.html')

if __name__ == '__main__':
    app.run(debug=True)

#{{ url_for('static', filename='style.css') }}