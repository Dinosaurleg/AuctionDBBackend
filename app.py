from flask import Flask
from blizzardApiControllers.BlizzardAPIController import BlizzardAPIController

app = Flask(__name__)

bAPIController = BlizzardAPIController()

@app.route("/")
def hello():
	return "Hello World!"

@app.route("/realms")
def getRealms():
	return bAPIController.getRealms()

if __name__ == "__main__":
	app.run(debug=True)