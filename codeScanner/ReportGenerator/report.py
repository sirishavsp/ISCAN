from flask import Blueprint, request, jsonify
from flask import url_for
import os
from flask import Blueprint, request, jsonify, url_for, current_app, send_from_directory
from flask import render_template_string
import os

report_blueprint = Blueprint('report_blueprint', __name__)

@report_blueprint.route('/generate_report/<path:filepath>', methods=['POST'])
def generate(filepath):
    data = request.get_json()
    print(request.json)  # Print the request.json
    results = data.get('results', [])  
    report = generate_report(results)

    # Save the report in the "static/reports" directory
    report_folder = current_app.config['REPORT_FOLDER']
    if not os.path.exists(report_folder):
        os.makedirs(report_folder)

    report_filepath = os.path.join(report_folder, f'{filepath}_report.html')
    with open(report_filepath, 'w') as f:
        f.write(report)

    # Generate the URL for the report file
    report_url = url_for('static', filename=os.path.join('reports', f'{filepath}_report.html'), _external=True)

    return jsonify({'message': 'Report generated successfully', 'report_url': report_url})


@report_blueprint.route('/report/<path:filepath>', methods=['GET'])
def view_report(filepath):
    report_folder = current_app.config['REPORT_FOLDER']
    report_filepath = os.path.join(report_folder, f'{filepath}_report.html')
    if os.path.exists(report_filepath):
        return send_from_directory(report_folder, f'{filepath}_report.html')
    else:
        return "Report not found", 404

def generate_report(results):
    unique_results = process_results(results)  # Process the results to remove duplicates
    sorted_results = sort_results(unique_results)  # Sort the results

    # # Load the report template from a file
    # with open('report.html', 'r') as file:
    #     report_template = file.read()

    # # Render the report using the template and the results
    # report = render_template_string(report_template, results=sorted_results)
    #     # Load the report template from a file
    with open('report2.html', 'r') as file:
        report_template = file.read()
    # Add this code here
    from collections import Counter
    severity_counts = Counter(result['severity'] for result in sorted_results)
    chart_data = {
        'high': severity_counts.get('high', 0),
        'medium': severity_counts.get('medium', 0),
        'low': severity_counts.get('low', 0),
    }

    # Render the report using the template and the results
    report = render_template_string(report_template, results=sorted_results)

    return report


def flatten(lst):
    flattened = []
    stack = [lst]
    
    while stack:
        curr = stack.pop()
        if isinstance(curr, list):
            stack.extend(curr)
        else:
            flattened.append(curr)
    
    return flattened

def process_results(results):
    flattened_results = flatten(results)
    unique_results = list(set(tuple(sorted(d.items())) for d in flattened_results))
    unique_results = [dict(t) for t in unique_results]
    return unique_results

def sort_results(results):
    return sorted(results, key=lambda x: (x.get('severity'), x.get('line_number')))
