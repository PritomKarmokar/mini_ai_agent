def extract_city(prompt: str) -> str:
    p = prompt.lower()
    if " in " in p:
        return p.split(" in ")[-1].strip(" ?!.")
    return "paris"  # fallback
