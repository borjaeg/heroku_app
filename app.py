import os
from flask import Flask

# Inialization

app = Flask(__name__)
app.config.update(
	DEBUG = True
	)

# controllers
@app.route("/")
def hello():
	return "Hello from Python!"

# Launch

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='127.0.0.1', port=port)