from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)

app.config.from_object(Config)

db = SQLAlchemy(app)

# Home Page
@app.route('/')
def home():
    return render_template('index.html')

# Water Analysis Form Page
@app.route('/analyze', methods=['GET', 'POST'])
def analyze():
    if request.method == 'POST':
        ph = float(request.form.get('ph', 7))
        total_coliforms = int(request.form.get('total-coliforms', 0))
        e_coli = int(request.form.get('e-coli', 0))
        iron = float(request.form.get('iron', 0))
        manganese = float(request.form.get('manganese', 0))
        nitrite = float(request.form.get('nitrite', 0))
        nitrate = float(request.form.get('nitrate', 0))
        arsenic = float(request.form.get('arsenic', 0))
        # Use ['hardness', 0] to default to 0 if no value is provided as hardness poses no health risk
        hardness = float(request.form.get('hardness', 0))


        # Placeholer for results
        results = {
            'ph': ph,
            'total-coliforms': total_coliforms,
            'e-coli': e_coli,
            'iron': iron,
            'manganese': manganese,
            'nitrite': nitrite,
            'nitrate': nitrate,
            'arsenic': arsenic,
            'hardness': hardness
        }

        # pH Condition
        if ph < 6.5:
            results['ph_recommendation'] = "Consider using a pH neutralizing filter (calcite or magnesium oxide) to raise the pH."
        elif ph > 9.5:
            results['ph_recommendation'] = "Use an acid injection system to lower the pH."
        else:
            results['ph_recommendation'] = "No action needed. pH is within the acceptable range."

        # Total Coliforms Condition
        if total_coliforms > 0:
            results['coliform_recommendation'] = "Install a UV disinfection system to kill bacteria or use chlorination treatment."
        else:
            results['coliform_recommendation'] = "No action needed. Total coliforms are not detected."

        # E. Coli Condition
        if e_coli > 0:
            results['e_coli_recommendation'] = "Install a UV disinfection system and/or chlorination to treat E. Coli contamination."
        else:
            results['e_coli_recommendation'] = "No action needed. E. Coli is not detected."

        # Iron Condition
        if iron > 200:
            results['iron_recommendation'] = "Use an iron removal filter (manganese greensand or Birm filter) to reduce iron levels."
        else:
            results['iron_recommendation'] = "No action needed. Iron levels are within the acceptable range."

        # Manganese Condition
        if manganese > 50:
            results['manganese_recommendation'] = "Use a manganese removal filter (manganese greensand or catalytic carbon) to treat high manganese levels."
        else:
            results['manganese_recommendation'] = "No action needed. Manganese levels are within the acceptable range."

        # Nitrite Condition
        if nitrite > 0.5:
            results['nitrite_recommendation'] = "Install an ion-exchange filter or reverse osmosis system to reduce nitrite levels."
        else:
            results['nitrite_recommendation'] = "No action needed. Nitrite levels are within the acceptable range."

        # Nitrate Condition
        if nitrate > 50:
            results['nitrate_recommendation'] = "Use a reverse osmosis system or anion exchange unit to reduce nitrate levels."
        else:
            results['nitrate_recommendation'] = "No action needed. Nitrate levels are within the acceptable range."

        # Arsenic Condition
        if arsenic > 10:
            results['arsenic_recommendation'] = "Install an arsenic-specific filter (adsorption media, reverse osmosis, or ion exchange)."
        else:
            results['arsenic_recommendation'] = "No action needed. Arsenic levels are within the acceptable range."

        # Hardness Condition
        if hardness > 200:
            results['hardness_recommendation'] = "Consider installing a water softener to reduce hardness and prevent scale buildup."
        else:
            results['hardness_recommendation'] = "No action needed. Hardness levels are within an acceptable range."

            # To handle form submission
        return render_template('results.html', results=results)
    return render_template('form.html')

# Analysis Results Page
# @app.route('/results')
# def results():
#     return render_template('results.html')

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