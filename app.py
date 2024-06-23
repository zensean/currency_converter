from flask import Flask, request, jsonify
from services.currency_exchange_service import CurrencyExchangeService

app = Flask(__name__)

currencies = {
    "TWD": {
        "TWD": 1,
        "JPY": 3.669,
        "USD": 0.03281
    },
    "JPY": {
        "TWD": 0.26956,
        "JPY": 1,
        "USD": 0.00885
    },
    "USD": {
        "TWD": 30.444,
        "JPY": 111.801,
        "USD": 1
    }
}

exchange_service = CurrencyExchangeService(currencies)

@app.route('/convert', methods=['GET'])
def convert_currency():
    source = request.args.get('source')
    target = request.args.get('target')
    amount = request.args.get('amount')

    if not source or not target or not amount:
        return jsonify({"msg": "Missing parameters"}), 400

    try:
        amount = float(amount.replace(',', ''))
    except ValueError:
        return jsonify({"msg": "Invalid amount"}), 400

    result = exchange_service.convert(source, target, amount)
    if result is None:
        return jsonify({"msg": "Currency not supported"}), 400

    return jsonify({"msg": "success", "amount": f"{result:,.2f}"})

if __name__ == '__main__':
    app.run(debug=True)
