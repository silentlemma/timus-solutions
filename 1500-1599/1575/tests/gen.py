"""One test from a seed and a mode: questions about the 70 stations of the
map. Mode 1 asks every ordered pair once in random order, mode 2 asks 4900
random pairs, mode 3 asks a few."""

import random
import sys

STATIONS = """1905_year_square 7_klyuchey Akademicheskaya Aviatsionnaya Bakinskih_Komissarov
Bazhovskaya Botanicheskaya Central_stadium China_town Chkalovskaya City Dinamo
Dvorets_sporta Elmash Gagarinskaya Geologicheskaya Himmash I_Pyatiletki_square
Italyanskaya Kalinovskaya Kamennye_palatki Keramicheskaya Koltsovo Kommunarov_square
Komsomolskaya Kompressornaya Kraulya Kuybyshevskaya Lechebnaya MEGA Mashinostroiteley
Mayakovskaya Metallurgov Moskovskaya Nizhne_Isetskaya Oborony_square Ozyornaya Parkovaya
Pionerskaya Pobedy Posadskaya Prospekt_Kosmonavtov Samolyotnaya Shcherbakovskaya
Shefskaya Shevchenko Sibirskaya Siniye_kamni Sortirovochnaya Sovhoznaya Taganskaya
Tatishchevskaya Teatralnaya Turbinnaya Uktusskie_Gory Uralmash Uralskaya University
Varshavskaya Verh_Isetskaya Vilonovskaya Voennaya Volgogradskaya Vostochnaya Vtorchermet
Vtuzgorodok Yugo_zapadnaya Zarechny Zelyony_ostrov Zvezda""".split()
MOST = 4900
FEW = 10


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        pairs = [(a, b) for a in STATIONS for b in STATIONS]
        rng.shuffle(pairs)
    else:
        count = MOST if mode == 2 else rng.randint(1, FEW)
        pairs = [(rng.choice(STATIONS), rng.choice(STATIONS)) for _ in range(count)]
    print(len(pairs))
    print("\n".join("%s %s" % p for p in pairs))


main()
