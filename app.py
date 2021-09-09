from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

from DomainSearch import verify_domains

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    if request.form["btn"] == "Single":
        return redirect(url_for("single"))

    if request.form["btn"] == "Bulk":
        return redirect(url_for("bulk"))

@app.route("/search/single", methods=["GET", "POST"])
def single():
    results = []
    if request.method == "POST":
        if request.form["btn"] == "Search":
            results = verify_domains([request.form["word"].strip()], request.form["tld"])
    return render_template("single.html", results=results)

@app.route("/search/bulk", methods=["GET", "POST"])
def bulk():
    results = []
    if request.method == "POST":
        words = [l.decode().strip() for l in request.files.get("text-file").read().split(b"\n")]
        results = verify_domains(words, request.form["tld"])

    return render_template("bulk.html", results=results)