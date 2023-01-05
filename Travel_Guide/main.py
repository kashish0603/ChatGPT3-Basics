from flask import Flask, request, render_template
import openai

app = Flask(__name__)

openai.api_key = "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"

@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == "POST":
        select = request.form.get('place')
        check = request.form.getlist('check')
        type = ','.join(str(e) for e in check)
        prompt = "Places to visit in "+ select + "which are " + type
        response = openai.Completion.create(model="text-davinci-003",prompt=prompt,temperature=0.6,max_tokens=150,top_p=1,frequency_penalty=1,presence_penalty=1)
        jsonData = response["choices"]
        for x in jsonData:
            values = x.values()
        return list(values)[0]
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)