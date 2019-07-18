# Strip any HTML tags from a string
# For reading strings froma  web page

import re

def strip_html_tags(line):
    html_tag_re = re.compile(r'(<!--.*?-->|<[^>]*>)')
    stripped_line = html_tag_re.sub('', line)
    stripped_line = stripped_line.strip() # re.sub leaving whitespace at start and end
    return stripped_line