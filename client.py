from web3 import Web3, HTTPProvider
import ipfsapi
import json

web3 = Web3(HTTPProvider('http://localhost:7545'))

contractRawAccount = '0xc1160e960b097dc5b593a566bae935c1b45301c4'
contractAccount = Web3.toChecksumAddress(contractRawAccount)

with open("build/contracts/NotaryOffice.json") as f:
    info_json = json.load(f)
    
    abi = info_json["abi"]
    contract = web3.eth.contract(address=contractAccount, abi=abi)

    # DOCUMENT HASH
    documentHash = 'hereIsTheHashOfDocument'

    # DOCUMENT OWNER ADDRESS AND PRIVATE KEY
    owner_address = Web3.toChecksumAddress(
                        '0x37b9590e14ce8322c301150bd8146ec76d9fdbc9')

    owner_pk = ('0x4f58381a1a46e925b4aef31771a9abc2951c2'
                'fd5861d789570eef82dcf64675e')


    # NOTARY ADDRESS AND PRIVATE KEY
    notary_address = Web3.toChecksumAddress(
                         '0x490adae81934b5520b6815b1bbd4ee2c86ef6b46')
    notary_pk = ('0xa2ffafc14d85e4e67808f1186b0d12710265d5d97ca0'
                 'b6772c774c2d14c170fb')

        
    nonce_owner = web3.eth.getTransactionCount(owner_address)
    _tx = contract.functions.registerDocument(documentHash)
    tx = _tx.buildTransaction({'nonce': nonce_owner})

    signed_tx = web3.eth.account.signTransaction(tx, private_key=pk_sender)
    web3.eth.sendRawTransaction(signed_tx.rawTransaction)
