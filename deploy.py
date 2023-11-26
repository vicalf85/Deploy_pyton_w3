from solcx import compile_standard, install_solc
import json
from web3 import Web3 
with open ("./SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()

install_solc("0.6.0")

#compire our solidity

compiled_sol = compile_standard (
    {
    "language":"Solidity",
    "sources":{"SimpleStorage.sol":{"content":simple_storage_file}},
    "settings":{
        "outputSelection":{
            "*":{"*":["abi","metadata","evm.bytecode","evm.sourceMap"]}
            }
        },

    },
    solc_version="0.6.0",
)
#print(compiled_sol)

with open("compiled_code.json","w") as file:
    json.dump(compiled_sol, file)

# get bytecode
bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"][
    "bytecode"
]["object"]

# get abi.
abi =compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]

#for conecting to ganache 

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
chain_id = 1337
my_address = "0x90F8bf6A479f320ead074411a4B0e7944Ea8c9C1"
private_key = "0x4f3edf983ac636a65a842ce7c78d9aa706d3b113bce9c46f30d7d21715b23b1d"

# create the contrat in python
SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)
# Get the latestest transaction
nonce = w3.eth.get_transaction_count(my_address)

print(nonce)

# 1. Build a transaction
# 2. Sign a transaction
# 3. Send a transaction

#transaction = SimpleStorage.constructor().get_transaction_count({"chainId":chain_id, "from":my_address, "nonce":nonce} )




# Construir la transacción
transaction = SimpleStorage.constructor().build_transaction(
    {
        "chainId": chain_id,
        "from": my_address,
        "gas": 2000000,  # Ajusta según tus necesidades
        "gasPrice": w3.to_Wei("50", "gwei"),  # Ajusta según tus necesidades
        "nonce": nonce,
    }
)
print(transaction)
# Firmar la transacción
#signed_transaction = w3.eth.account.sign_transaction(transaction, private_key)

# Enviar la transacción
#transaction_hash = w3.eth.send_raw_transaction(signed_transaction.rawTransaction)

#print("Transaction Hash:", transaction_hash)










