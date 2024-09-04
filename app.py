from flask import Flask, render_template, request

app = Flask(__name__)

# Home Page
@app.route('/')
def home():
    return render_template('index.html')

# Water Analysis Form Page
@app.route('/analyze', methods=['GET', 'POST'])
def analyze():
    if request.method == 'POST':
        ph = int(request.form['ph'])
        total_coliforms = int(request.form['total-coliforms'])
        e_coli = int(request.form['e-coli'])
        iron = int(request.form.get('iron'))
        manganese = int(request.form['manganese'])
        nitrite = int(request.form['nitrite'])
        nitrate = int(request.form['nitrate'])
        arsenic = int(request.form['arsenic'])
        # Use ['hardness', 0] to default to 0 if no value is provided as hardness poses no health risk
        hardness = int(request.form['hardness'])


        # Placeholer for results
        results = {


        }


        # To handle form submission
        return render_template('results.html')
    return render_template('form.html')

# Analysis Results Page
@app.route('/results')
def results():
    return render_template('results.html')

# About Page
@app.route('/about')
def about():
    return render_template('about.html')

# Contact Page
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)