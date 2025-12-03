# Blockchain +  Chatbot AI 🤖⛓️  

This project combines **OpenAI's GPT model** with an **Ethereum smart contract** to build a simple chatbot whose conversations are logged immutably on the blockchain.  
It demonstrates how AI + Blockchain can be used together for transparency, auditability, and trust.

---

## 🚀 Features  

- **AI Chatbot**: Uses OpenAI GPT model to respond to user queries.  
- **Blockchain Logging**: Stores each user and bot message on an Ethereum test network (Ganache).  
- **Smart Contract**: Solidity contract deployed automatically from Python script.  
- **Local Environment**: Works with Python virtual environment, Ganache, and dotenv for API keys.  

---

## 🛠️ Tech Stack  

- **Python 3.9+**  
- **Web3.py**  
- **Solcx (Solidity compiler)**  
- **OpenAI API (GPT-4o)**  
- **Ganache** (local Ethereum blockchain)  
- **dotenv** (to manage API keys)  

---

## 📂 Project Structure  

Blockchain_Chatbot/
│
├── main.py # Main Python script (deploys contract + runs chatbot)
├── .env # Contains your OpenAI API key
├── venv/ # Python virtual environment
└── README.md # This file

---

## ⚙️ Setup  

1. **Clone the repo & enter directory**  
   ```bash
   git clone <repo_url>
   cd Blockchain_Chatbot

2. **Create and activate a virtual environment**

    python3 -m venv venv
    source venv/bin/activate   # macOS/Linux
    # .\venv\Scripts\activate  # Windows PowerShell


3. **Install dependencies**

    pip install -r requirements.txt


(If you don’t have requirements.txt, manually install: web3 openai python-dotenv py-solc-x)

4. **Start Ganache**

    Download Ganache

    Run it and note the RPC server URL (default: http://127.0.0.1:7545)

5. **Set your OpenAI API key**

    Create a .env file in the project root:

    OPENAI_API_KEY=your_api_key_here


6. **Run the script**

    python main.py
