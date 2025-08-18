from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

CLIENT_ID = "YOUR_CLIENT_ID"
CLIENT_SECRET = "YOUR_CLIENT_SECRET"

def get_access_token():
    url = "https://api-m.sandbox.paypal.com/v1/oauth2/token"
    headers = {"Accept": "application/json", "Accept-Language": "en_US"}
    data = {"grant_type": "client_credentials"}
    response = requests.post(url, headers=headers, data=data, auth=(CLIENT_ID, CLIENT_SECRET))
    return response.json()["access_token"]

@app.route("/")
def index():
    return render_template("index.html", client_id=CLIENT_ID)

@app.route("/create-order", methods=["POST"])
def create_order():
    token = get_access_token()
    url = "https://api-m.sandbox.paypal.com/v2/checkout/orders"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    body = {
        "intent": "CAPTURE",
        "purchase_units": [{
            "amount": {
                "currency_code": "USD",
                "value": "10.00"
            }
        }]
    }
    response = requests.post(url, headers=headers, json=body)
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(debug=True)

