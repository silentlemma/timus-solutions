import sys
from collections import deque

# the lines of the map in the order of their stations; the circle line closes
# on itself
LINES = [
    "Pobedy I_Pyatiletki_square Zvezda Uralskaya Shevchenko Teatralnaya Kuybyshevskaya"
    " Oborony_square Mayakovskaya Parkovaya Botanicheskaya Samolyotnaya Vtorchermet"
    " Keramicheskaya",
    "Bakinskih_Komissarov Prospekt_Kosmonavtov Uralmash Mashinostroiteley Uralskaya Dinamo"
    " 1905_year_square Geologicheskaya Bazhovskaya Chkalovskaya Botanicheskaya"
    " Shcherbakovskaya Uktusskie_Gory Nizhne_Isetskaya Himmash",
    "Taganskaya Elmash Turbinnaya Pionerskaya Shevchenko 1905_year_square Moskovskaya"
    " Central_stadium Kraulya Metallurgov MEGA",
    "7_klyuchey Sortirovochnaya China_town Zarechny City 1905_year_square Kuybyshevskaya"
    " Sibirskaya Siniye_kamni Lechebnaya Varshavskaya Kompressornaya Koltsovo",
    "Kalinovskaya Italyanskaya Ozyornaya Shefskaya Komsomolskaya Gagarinskaya Teatralnaya"
    " Geologicheskaya Posadskaya Volgogradskaya Yugo_zapadnaya Akademicheskaya",
    "Zelyony_ostrov Tatishchevskaya Verh_Isetskaya Kommunarov_square 1905_year_square"
    " Teatralnaya Vostochnaya Vtuzgorodok Kamennye_palatki University",
    "Vilonovskaya Gagarinskaya Vostochnaya Kuybyshevskaya Geologicheskaya Dvorets_sporta"
    " Aviatsionnaya Voennaya Sovhoznaya",
]
CIRCLE = (
    "Uralskaya Pionerskaya Gagarinskaya Vtuzgorodok Sibirskaya Oborony_square Bazhovskaya"
    " Dvorets_sporta Posadskaya Moskovskaya Kommunarov_square City"
)


def main():
    adj = {}

    def join(a, b):
        adj.setdefault(a, set()).add(b)
        adj.setdefault(b, set()).add(a)

    for line in LINES:
        stops = line.split()
        for a, b in zip(stops, stops[1:]):
            join(a, b)
    ring = CIRCLE.split()
    for a, b in zip(ring, ring[1:] + ring[:1]):
        join(a, b)
    # every run between neighbouring stations takes a minute and changes are
    # free, so the answer is the number of runs on a shortest path
    dist = {}
    for start in adj:
        seen = {start: 0}
        queue = deque([start])
        while queue:
            v = queue.popleft()
            for u in adj[v]:
                if u not in seen:
                    seen[u] = seen[v] + 1
                    queue.append(u)
        dist[start] = seen
    words = iter(sys.stdin.read().split())
    n = int(next(words))
    out = [str(dist[next(words)][next(words)]) for _ in range(n)]
    print("\n".join(out))


main()
