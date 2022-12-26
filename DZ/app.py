from flask import Flask
import main
import requests
import matplotlib.pyplot as plt

app = Flask('fibonacci')


@app.route('/')
def start():
    return "Hello, write in address bar number of fibonacci element"

@app.route('/<int:n>')
def fib(n):
    return str(list(main.fibonacci(n)))

@app.errorhandler(404)
def page_not_found(e):
    return "Enter a number like ..../5 or ..../7 "

if __name__=="__main__":
    app.run(debug=True)