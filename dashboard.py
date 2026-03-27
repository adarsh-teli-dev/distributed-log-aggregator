from flask import Flask, render_template_string
import time

LOG_FILE = "server_logs.txt"

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
<title>Distributed Log Monitor</title>
<style>
body { font-family: monospace; background:black; color:#00ff88; }
h1 { color:#00ff88; }
#logs { white-space: pre-wrap; }
</style>
<meta http-equiv="refresh" content="2">
</head>
<body>
<h1>Distributed Log Aggregation Dashboard</h1>
<div id="logs">{{logs}}</div>
</body>
</html>
"""

@app.route("/")
def index():
    try:
        with open(LOG_FILE, "r") as f:
            logs = f.read()
    except:
        logs = "No logs yet..."
    return render_template_string(HTML_PAGE, logs=logs)


if __name__ == "__main__":
    print("Dashboard running at http://127.0.0.1:5000")
    app.run(port=5000)