from flask import Flask
from dotenv import load_dotenv
import os

app = Flask(__name__)

@app.route("/")
def index():

    username = os.getenv("USER")
    email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")

    print(username, email, password)

    return "<h1>Mi primera app Flask deployada en Render <br>Nombre: {} <br>Email: {} <br>Password:  {}</h1><hr><img src='https://project-static-assets.s3.amazonaws.com/APISpreadsheets/ProgrammingMemes/JSForKids.jpg'>".format(username, email, password)

def status_404(error):
    return "<h1>Página no encontrada</h1>", 404

if __name__ == "__main__":
    app.register_error_handler(404, status_404)
    app.run()