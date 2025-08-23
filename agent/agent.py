from .llm import call_llm
from . import tools

def answer(q: str):
    plan = call_llm(q)
    # {"tool": "weather", "args": {"city": city}}
    if plan and isinstance(plan, dict) and "tool" in plan:
        if plan["tool"] == "calc":
            return tools.evaluate(plan["args"]["expr"])
        elif plan["tool"] == "weather":
            city = plan["args"]["city"]
            t = tools.temp(city)
            return f"{t} C"
        elif plan["tool"] == "kb":
            return tools.kb_lookup(plan["args"]["q"])
        elif plan["tool"] == "currency_converter":
            return tools.currency_converter(plan["args"]["exp"])

    return str(plan)
