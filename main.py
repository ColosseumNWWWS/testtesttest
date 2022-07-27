from flask import *

app = Flask(__name__)
app.secret_key = ',uzO2a4>zIBsN<@U2R,j'

@app.route("/")
def index():
    return "Ciao gigi"

if __name__ == "__main__":
    app.run("0.0.0.0", 80)
