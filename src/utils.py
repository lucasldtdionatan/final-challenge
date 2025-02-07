def generate_reference(prefix: str) -> str:
    import random
    import string
    
    max_random_chars = max(0, 8 - len(prefix))
    random_part = "".join(random.choices(string.ascii_uppercase + string.digits, k=max_random_chars))
    
    return f"{prefix}{random_part}"