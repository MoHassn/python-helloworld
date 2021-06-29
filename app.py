from flask import Flask
from flask import json
import logging
app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG,
format='%(asctime)s %(message)s',
filename="app.log"
)
@app.route("/")
def hello():
    app.logger.info('Main request successfull')
    return "Hello World!"

@app.route("/status")
def status():
    # logging.debug("test")
    response = app.response_class(
        response = json.dumps({"result": "OK - healthy"}),
        status = 200,
        mimetype = "application/json"
    )
    app.logger.info('Status request successfull')
    return response

@app.route("/metrics")
def metrics():
    response = app.response_class(
        response = json.dumps({"status": "success", "code": 0, "data": {"UserCount":140,"UserCountActive":23}}),
        status=200,
        mimetype= "application/json"

    )
    app.logger.info('Metrics request successfull')
    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0')
