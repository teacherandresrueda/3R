def classify_number(n):
    if n <= 12:
        return "bajo"
    elif n <= 20:
        return "bajo-medio"
    elif n <= 30:
        return "medio"
    elif n <= 40:
        return "medio-alto"
    else:
        return "alto"

def count_ranges(combo):
    counts = {"bajo":0,"bajo-medio":0,"medio":0,"medio-alto":0,"alto":0}
    for n in combo:
        counts[classify_number(n)] += 1
    return counts

def is_structure(combo):
    altos = [n for n in combo if n >= 41]
    return len(altos) >= 2

def has_cluster(combo):
    combo = sorted(combo)
    for i in range(len(combo)-1):
        if abs(combo[i] - combo[i+1]) <= 2:
            return True
    return False

def detect_mode(combo):
    if is_structure(combo) and has_cluster(combo):
        return "ESTRUCTURA"
    else:
        return "DISPERSION"
