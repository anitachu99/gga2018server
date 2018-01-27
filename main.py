from flask import Flask, render_template, redirect
app = Flask(__name__)


@app.route('/')
def index():
    """
    Returns the index of the function.
    """
    return "TODO"


if __name__ == '__main__':
  app.run()
