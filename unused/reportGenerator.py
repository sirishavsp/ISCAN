
def generate_report(results):
    if results:
        results = unique_results(results)
        with open('report.html', 'w') as f:
            f.write('<!DOCTYPE html>\n<html>\n<head>\n<title>IaC Security Scanner Results</title>\n')
            f.write('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"')
            f.write(' integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm"')
            f.write(' crossorigin="anonymous">\n')
            f.write('</head>\n<body>\n')
            f.write('<div class="container">\n')
            f.write('<h1 class="mt-5">IaC Security Scanner Results</h1>\n')
              
            # Displaying the terra.tf file with highlighted lines
            with open('terra.tf', 'r') as terra_file:
                f.write('<pre><code>')
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
                    f.write('<span class="{}">{}</span>\n'.format(line_class, line))
                    line_number += 1
                f.write('</code></pre>\n')
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
            f.write('<script src="https://code.jquery.com/jquery-3.6.0.min.js"')
            f.write(' integrity="sha384-/pOZqwM7Iu/54un74V7RVd6aEtKrV7zgFpl1bNADtfU6FvsZ6kqMW3qQ4Ww0l5i5"')
            f.write(' crossorigin="anonymous"></script>\n')
            f.write('<script src="https://cdn.jsdelivr.net/npm/tablefilter@2.5.0/dist/tablefilter/tablefilter.js"')
            f.write(' integrity="sha384-DUTvG8al7VdYZCkQ2fHMI9eKbYS7IACNULfbZQ+o23hJ0cYwTIl1sAzs+Fr0XJh9"')
            f.write(' crossorigin="anonymous"></script>\n')
            f.write('<script>\n')
            f.write('var filtersConfig = {\n')
            f.write('    base_path: "https://cdn.jsdelivr.net/npm/tablefilter@2.5.0/dist/tablefilter/",\n')
            f.write('    auto_filter: {\n')
            f.write('        highlight_keywords: true,\n')
            f.write('        case_sensitive: false\n')
            f.write('    },\n')
            f.write('    col_0: "select",\n')
            f.write('    col_1: "select",\n')
            f.write('    col_2: "select",\n')
            f.write('    col_3: "select",\n')
            f.write('    alternate_rows: true,\n')
            f.write('    rows_counter: true,\n')
            f.write('    btn_reset: true,\n')
            f.write('    loader: true,\n')
            f.write('    mark_active_columns: true,\n')
            f.write('};\n')
            f.write('var tf = new TableFilter("results-table", filtersConfig);\n')
            f.write('tf.init();\n')
            f.write('</script>\n')
            f.write('</body>\n</html>\n')

    else:
        print('No results to generate report for.')

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
