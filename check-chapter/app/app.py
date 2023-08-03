from flask import Flask, request
import os
import datetime

app = Flask(__name__)

chapter = os.environ.get("CHAPTER_VALUE", "1089")

@app.route("/")
def hello():
    return "Hello world"

@app.route("/check_chapter")
def check_chapter():

    @app.route("/write_datetime")
    def write_datetime():
        now = datetime.datetime.now()

        file_path = "D:/LiveCampus/II.Exercice/Docker-1/check-chapter/app/file.txt"

        with open(file_path, "a") as f:
            f.write(f"Received request at: {now}\n")

        return f"Time logged: {now}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)