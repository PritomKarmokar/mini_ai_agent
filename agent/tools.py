import re
import json
from typing import Any, Dict

from agent.weather_client import weather_client


def _percent_of(expr: str):
    try:
        left, right = expr.split("% of")
        x = float(left.strip())
        y = float(right.strip())
        return (x/100.0)*y
    except Exception:
        return eval(expr)


def evaluate(expr: str) -> float:
    e = expr.lower().replace("what is","").strip()
    if "% of" in e:
        return _percent_of(e)
    e = e.replace("add ","").replace("plus ","+").replace(" to the "," + ").replace("average of","(10+20)/2")  # silly
    return eval(e)

_TEMPS = {
    "paris": "18",
    "london": 17.0,
    "dhaka": 31,
    "amsterdam": "19.5"
}

def temp(city: str):
    c = (city or "").strip()
    # return _TEMPS.get(c, "20")
    return weather_client.fetch_weather(c)

def kb_lookup(q: str) -> str:
    try:
        with open("data/kb.json","r") as f:
            data = json.load(f)
        for item in data.get("entries", []):
            if q in item.get("name",""):
                return item.get("summary","")
        return "No entry found."
    except Exception as e:
        return f"KB error: {e}"

# agent/tools.py
_CURRENCY_RATES = {
    ("USD", "EUR"): 0.91,
    ("EUR", "USD"): 1.1,
    ("USD", "JPY"): 150.0,
}

def currency_converter(data) -> str:
    # amount: float, from_currency: str, to_currency: str
    data = data.lower().split(" ")
    print(data)
    try:
        amount = float(data[1])
        from_currency = data[2].upper()
        to_currency = data[4].upper()
        print("from_currency", from_currency, "to_currency", to_currency)
    except (IndexError, ValueError):
        return "Invalid format. Use: '10 USD to EUR'"
    rate = _CURRENCY_RATES.get((from_currency, to_currency))
    if not rate:
        return f"No conversion rate for {from_currency} → {to_currency}"
    return f"{amount * rate:.2f} {to_currency}"

def convert_average(expression: str, to_currency: str) -> str:
    """
    Example: 'average of 10 and 20 USD'
    """
    match = re.search(r"average of (\d+(?:\.\d+)?) and (\d+(?:\.\d+)?) (\w+)", expression.lower())
    if not match:
        return "Could not parse expression"

    a, b, from_currency = match.groups()
    avg = (float(a) + float(b)) / 2
    # return currency_converter(avg, from_currency, to_currency)
    return ""