import string


def is_palindrome(text: str) -> bool:
    text = text.lower().replace(" ", "")

    return text == text[::-1]


print(is_palindrome("Kajak"))


def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("Liczba nie może być ujemna")

    if n == 0:
        return 0

    if n == 1:
        return 1

    a = 0
    b = 1

    for _ in range(2, n + 1):
        a, b = b, a + b

    return b


def count_vowels(text: str) -> int:
    text = text.lower()
    vowels = "aeiouyąęó"

    return sum(1 for char in text if char in vowels)


def calculate_discount(price: float, discount: float) -> float:
    if not (0 <= discount <= 1):
        raise ValueError("Zniżka musi być w zakresie od 0 do 100")

    return price * (1 - discount)


def flatten_list(nested_list: list) -> list:
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)

    return flat_list


def word_frequencies(text: str) -> dict:
    clean_text = text.lower()
    for char in string.punctuation:
        clean_text = clean_text.replace(char, "")

    words = clean_text.split()
    frequencies = {}

    for word in words:
        if word in frequencies:
            frequencies[word] += 1
        else:
            frequencies[word] = 1

    return frequencies


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True
