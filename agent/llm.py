import json, random
from applibs.helpers import extract_city

def call_llm(prompt: str):
    """
    A fake LLM that *sometimes* returns a tool plan as a dict,
    sometimes malformed JSON, and sometimes a direct answer.
    """

    p = prompt.lower()

    if "weather" in p or "temperature" in p:
        # city = "paris" if "paris" in p else ("london" if "london" in p else "dhaka")
        city = extract_city(prompt)
        return {"tool": "weather", "args": {"city": city}}
    if "%" in p or "add" in p or any(op in p for op in ["+", "-", "*", "/"]):
        return {"tool": "calc", "args": {"expr": prompt}}
    if "who is" in p:
        name = prompt.split("who is", 1)[1].strip().rstrip("?")  # todo: IndexError: list index out of range
        return {"tool": "kb", "args": {"q": name}}
    # todo: first of all need to handle the short question and then pass them below
    if "convert" in p and "usd" in p and "eur" in p:
        return {
            "tool": "currency_converter",
            "args": {
                "exp": p,
                "to_currency": "EUR"
            }
        }
    return {"tool": "weather", "args": {"cty": "paris"}}

    # if "ada lovelace" in p:
    #     return "Ada Lovelace was a 19th-century mathematician and early computing pioneer."
    # return "I think you are asking about: " + prompt[:60]
