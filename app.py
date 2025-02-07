from flask import Flask, render_template
import os
import shutil # For copying static assets
from data import pairs

app = Flask(__name__)

# List of pages to generate (add your template filenames here)
pages = [("index.html", "index.html")]  # (output filename, template file)


# Ensure the output folder exists
output_folder = "static_site"
os.makedirs(output_folder, exist_ok=True)

# Copy static files to the output folder
static_folder = "static"
output_static_folder = os.path.join(output_folder, "static")
shutil.copytree(static_folder, output_static_folder, dirs_exist_ok=True)

# Render the pages to static HTML files
with app.app_context():
    for output_file, template in pages:
        content = render_template(template)  # Render the template file
        with open(os.path.join(output_folder, output_file), "w", encoding="utf-8") as f:
            f.write(content)  # Save as static HTML

print("Static site generated successfully!")
