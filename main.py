from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import subprocess

app = Flask(__name__)
CORS(app)


@app.route('/', methods=["POST", "OPTION"])
def decision():
    html = "<h3>Hello you're here</h3>"
    content = request.json
    if content['lang'] == "c_cpp":
        resultstr = c(content)
        resultsend = {'result': resultstr}
        return jsonify(resultsend)
    elif content['lang'] == "python":
        resultstr = python(content)
        resultsend = {'result': resultstr}
        return jsonify(resultsend)
    elif content['lang'] == "java":
        resultstr = java(content)
        resultsend = {'result': resultstr}
        return jsonify(resultsend)
    elif content['lang'] == "c++":
        resultstr = cplus(content)
        resultsend = {'result': resultstr}
        return jsonify(resultsend)
    else:
        resultsend = {'result': "Not a supported language"}
        return jsonify(resultsend)

def c(content):
    code = open("code.c", "w")
    code.write(content['code'])
    code.close()

    subprocess.call("gcc code.c 2>&1 | tee  result.txt", shell=True)
    result = open('result.txt', 'r')
    resultstr = result.read()
    if len(resultstr) == 0:
        subprocess.call("./a.out > temp.txt", shell=True)
        result = open('temp.txt')
        resultstr = result.read()
        return resultstr
    else:
        return resultstr


def python(content):
    code = open("code.py", "w")
    code.write(content['code'])
    code.close()

    subprocess.call("python3 code.py 2>&1 | tee result.txt", shell=True)
    result = open('result.txt', 'r')
    resultstr = result.read()
    return resultstr


def java(content):
    code = open("code.java", "w")
    code.write(content['code'])
    code.close()

    subprocess.call("javac code.java 2>&1 | tee result.txt", shell=True)
    result = open('result.txt', 'r')
    resultstr = result.read()
    if len(resultstr) == 0:
        subprocess.call("java code > temp.txt", shell=True)
        result = open('temp.txt', 'r')
        resultstr = result.read()
        return resultstr
    else:
        return resultstr


def cplus(content):
    code = open("code.cpp", "w")
    code.write(content['code'])
    code.close()

    subprocess.call("g++ code.cpp 2>&1 | tee  result.txt", shell=True)
    result = open('result.txt', 'r')
    resultstr = result.read()
    if len(resultstr) == 0:
        subprocess.call("./a.out > temp.txt", shell=True)
        result = open('temp.txt', 'r')
        resultstr = result.read()
        return resultstr
    else:
        return resultstr

if __name__ == "__main__":
    app.run(host='0.0.0.0')
