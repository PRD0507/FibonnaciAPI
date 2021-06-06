import flask
from flask import jsonify, request


class Fibonnaci:

    def __init__(self, n):
        self.n = n
        self.n1 = 0
        self.n2 = 1
        self.n3 = 1

        # Check if n is less than 0
        if self.n < 0:
            print("Incorrect input")

        else:
            for i in range(1, self.n):
                self.n3 = self.n1 + self.n2
                self.n1 = self.n2
                self.n2 = self.n3

    def next(self):
        self.n3 = self.n1 + self.n2
        self.n1 = self.n2
        self.n2 = self.n3

        return self.n2


app = flask.Flask(__name__)
app.config["DEBUG"] = True

dict_itr = {}

@app.route('/', methods=['GET'])
def home():
    return "<h1>Server Started</h1>" \
            "<p>Check the description provided in ReadMe to call different APIs</p>" \
            "<a href='http://127.0.0.1:5000/api/fibonnaci/all' target='_blank''>Link to check all the jumps/inputs given by researcher</a></br>" \



# A route to return all of the jump and associated fibonnaci value

@app.route('/api/fibonnaci/all', methods=['GET'])
def api_all():
    if not dict_itr:
        return "<h1>Fibonnaci series API has not been called a single time by Researcher</h1><p>The fibonnaci for a jump number has not been called even once by researcher</p><p>Refer the Fibonnaci_ReadMe file for API instructions</p>"
    else:
        return jsonify(dict_itr)


@app.route('/api/fibonnaci/', methods=['GET'])
def api_id():
    # Check if an jump value was provided as part of the URL.
    # If no jump value is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
        if id <= 0:
            return "Minimum value of jump should be >=1"
    else:
        return "Error: No id field provided. Please specify an id."

    # Call the Fibbonnaci class by passind jump value as id
    iterator = Fibonnaci(id)

    dict_itr[id] = iterator.next()

    #Returns the fibonnaci value associated for key which is the jump value inserted by the researcher as input

    return jsonify(dict_itr[id])

app.run()


