import random
from filters import detect_mode

def generate_number():
    return random.randint(1,56)

def generate_combo(mode="ESTRUCTURA"):
    combo = set()

    while len(combo) < 6:
        combo.add(generate_number())

    combo = list(combo)

    if mode == "ESTRUCTURA":
        combo = sorted(combo)

        # fuerza 2 altos
        altos = [n for n in combo if n >= 41]
        while len(altos) < 2:
            combo[random.randint(0,5)] = random.randint(41,56)
            altos = [n for n in combo if n >= 41]

    return sorted(combo)

def generate_multiple(n=5, mode="ESTRUCTURA"):
    return [generate_combo(mode) for _ in range(n)]
