
from flask import Flask, render_template, request

from web3 import Web3

web3 = Web3(Web3.HTTPProvider('https://goerli.infura.io/v3/9bfea926aefa4ae7b9137fb9e2fb81d4'))




app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods =['GET', 'POST'])
def main():
    if request.method=='POST':
        from_account = str(request.form['account'])

        to_account= '0x8c218E3CE341d04cc9A59Fa61e8cc442A99A9109'

        private_key = str(request.form['pkey'])


        address1 = web3.toChecksumAddress(from_account)
        address2 = web3.toChecksumAddress(to_account)

        nonce = web3.eth.getTransactionCount(address1)
        amount = request.form['amount']
        tx = {
            'nonce': nonce,
            'to' : address2,
            'value': web3.toWei(str(amount),'ether'),
            'gas': 21000,
            'gasPrice': web3.toWei(40,'gwei')

        }

        signed_tx = web3.eth.account.sign_transaction(tx,private_key)

        tx_transaction = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        return render_template('hola.html')
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)

