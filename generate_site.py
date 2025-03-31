import os
import json
from jinja2 import Environment, FileSystemLoader

# Load metadata
with open("metadata_32.json", "r") as f:
    metadata = json.load(f)

features = sorted(metadata.values(), key=lambda x: int(x["feature_idx"]))

# Set up the Jinja2 environment to look for templates in the "templates" folder.
env = Environment(loader=FileSystemLoader("templates"))
template = env.get_template("index_template.html")

# Render the template with the features list
html_output = template.render(features=features)

# Write the output to an index.html file in the same folder.
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_output)

print("Site generated successfully! Open index.html in your browser to view the site.")
