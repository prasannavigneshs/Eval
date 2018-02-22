import sys
import contextlib
from io import StringIO
from flask import Flask, request, redirect, render_template, url_for

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        post_code = request.form['code']
        f = open('code.txt', 'w')
        f.write(post_code)
        f.close()
        return redirect(url_for('get_code'))
    else:
        post_code = "hii"
        f = open('code.txt', 'w')
        f.write(post_code)
        f.close()
        return redirect(url_for('get_code'))


@app.route('/getcode')
def get_code():
    code_from_file = get_code_from_file()
    raw_code = code_from_file.split()
    code = ""
    keywords = ['else:', 'elif:']
    control_statements = ['return', 'break', 'continue', 'pass']
    c = 0
    for i in raw_code:
        if i == '!!':
            code += '\n'
        elif i[-1] == ':' and i not in keywords and i not in control_statements:
            code += i
            c += 1
        elif c > 0 and i not in keywords and i not in control_statements:
            code += ('\t'*c)+i
            code += " "
        elif i in keywords:
            c -= 1
            code += ('\t'*c) + i
            code += " "
            c += 1
        elif i in control_statements:
            code += ('\t' * c) + i
            code += " "
            c -= 1
        else:
            code += i
            code += " "
        f = open('code.txt', 'w')
        f.write(code)
        f.close()

    return redirect(url_for('python'))


@app.route('/result', methods=['POST'])
def result():
    code = request.form['code']
    f = open('code.txt', 'w')
    f.write(code)
    f.close()
    output = compute_result(code)
    return render_template('index.html', code=code, op=True, output=output)


@app.route('/python')
def python():
    return render_template('index.html', code=get_code_from_file())


@contextlib.contextmanager
def stdoutio(stdout=None):
    old = sys.stdout
    if stdout is None:
        stdout = StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old


def compute_result(code):
    with stdoutio() as s:
        try:
            exec(code)
        except Exception as e:
            print(e)

    with open('filename.txt', 'w') as f:
        print(s.getvalue(), file=f)

    res = ""

    f = open('filename.txt', 'r')
    l = f.readline()
    while l != "":
        if len(l) > 1:
            res += l
        l = f.readline()
    f.close()

    return res


def get_code_from_file():

    res = ""

    f = open('code.txt', 'r')
    l = f.readline()
    while l != "":
        if len(l) > 1:
            res += l
        l = f.readline()
    f.close()

    return res


if __name__ == '__main__':
    app.run(host='0.0.0.0')
