from flask import Flask, render_template, request, redirect

app = Flask(__name__)

todo = []

@app.route("/", methods=["GET", "POST"])
def index():
  # TODO: GET Method - Update this function to send the todo list to the html file
  return render_template("index.html")

  # TODO: POST Method - Update this function to add a new task to the list when the form is submitted


@app.route("/remove", methods=["POST"])
def remove():
  # TODO: POST Method - Update this function to remove task selected from the list
  return redirect("/")
