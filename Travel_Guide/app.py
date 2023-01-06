from flask import Flask, request, render_template, jsonify
import openai


app = Flask(__name__)

openai.api_key = "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"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=["POST", "GET"])
def result():
    if request.method == "POST":
        fname = request.form.get('firstname')
        lname = request.form.get('lastname')
        full = fname + " " + lname
        select = request.form.get('place')
        check = request.form.getlist('check')
        type = ','.join(str(e) for e in check)
        city = request.form.get('city')
        if city == '':
            prompt = "Places to visit in "+ select + "which are " + type
        else:
            prompt = "Places to visit in "+ select + ", city " + city+ "which are " + type
        response = openai.Completion.create(model="text-davinci-003",prompt=prompt,temperature=0.6,max_tokens=150,top_p=1,frequency_penalty=1,presence_penalty=1)
        jsonData = response["choices"]
        for x in jsonData:
            v = x.values()
        result = {
            'output': list(v)[0],
        }
        result = {str(key): value for key, value in result.items()}
        # return jsonify(result=result)
        return render_template("result.html", result=result, name = full, place = select, check = check, type=type )

if __name__ == '__main__':
    app.run(debug=True)