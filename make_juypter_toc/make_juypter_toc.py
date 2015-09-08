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

def headers_to_table(markdown_headers, notebook_name):
    """Produces a markdown table of contents from markdown headers.

    This function uses a two pass solution to turn markdown headers into a
    table of contents. The first pass strips one # from every header and the
    second pass turns all remaining # into spaces. Then the function produces
    markdown links spaced in table formats.
    """
    if markdown_headers is None:
        return None

    # First pass just strips #
    stripped_headers = []
    for header in markdown_headers:
        # While we're here let's clean up the data.
        header = header.replace("\n", "")
        # Third argument is max replace>
        stripped_headers.append(header.replace("#", "", 1))

    # Second pass Produces actual table of contents.
    table_of_contents = []
    for header in stripped_headers:
        # Using the fact that we know markdown headers have to start on the
        # left side.
        pound_stripped_header = header.lstrip("#")
        nesting_count = len(header) - len(pound_stripped_header)

        # Remove spaces from URL. All spaces are convered to - so -- is valid.
        href_header = pound_stripped_header.replace(" ", "-")
        # Finally constructing toc line
        toc_line = (u"{spaces}* [{header_name}]" \
            "(http://localhost:8888/{notebook_name}/#{href_header})").format(
                spaces=" " * (nesting_count * 4),
                header_name=pound_stripped_header,
                notebook_name=notebook_name,
                href_header=href_header,)
        table_of_contents.append(toc_line)

    return table_of_contents

def get_headers():
    markdown_headers = []
    with open(sys.argv[1]) as notebook_handler:
        notebook_data = json.load(notebook_handler)
        for cell in notebook_data["cells"]:
            if cell["cell_type"] == "markdown":
                for line in cell["source"]:
                    line = line.strip()
                    if line.startswith("#"):
                        markdown_headers.append(line)
    return markdown_headers

if __name__ == "__main__":
    headers = get_headers()
    toc = headers_to_table(headers, argv[2])
    for line in toc:
        print(line)
