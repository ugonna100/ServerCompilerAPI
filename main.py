from flask import Flask, request, jsonify
import subprocess
app = Flask(__name__)


@app.route('/', methods=['POST'])
def decision():
    html = "<h3>Hello you're here</h3>"
    content = request.json
    if content['lang'] == "C":
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

def c(content):
    code = open("code.c", "w")
    code.write(content['code'])
    code.close()

    subprocess.call("gcc code.c > result.txt", shell=True)
    result = open('result.txt', 'r')
    resultstr = result.read()
    if len(resultstr) == 0:
       # print("compiler has no errors")
        subprocess.call("./a.out > temp.txt", shell=True)
        result = open('temp.txt')
        resultstr = result.read()
        return resultstr
    else:
       # print("compiler has text...", resultstr)
        return resultstr


def python(content):
    code = open("code.py", "w")
    code.write(content['code'])
    code.close()

    subprocess.call("python3 code.py > result.txt", shell=True)
    result = open('result.txt', 'r')
    resultstr = result.read()
    return resultstr


def java(content):
    code = open("code.java", "w")
    code.write(content['code'])
    code.close()

    subprocess.call("javac code.java > result.txt", shell=True)
    result = open('result.txt', 'r')
    resultstr = result.read()
    if len(resultstr) == 0:
        print("Compiling...")
        subprocess.call("java code > temp.txt", shell=True)
        result = open('temp.txt', 'r')
        resultstr = result.read()
        return resultstr
    else:
        return resultstr

if __name__ == "__main__":
    app.run(host='0.0.0.0')
