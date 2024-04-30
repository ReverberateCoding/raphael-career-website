from flask import Flask, render_template

app = Flask(__name__)

flowers = [
    {
        "name": "Mummy",
        "price": "$99.99",
        "image_link": "static/images/flower_images/flower_image2.jpg",
    },
    {
        "name": "Hello",
        "price": "$34.99",
        "image_link": "static/images/flower_images/flower_image3.jpg",
    },
]
@app.route("/")
def hello_world():
    return render_template('home.html', flowers = flowers)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)