import os
from openai import OpenAI
from web3 import Web3
from solcx import compile_source, install_solc
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY "] = os.getenv("OPENAI_API_KEY")

##Connect to Ganache Server##

ganache_url = "http://127.0.0.1:7545"
w3 = Web3(Web3.HTTPProvider(ganache_url))

if not w3.is_connected():
    raise Exception("Failed to connect to Ganache server")

# Set default account (first account from Ganache)
w3.eth.default_account = w3.eth.accounts[0]

# Solidity smart contract as string
contract_source_code = '''
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract ChatLog {
    event MessageLogged(address indexed sender, string message, uint256 timestamp);

    function logMessage(string calldata message) public {
        emit MessageLogged(msg.sender, message, block.timestamp);
    }
}
'''

## Compile the solidity contract ##

install_solc('0.8.0')

compiled_sol = compile_source(contract_source_code, solc_version='0.8.0')

contract_id, contract_interface = compiled_sol.popitem()

## Extract the bytecode and ABI ##

bytecode = contract_interface['bin']
abi = contract_interface['abi']

## Deploy this contract to Ganache ##

ChatLog = w3.eth.contract(abi = abi, bytecode = bytecode)
print("Deploying chatbot contracts.......")
tx_hash = ChatLog.constructor().transact()
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
contract_address = tx_receipt.contractAddress
print("Contract deployed at this address: ", contract_address)

## Create a Contract instance to interact with ##

chatlog_contract = w3.eth.contract(address= contract_address, abi=abi)

## Define the function to log messages and get chat responses from LLM

def log_message_on_blockchain(message):
    try:
        tx_hash = chatlog_contract.functions.logMessage(message).transact()
        tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        print("Logged on BlockChain. TxHash: ", tx_hash.hex())
    except Exception as e:
        print("Error logging on Blockchain: ", e)

def get_chatbot_response(user_message):
    try:
        client = OpenAI()
        response = client.chat.completions.create(
            model = "gpt-4o",
            messages = [
                {"role" : "system", "content": "you are a helpful chatbot."},
                {"role" : "user", "content" : user_message}
            ],
            max_tokens=256
        )
        reply = response.choices[0].message.content.strip()
        return reply
    
    except Exception as e:
        print("Error getting response from LLM: ", e)
        return "I am having trouble processing that."

## Driver Code ##

def main():
    print("Welcome to Blockchain and AI simple chatbot")
    print("type 'exit or 'quit' to end the chatbot.\n")

    while True:
        user_message = input("You: ")
        if user_message.lower() in ["exit", "quit"]:
            print("Goodbye")
            break

        log_message_on_blockchain(f"User: {user_message}")
        bot_response = get_chatbot_response(user_message)
        print("Bot: ", bot_response)

        log_message_on_blockchain(f"Bot: {bot_response}")

if __name__ == "__main__":
    main()    