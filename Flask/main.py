from flask import Flask,request,jsonify

app = Flask(__name__)


@app.route('/add', methods=["GET","POST"])
def post():
    if request.method == "GET":
        return "Get"
    if request.method == "POST":
        data = request.json
        ans = 0
        print(request.json)
        for i in data['number']:
            ans += i
        print(ans)
        return jsonify({'ans': ans})



if __name__ == '__main__':
    app.run()
    # val()



