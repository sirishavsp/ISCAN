from flask import Flask, request, render_template, send_from_directory
import os
from report import generate_report, report_blueprint

app = Flask(__name__)
app.register_blueprint(report_blueprint)  # Register the report blueprint
app.config['REPORT_FOLDER'] = os.path.join(app.root_path, 'static', 'reports')

@app.route('/')
def index():
    reports = [report.replace('static/reports/', '') for report in os.listdir(app.config['REPORT_FOLDER'])]
    return render_template('index.html', reports=reports)

if __name__ == "__main__":
    app.run(port=8080, debug=True)
