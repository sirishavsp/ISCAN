from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'


class InputForm(FlaskForm):
    url = StringField('URL', validators=[DataRequired()])


def generate_report(results,report_filepath):
    if results:
        results = unique_results(results)
        with open(report_filepath, 'w') as f:
            f.write('<!DOCTYPE html>\n<html>\n<head>\n<title>IaC Security Scanner Results</title>\n')
            f.write('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"')
            f.write(' integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm"')
            f.write(' crossorigin="anonymous">\n')
            f.write('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.62.2/codemirror.min.css" integrity="sha512-v5gLZQ0vSl9E7Lqlx2r2mkS7V+76CGbbtbdwSdMnBn2mF8oNML4BC+4VJ7d3gX6CC0d0P4C9VZiJWyN/TS7ig==" crossorigin="anonymous" referrerpolicy="no-referrer" />\n')
            f.write('</head>\n<body>\n')
            f.write('<div class="container">\n')
            f.write('<h1 class="mt-5">IaC Security Scanner Results</h1>\n')

            f.write('<table id="results-table" class="table">\n<thead>\n<tr>\n')
            f.write('<th scope="col">Issue</th>\n<th scope="col">Severity</th>\n<th scope="col">Line Number</th>\n<th scope="col">Recommendation</th>\n')
            f.write('</tr>\n</thead>\n<tbody>\n')
            sorted_results = sorted(results, key=lambda x: (x.get('severity'), x.get('line_number')))

            for result in sorted_results:
                f.write('<tr>\n')
                f.write('<td>{}</td>\n'.format(result.get('issue')[:30]))
                f.write('<td>{}</td>\n'.format(result.get('severity')))
                f.write('<td>{}</td>\n'.format(result.get('line_number')))
                f.write('<td>{}</td>\n'.format(result.get('recommendation')))
                f.write('</tr>\n')
            f.write('</tbody>\n</table>\n')

            # Displaying the terra.tf file with highlighted lines using CodeMirror
            with open('terra.tf', 'r') as terra_file:
                f.write('<h2 class="mt-5">Code Editor</h2>\n')
                f.write('<textarea id="code" name="code" style="min-height: 400px; min-width: 800px;">')
                line_number = 1
                for line in terra_file:
                    line_class = ''
                    for result in results:
                        if result['line_number'] == line_number:
                            severity = result['severity']
                            if severity == 'high':
                                line_class = 'text-danger'
                            elif severity == 'medium':
                                line_class = 'text-warning'
                            elif severity == 'low':
                                line_class = 'text-success'
                            break
                        # Add CodeMirror editor for syntax highlighting
            f.write('<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.62.2/codemirror.min.js" integrity="sha512-Gp+8MJvDl2G5Qq/0S3mXg4bxBCj8gP5TAdlxM+/tdE+4HHl1H1QesuT0ZUxJxj3Z/aP5i0rsfK3cVr+bojuzdw==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>\n')
            f.write('<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.62.2/mode/terraform/terraform.min.js" integrity="sha512-kS3o1ce3aj6U1izxqVKRg0sfgjy1hHfGXe7/sR3Hq6f0B0Uh+kT0ffu63OyEPx9GzQlYzr9N0gijmGufMe5cTg==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>\n')
            f.write('<script>\n')
            f.write('var editor = CodeMirror.fromTextArea(document.getElementById("code"), {\n')
            f.write('mode: "terraform",\n')
            f.write('lineNumbers: true,\n')
            f.write('readOnly: true\n')
            f.write('});\n')
            f.write('</script>\n')

            # Display the table of results using DataTables plugin
            f.write('<table id="results-table" class="table">\n<thead>\n<tr>\n')
            f.write('<th scope="col">Issue</th>\n<th scope="col">Severity</th>\n<th scope="col">Line Number</th>\n<th scope="col">Recommendation</th>\n')
            f.write('</tr>\n</thead>\n<tbody>\n')
            sorted_results = sorted(results, key=lambda x: (x.get('severity'), x.get('line_number')))

            for result in sorted_results:
                f.write('<tr>\n')
                f.write('<td>{}</td>\n'.format(result.get('issue')[:30]))
                f.write('<td>{}</td>\n'.format(result.get('severity')))
                f.write('<td>{}</td>\n'.format(result.get('line_number')))
                f.write('<td>{}</td>\n'.format(result.get('recommendation')))
                f.write('</tr>\n')
            f.write('</tbody>\n</table>\n</div>\n')

            # Add DataTables plugin for sorting and filtering
            f.write('<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>\n')
            f.write('<script src="https://cdn.datatables.net/1.10.24/js/jquery.dataTables.min.js"></script>\n')
            f.write('<script>\n')
            f.write('$(document).ready(function() {\n')
            f.write('$("#results-table").DataTable();\n')
            f.write('});\n')
        


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

def unique_results(results):
    flattened_results = flatten(results)
    unique_results = list(set(tuple(sorted(d.items())) for d in flattened_results))
    unique_results = [dict(t) for t in unique_results]
    return unique_results
