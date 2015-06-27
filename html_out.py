#!/usr/bin/env python
""" generate html output from dictionary of CVE finding data

    Copyright Mark Menkhus, May 2015
"""

import pystache
import re


def html_header_exists(input=None):
    """ test if html headers have previously been added
    """
    for line in input.splitlines():
        if re.search(r'DOCTYPE html', line, re.IGNORECASE):
            print (line)
            return True
    return False


def html_footer_exists(input=None):
    """ test if html footers have previously been added
    """
    for line in input.splitlines():
        if re.search(r'\</html\>', line, re.IGNORECASE):
            return True
    return False


def listtosentence(input=''):
    """ solve problem of getting a list converted into a sentence
        element
    """
    output = ''
    if isinstance(input, basestring):
        output = input
        return output
    else:
        if type(input) is list:
            for item in input:
                item = str(item)
                output += item.join(' ,')
            return output
    return input


def cve_table_content(packagename=None, falco_dict={}):
    """ accept findings in dictionary form
        start with style inline for simplicity
    """
    table_header = r'<h4>' + 'Known vulnerabilities found using search for ' 
    table_header += listtosentence(packagename) + ' in list of CPEs'+ r'</h4>'
    table_header += r'<h3>Finding notes:</h3>'
    table_header += r'<p id="editable" contenteditable=true>' 
    table_header += 'This line is an editable area for your dispensation notes'
    table_header += r', edit in browser as needed for your vulnerability response.' + r'</p>'
    table_column_header = """<table style="width:100%">\n<div id="CVE table">\
    <tr>\n<th>CVE#</th>\n<th>CVE vulnerability summary</th> \
    \n<th>Score</th>\n<th>Date</th>\n<th>CPE URI</th></tr>"""
    table = table_header + table_column_header
    table_body = ''
    table_footer = """</div>
</table>
"""
    for item in falco_dict:
        template_content = """<tr>\n<td>{{cve}}</td>\n<td>{{summary}}</td>\
            \n<td>{{cvss_base_score}}</td>\n<td>{{date}}</td> \
            \n<td>{{cpe}}</td>\n</tr>\n"""
        table_body += pystache.render(template_content, item)
    table += table_body
    table += table_footer
    return table


def html_wrap_content(content=''):
    """ wrap content in html headers
    """
    html_header = """<!DOCTYPE html>
<html lang="en">
<style>
    table, th, td {
    border: 1px solid black;
    border-collapse: collapse;
    }
    th, td {
        padding: 5px;
        text-align: left;
    }
    tr:nth-child(odd) {
        background-color: #BDBDBD;
    }
    tr:nth-child(even) {
        background-color: #F2F2F2;
    }
</style>
<head>
     <meta charset="utf-8">
    <title>Falco vulnerability findings</title>
</head>
<body>
"""
    html_footer = """
</body>
</html>
"""
    out = ''
    if not html_header_exists(content):
        out += html_header
        out += content
    else:
        out += content
    if not html_footer_exists(content):
        out += html_footer
    else:
        return out
    return out
