from flask import Flask, request

app = Flask(__name__)


@app.route('/multiply/<int:number>')
def multiply(number: int):
    res = ""
    for i in range(1, 11):
        res += f"{number} * {i} = {number * i}\n"
    return f"<p>{res}</p>"


@app.route('/factorial')
def factorial():
    if request.args.get('num') is None:
        return "Number {num} is required"

    num = int(request.args.get('num'))
    print(num)
    rep = 1
    for i in range(1, num + 1):
        rep *= i
    return f"Factorial of {num} is {rep}."

@app.route('/even_odd/<int:n>')
def even_odd(n: int):
    if n % 2 == 0:
        return f"Number {n} is even"
    else:
        return f"Number {n} is odd"

@app.route('/calc')
def calc():
    a = request.args.get('a')
    b = request.args.get('b')
    op = request.args.get('op')

    if a is None or b is None or op is None:
        return "Non found"

    if op == 'add':
        return f"Result of {a} + {b} = {float(a) + float(b)}"
    elif op == 'sub':
        return f"Result of {a} - {b} = {float(a) - float(b)}"
    elif op == 'mult':
        return f"Result of {a} * {b} = {float(a) * float(b)}"
    elif op == 'div':
        if b == 0:
            return f"Result of {a} / {b} = NaN"
        return f"Result of  {a} / {b} = {float(a) / float(b)}"
    else:
        return "error"

@app.route('/primes')
def primes():
    limit = request.args.get('limit')
    if limit is None or not limit.isdigit() or int(limit) < 2:
        return "Provide a number greater than 1"
    if int(limit) > 6000:
        return "Provide a number less than 6000"

    count = int(limit) * 10 + 2

    nums = [ True for _ in range(count)]
    for i in range(2, count):
        if nums[i]:
            for j in range(i + i, count, i):
                print(f"{j}")
                nums[j] = False
    rep = []
    for i in range(1, count):
        if nums[i]:
            rep.append(i)

    print(len(rep[:int(limit)]))
    return f"<p>{rep[:int(limit)]}</p>"


if __name__ == '__main__':
    app.run(debug=True)