from flask import Flask, request

app = Flask(__name__)

@app.route("/add")
def add():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    result = a + b
    return str(result)

@app.route("/sub")
def sub():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    result = a - b
    return str(result)

@app.route("/mult")
def mult():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    result = a * b
    return str(result)

@app.route("/div")
def div():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    result = a / b
    return str(result)

@app.route("/math/<operation>")
def math(operation):
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)


    if operation == 'add':
        result = a + b
    elif operation == 'sub':
        result = a - b
    elif operation == 'mult':
        result = a * b
    elif operation == 'div':
        if b != 0:
            result = a / b
        else:
            return "Division by zero is not allowed."
    else:
        return "Invalid operation. Supported operations: add, sub, mult, div"

    return str(result)