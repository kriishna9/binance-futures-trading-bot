from bot.client import client
from bot.logging_config import logger
from binance.exceptions import BinanceAPIException


def place_market_order(symbol, side, quantity):
    try:
        logger.info(
            f"Market Order Request: {symbol} {side} {quantity}"
        )

        response = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )

        logger.info(f"Market Order Response: {response}")

        return response

    except BinanceAPIException as e:
        logger.error(f"Binance API Error: {e}")
        raise

    except Exception as e:
        logger.error(f"Unexpected Error: {e}")
        raise


def place_limit_order(symbol, side, quantity, price):
    try:
        logger.info(
            f"Limit Order Request: {symbol} {side} {quantity} @ {price}"
        )

        response = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )

        logger.info(f"Limit Order Response: {response}")

        return response

    except BinanceAPIException as e:
        logger.error(f"Binance API Error: {e}")
        raise

    except Exception as e:
        logger.error(f"Unexpected Error: {e}")
        raise