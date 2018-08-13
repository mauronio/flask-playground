import db_query
import json

OER_QUERY_NAME = 'OER_SERVICES'
JSON_OUT_FORMAT = 'json'
HTML_OUT_FORMAT = 'html'

def get_html_formatted_results(p_query_name, results, p_query_params):

    html_text = """
        <!DOCTYPE html>
        <html>
        <body>
    """

    html.text += "<h1>" + p_query_name + "</h1>\n"

    for param_key, param_value in p_query_params:
        html.text += "<p>" + param_key + " = " + param_value + "</p>\n"

    html_text += """
        <table>
            <tr>
    """

    for col_key, col_desc in results['columns']:
        html_text += "<th>" + col_desc + "/th>"

    html_text += "</tr>\n"

    for row in results['rows']:
        html_text += "<tr>\n"
        for col_key, col_value in row:
            html_text += "<td>" + col_value + "</td>"
        html_text += "</tr>\n"

    html_text += "</table>\n"

    html_text += """
    </body>
    </html>
    """

    return html_text


def get_results(p_query_name, p_out_format = JSON_OUT_FORMAT, p_query_params):

    results = None
    formatted_results = ''

    if p_query_name == OER_QUERY_NAME:
        results = db_query.get_results()

    if not results is None:

        if p_out_format == JSON_OUT_FORMAT:

            formatted_results = json.dumps(results, indent=4) 

        if p_out_format == HTML_OUT_FORMAT:

            formatted_results = get_html_formatted_results(p_query_name, results, p_query_params)

    return formatted_results
    

