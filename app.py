from datetime import datetime
from flask import Flask, render_template_string

app = Flask(__name__)

# Basic HTML template using Jinja2 syntax
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #f4f4f4;
        }
        header {
            background: #007BFF;
            color: white;
            padding: 20px;
            text-align: center;
        }
        .container {
            width: 80%;
            margin: 40px auto;
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        footer {
            margin-top: 30px;
            text-align: center;
            padding: 15px;
            background: #222;
            color: white;
        }
        .btn {
            display: inline-block;
            padding: 10px 20px;
            background: #007BFF;
            color: white;
            text-decoration: none;
            border-radius: 5px;
        }
        .btn:hover {
            background: #0056b3;
        }
    </style>
</head>
<body>

<header>
    <h1>{{ title }}</h1>
</header>

<div class="container">
    <h2>Hello, World!</h2>

    <p>This page was generated using Python & Flask.</p>

    <p>
        Current Date & Time:
        <strong>{{ current_time }}</strong>
    </p>

    <a href="#" class="btn">Learn More</a>
</div>

<footer>
    &copy; {{ current_year }} My Website
</footer>

</body>
</html>
"""

@app.route("/")
def home():
    title = "Welcome"
    now = datetime.now()
    current_time = now.strftime("%B %d, %Y, %I:%M %p")
    current_year = now.year
    
    return render_template_string(
        HTML_TEMPLATE, 
        title=title, 
        current_time=current_time, 
        current_year=current_year
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)