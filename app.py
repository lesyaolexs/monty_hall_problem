from flask import Flask, request, abort, jsonify
from tools import monty_hall_problem_check


app = Flask(__name__)

@app.route('/play', methods=['POST'])
def play():
    if not request.json or\
            not 'choose_option' in request.json and\
            not 'attempts' in request.json:
        abort(400)

    if request.json['choose_option'] == 'keep' or\
            request.json['choose_option'] == 'change':
        pass
    else:
        abort(400, 'choose_option can be `keep` or `change`')

    res = monty_hall_problem_check(request.json['choose_option'],
                                   request.json['attempts'])
    return jsonify(res)



if __name__ == '__main__':
    app.run()
