import pandas as pd
import random

# ---------------- CARGAR DATOS ----------------
def cargar_datos():
    melate = pd.read_csv("melate.csv")
    revancha = pd.read_csv("revancha.csv")
    revanchita = pd.read_csv("revanchita.csv")

    return melate, revancha, revanchita


# ---------------- FEATURES ----------------
def agregar_features(df):
    nums = ["n1","n2","n3","n4","n5","n6"]

    df["suma"] = df[nums].sum(axis=1)
    df["pares"] = df[nums].apply(lambda x: sum(x % 2 == 0), axis=1)
    df["rango"] = df[nums].max(axis=1) - df[nums].min(axis=1)

    df["modo"] = df["rango"].apply(lambda x: "estructura" if x < 25 else "dispersion")

    return df


# ---------------- DETECTAR MODO ----------------
def detectar_modo_actual(df):
    ultimos = df.tail(5)
    conteo = ultimos["modo"].value_counts()

    return conteo.idxmax()


# ---------------- GENERADOR INTELIGENTE ----------------
def generar_combinacion(modo):
    numeros = list(range(1, 57))

    if modo == "estructura":
        # números cercanos
        base = random.randint(1, 40)
        combinacion = sorted(random.sample(range(base, base+15), 6))
    else:
        # números dispersos
        combinacion = sorted(random.sample(numeros, 6))

    adicional = random.randint(1, 56)

    return combinacion, adicional


# ---------------- MOTOR PRINCIPAL ----------------
def motor_3r():
    melate, revancha, revanchita = cargar_datos()

    melate = agregar_features(melate)
    revancha = agregar_features(revancha)
    revanchita = agregar_features(revanchita)

    modo_melate = detectar_modo_actual(melate)
    modo_revancha = detectar_modo_actual(revancha)

    print("🧠 Modo actual Melate:", modo_melate)
    print("🧠 Modo actual Revancha:", modo_revancha)

    # lógica cruzada
    if modo_melate == "estructura":
        modo_objetivo = "dispersion"
    else:
        modo_objetivo = "estructura"

    print("🎯 Modo objetivo:", modo_objetivo)

    combinacion, adicional = generar_combinacion(modo_objetivo)

    print("\n🎰 COMBINACIÓN SUGERIDA:")
    print("Números:", combinacion)
    print("Adicional:", adicional)


if __name__ == "__main__":
    motor_3r()
