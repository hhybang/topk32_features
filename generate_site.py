import os
import json
from jinja2 import Environment, FileSystemLoader

# Load metadata
with open("/home/hbang/data/sae/metadata.json", "r") as f:
    metadata = json.load(f)

# Setup Jinja2 environment to load templates from the 'templates' directory
env = Environment(loader=FileSystemLoader("templates"))

# Create directories for the site pages
site_dir = "site"
features_dir = os.path.join(site_dir, "features")
os.makedirs(features_dir, exist_ok=True)

# Load templates
feature_template = env.get_template("feature_template.html")
index_template = env.get_template("index_template.html")

# Generate a page for each feature that exists in metadata
for feature_idx, meta in metadata.items():
    html_content = feature_template.render(metadata=meta)
    feature_filename = os.path.join(features_dir, f"feature_{feature_idx}.html")
    with open(feature_filename, "w", encoding="utf-8") as f:
        f.write(html_content)

# Create the index page.
# The features in the index will be sorted numerically.
features_list = sorted([int(k) for k in metadata.keys()])
index_html = index_template.render(features=features_list)
with open(os.path.join(site_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(index_html)
