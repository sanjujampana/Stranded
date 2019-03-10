import smartcar
from flask import Flask, request, jsonify

client = smartcar.AuthClient(
    client_id="68224d34-50a2-47a2-a4d0-ee72a3a44410",
    client_secret="3b231c47-cca5-419e-892e-807f81328ef1",
    redirect_uri='http://localhost:8000/exchange',
    scope={
        'read_vehicle_info',
        'read_location',
        'read_odometer',
        'control_security'
    }
)

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
        auth_url = client.get_auth_url()
        return '''
            <h1>Hello World!</h1>
            <a href=%s>
                <button>Connect Car</button>
            </a>
        ''' %auth_url


@app.route('/callback', methods=['GET'])
def callback():
    code = request.args.get('code')
    access = client.exchange_code(code)

    print(access)

    return jsonify(access)


if __name__ == '__main__':
    app.run(port=8000)