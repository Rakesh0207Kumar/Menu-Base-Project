#!/usr/bin/env python3

import cgi
import json
import sys
from googlesearch import search

print("Content-Type: application/json")
print()

try:
    form = cgi.FieldStorage()
    query = form.getvalue("query")

    if query:
        results = [result for result in search(query, num_results=5)]
        print(json.dumps(results))
    else:
        print(json.dumps({"error": "No query provided"}))
except Exception as e:
    print(json.dumps({"error": str(e)}))
    sys.stderr.write(str(e))
