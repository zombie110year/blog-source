#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import getopt
import sys
import re

help_doc = """\
Usage:  insert_local_text -i <input-file> -o <output-file>
        * to Convert pure text from input-file to html document
        * in a <pre><code> element.
OR:     insert_local_text -h
        * to Get the help document.
"""

args = sys.argv[1:]
options, arguments = getopt.getopt(args, shortopts="i:o:h")
for key, value in options:
    if key == "-i":
        input_file = value
        continue
    elif key == "-o":
        output_file = value
        continue
    elif key == "-h":
        print(help_doc)
        exit(0)

origin_file = re.findall(r"(\\{1}assert\\{1}[\S]+)$", input_file)[0]
origin_file = origin_file.replace("\\", "/")
html_template = """\
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
<a href="/public%s">Origin-File</a>
    <pre><code>
%s
</code></pre>
</body>
</html>
"""

with open(input_file, "r", encoding="utf-8") as read_file:
    read_text = read_file.read()

with open(output_file, "wb") as write_file:
    write_file.write((html_template%(origin_file, read_text)).encode("utf-8"))