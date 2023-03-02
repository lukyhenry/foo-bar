from flask import Flask
import requests
app = Flask(__name__)

@app.route('/foo')
def hello():
    return '{"msg":"Hello from the foo microservice"}'

@app.route('/api/bar', methods=['GET'])
def get_message():
    r = requests.get('http://bar-service/bar', 
                 headers={'Accept': 'application/json'})

    print(f"Response: {r.json()}")
    return r.json()

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')