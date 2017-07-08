from flask import Flask, request, jsonify
import subprocess
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def decision():
    html = "<h3>Hello you're gay</h3>"
    content = request.json
    if content['lang'] == "C":
        code = open("code.c", "w")
        codestring = content['code']
        code.write(codestring)
        code.close()
        returncode = subprocess.call("python print(hello world)", shell=True)
        print(content['code'])
    return jsonify(request.json)
#    return html

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
