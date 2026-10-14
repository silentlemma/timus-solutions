#include <cstdio>
#include <map>
#include <queue>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

// the lines of the map from the statement, in the order of their stations; the circle line closes
// on itself
const char *LINES[] = {
    "Pobedy I_Pyatiletki_square Zvezda Uralskaya Shevchenko Teatralnaya Kuybyshevskaya "
    "Oborony_square Mayakovskaya Parkovaya Botanicheskaya Samolyotnaya Vtorchermet "
    "Keramicheskaya",
    "Bakinskih_Komissarov Prospekt_Kosmonavtov Uralmash Mashinostroiteley Uralskaya Dinamo "
    "1905_year_square Geologicheskaya Bazhovskaya Chkalovskaya Botanicheskaya "
    "Shcherbakovskaya Uktusskie_Gory Nizhne_Isetskaya Himmash",
    "Taganskaya Elmash Turbinnaya Pionerskaya Shevchenko 1905_year_square Moskovskaya "
    "Central_stadium Kraulya Metallurgov MEGA",
    "7_klyuchey Sortirovochnaya China_town Zarechny City 1905_year_square Kuybyshevskaya "
    "Sibirskaya Siniye_kamni Lechebnaya Varshavskaya Kompressornaya Koltsovo",
    "Kalinovskaya Italyanskaya Ozyornaya Shefskaya Komsomolskaya Gagarinskaya Teatralnaya "
    "Geologicheskaya Posadskaya Volgogradskaya Yugo_zapadnaya Akademicheskaya",
    "Zelyony_ostrov Tatishchevskaya Verh_Isetskaya Kommunarov_square 1905_year_square "
    "Teatralnaya Vostochnaya Vtuzgorodok Kamennye_palatki University",
    "Vilonovskaya Gagarinskaya Vostochnaya Kuybyshevskaya Geologicheskaya Dvorets_sporta "
    "Aviatsionnaya Voennaya Sovhoznaya",
};
const char *CIRCLE =
    "Uralskaya Pionerskaya Gagarinskaya Vtuzgorodok Sibirskaya Oborony_square Bazhovskaya "
    "Dvorets_sporta Posadskaya Moskovskaya Kommunarov_square City";

const int NAME = 41; // station names are short

map<string, int> id;
vector<vector<int>> adj;

int station(const string &name) {
    if (!id.count(name)) {
        int fresh = id.size();
        id[name] = fresh;
        adj.push_back({});
    }
    return id[name];
}

vector<int> stops(const char *line) {
    istringstream in(line);
    vector<int> s;
    string name;
    while (in >> name)
        s.push_back(station(name));
    return s;
}

void join(int a, int b) {
    adj[a].push_back(b);
    adj[b].push_back(a);
}

int main() {
    for (const char *line : LINES) {
        vector<int> s = stops(line);
        for (size_t i = 0; i + 1 < s.size(); i++)
            join(s[i], s[i + 1]);
    }
    vector<int> ring = stops(CIRCLE);
    for (size_t i = 0; i < ring.size(); i++)
        join(ring[i], ring[(i + 1) % ring.size()]);
    // every run between neighbouring stations takes a minute and changes are
    // free, so the answer is the number of runs on a shortest path
    int n = adj.size();
    vector<vector<int>> dist(n, vector<int>(n, -1));
    for (int s = 0; s < n; s++) {
        queue<int> q;
        q.push(s);
        dist[s][s] = 0;
        while (!q.empty()) {
            int v = q.front();
            q.pop();
            for (int u : adj[v])
                if (dist[s][u] < 0) {
                    dist[s][u] = dist[s][v] + 1;
                    q.push(u);
                }
        }
    }
    int questions;
    if (scanf("%d", &questions) != 1)
        return 0;
    char a[NAME], b[NAME];
    for (int i = 0; i < questions; i++) {
        if (scanf("%40s %40s", a, b) != 2)
            return 0;
        printf("%d\n", dist[id[a]][id[b]]);
    }
}
