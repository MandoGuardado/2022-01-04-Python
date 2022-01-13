#!/usr/bin/python3
"""By Chad Feeser | Alta3 Research
To use, try:
    curl localhost:5000/
    curl localhost:5000/atreides/
"""

from flask import Flask
app = Flask(__name__)

# if user sends HTTP GET to /
@app.route("/")
def index():
    return "In Frank Herbert's Dune, the Spice Melange makes space travel possible."

# if user sends HTTP GET to /atreides
@app.route("/atreides")
def atreides():
    return "As Dune opens, House Atreides is transitioning their rule to Arrakis, a desert planet."
    
# bind to all IP addresses port 5000
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

