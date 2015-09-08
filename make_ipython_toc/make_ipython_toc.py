"""Build a table of contents using markdown headers.

This is a very simple script that produces a table of contents that can be
added to a IPython notebook. The table is produced by looking for all markdown
headers in a notebook (# signs). The table follows the proper nesting so

#Header1
##header2

will produce

#Table of Contents
1. [Header1](http://localhost:8888/notebooks/notebook_name/#header1]
    * [Header2](http://localhost:8888/notebooks/notebook_name/#header2]
"""
import sys
import json

def headers_to_table(markdown_headers):
    return None

markdown_headers = []
with open(sys.argv[1]) as notebook_handler:
    notebook_data = json.load(notebook_handler)
    for cell in notebook_data["cells"]:
        if cell["cell_type"] == "markdown":
            for line in cell["source"]:
                if "#" in line:
                    markdown_headers.append(line)

print(markdown_headers)

