from flask import Flask, request

app = Flask(__name__)

@app.get('/welcome')
def say_welcome():
    """Returns simple "welcome" Greeting"""

    return """
    <html>
    <head>
        <title>Welcome!</title>
    </head>
    <body>
        <h1>Welcome!</h1>
    <body>
    </html>
    """

@app.get('/welcome/home')
def say_welcome_home():
    """Returns simple "welcome home" Greeting"""

    return """
    <html>
    <head>
        <title>Welcome home!</title>
    </head>
    <body>
        <h1>Welcome Home!</h1>
    <body>
    </html>
    """

@app.get('/welcome/back')
def say_welcome_back():
    """Returns simple "welcome back" Greeting"""

    return """
    <html>
    <head>
        <title>Welcome back!</title>
    </head>
    <body>
        <h1>Welcome back!</h1>
    <body>
    </html>
    """

