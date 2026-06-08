Binance Futures Testnet Trading Bot

Features

* Place Market Orders
* Place Limit Orders
* BUY and SELL support
* Logging of API requests and responses
* Error handling for API and user input errors
* CLI-based interaction

Requirements

* Python 3.x
* Binance Futures Testnet Account
* API Key and Secret Key

Installation

pip install -r requirements.txt

Configuration

Create a .env file:

API_KEY=your_api_key
API_SECRET=your_api_secret

Run

python3 -m bot.cli

Example

Order Type: MARKET
Symbol: BTCUSDT
Side: BUY
Quantity: 0.001

Order Type: LIMIT
Symbol: BTCUSDT
Side: SELL
Quantity: 0.001
Price: 65000

Project Structure

trading_bot/
│
├── bot/
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   ├── logging_config.py
│   ├── cli.py
│   └── init.py
│
├── logs/
├── .env
├── README.md
└── requirements.txt

Assumptions

* Only Binance Futures Testnet is supported.
* Only USDT-M Futures contracts are used.
