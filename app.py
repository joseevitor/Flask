from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    return "main menu from some application"

@app.route('/ekko')
def ekko():
    return "ekko is a champion from league of legends"

@app.route('/garen')
def garen():
    return "FOR DEMACIAAA"

@app.route('/')
def ():
    return ""



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

