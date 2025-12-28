def calculate_discount(price: float, discount: float) -> float:
    if not (0 <= discount <= 1):
        raise ValueError("Zniżka musi być w zakresie od 0 do 100")

    return price * (1 - discount)
