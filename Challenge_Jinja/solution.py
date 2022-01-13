#!/usr/bin/python3

from flask import Flask
from flask import render_template

app = Flask(__name__)

app.secret_key = "random random RANDOM!"


@app.route("/")
@app.route("/hosts")
def index():
    groups = [{"hostname": "hostA", "ip": "192.168.30.22", "fqdn": "hostA.localdomain"},
              {"hostname": "hostB", "ip": "192.168.30.33", "fqdn": "hostB.localdomain"},
              {"hostname": "hostC", "ip": "192.168.30.44", "fqdn": "hostC.localdomain"}]
    return render_template("hosts.html.j2", grp=groups)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
