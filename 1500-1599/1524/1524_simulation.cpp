#include <algorithm>
#include <cmath>
#include <cstdio>
#include <iostream>
#include <map>
#include <queue>
#include <string>
#include <tuple>
#include <vector>

using namespace std;

const double EPS = 1e-9; // rounding to the closest minute must not suffer from 0.4999999
const int DAY = 24 * 60, HOUR = 60, NONE = -1;
enum Kind { RUN, KILL, FINDOUT, TALK };
// message kinds in the order they are printed within one minute
enum Message { BOUGHT = 1, BROKEN, KILLED, FINISHED, TIRED, JOINED, STARTED };

const double HALF = 0.5;
const int LETTERS = 26, STAMP = 32;
// the order of the traits of an agent in the input
enum Trait { ACC, WALK, INTEL, EXP, DRIVE, TRAITS };

int minutes(double x) { return (int)floor(x + HALF + EPS); }

struct Agent {
    string name;
    char letter;
    double acc, walk, intel, exp, drive;
    bool busy = false, alive = true;
};

struct CarType {
    double need;
    int limit;
    string name;
};

struct Car {
    int kind, passed;
    string id;
    bool busy = false, broken = false;
};

struct Monster {
    double needExp, needInt;
    int evade, value;
    string name;
};

struct Quest {
    int kind = RUN, dist = 0, monster = 0;
    double need = 0;
    int mint = 0, state = 0; // state 0 waiting, 1 under way, 2 done
};

// a team with its car (or none) and the moments of the quest counted from
// its start, NONE where there is no such moment
struct Plan {
    vector<int> team;
    int car = NONE, total = 0, broke = NONE, kill = NONE, walked = 0, drove = 0;
};

struct Stats {
    double walk, drive, acc, exp, intel;
};

vector<Agent> agents;
vector<CarType> types;
vector<Car> cars;
vector<Monster> monsters;
vector<Quest> quests;
map<int, Plan> active;
priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<>> timeline;
vector<pair<int, string>> logs;
int maxWalk, maxEvade, maxValue;
double retireAt;

string letters(const vector<int> &team) {
    string s;
    for (int a : team)
        s += agents[a].letter;
    return s;
}

string teamText(const vector<int> &team) {
    string s = string("Agent ") + agents[team[0]].letter;
    if (team.size() > 1)
        s += string(" and agent ") + agents[team[1]].letter;
    return s;
}

Stats teamStats(const vector<int> &team) {
    const Agent &a = agents[team[0]];
    if (team.size() == 1)
        return {a.walk, a.drive, a.acc, a.exp, a.intel};
    const Agent &b = agents[team[1]];
    return {min(a.walk, b.walk), max(a.drive, b.drive), (a.acc + b.acc) / 2,
            1 - (1 - a.exp) * (1 - b.exp), 1 - (1 - a.intel) * (1 - b.intel)};
}

// the time of the work at the place, or NONE when the team may not do it
int actionTime(const Quest &q, const Stats &st) {
    if (q.kind == KILL) {
        const Monster &m = monsters[q.monster];
        return st.exp >= m.needExp && st.intel >= m.needInt ? minutes(m.evade / st.acc) : NONE;
    }
    if (q.kind == FINDOUT)
        return st.intel >= q.need ? minutes(q.mint / st.intel) : NONE;
    if (q.kind == TALK)
        return st.exp >= q.need ? minutes(q.mint / st.exp) : NONE;
    return 0;
}

bool withCar(const vector<int> &team, const Quest &q, int action, const Stats &st, int c, Plan &p) {
    const CarType &t = types[cars[c].kind];
    int rest = t.limit - cars[c].passed, d = q.dist;
    if (rest <= 0 || st.drive < t.need)
        return false;
    auto byCar = [&](int x) { return minutes(x / st.drive); };
    auto onFoot = [&](int x) { return minutes(x / st.walk); };
    p = Plan();
    p.team = team;
    p.car = c;
    int there, back;
    if (rest < d) { // breaks on the way there, the rest is walked
        there = byCar(rest) + onFoot(d - rest);
        back = onFoot(d);
        p.broke = byCar(rest);
        p.walked = 2 * d - rest;
        p.drove = rest;
    } else if (rest == d) { // breaks on arrival
        there = byCar(d);
        back = onFoot(d);
        p.broke = there;
        p.walked = p.drove = d;
    } else if (rest < 2 * d) { // breaks on the way back
        there = byCar(d);
        back = byCar(rest - d) + onFoot(2 * d - rest);
        p.broke = there + action + byCar(rest - d);
        p.walked = 2 * d - rest;
        p.drove = rest;
    } else {
        there = back = byCar(d);
        p.drove = 2 * d;
        if (rest == 2 * d) // breaks on return
            p.broke = there + action + back;
    }
    p.total = there + action + back;
    if (q.kind == KILL)
        p.kill = there + action;
    return true;
}

bool bestForTeam(const vector<int> &team, const Quest &q, const vector<int> &freeCars, Plan &best) {
    Stats st = teamStats(team);
    int action = actionTime(q, st);
    if (action == NONE)
        return false;
    int there = minutes(q.dist / st.walk);
    best = Plan();
    best.team = team;
    best.total = 2 * there + action;
    best.walked = 2 * q.dist;
    if (q.kind == KILL)
        best.kill = there + action;
    Plan p;
    for (int c : freeCars)
        // a car only when strictly faster, then the smaller id
        if (withCar(team, q, action, st, c, p) &&
            (p.total < best.total ||
             (p.total == best.total && best.car != NONE && cars[c].id < cars[best.car].id)))
            best = p;
    return true;
}

bool better(const Plan &a, const Plan *b) {
    if (!b)
        return true;
    return make_tuple(a.total, a.team.size(), letters(a.team)) <
           make_tuple(b->total, b->team.size(), letters(b->team));
}

bool bestPlan(const Quest &q, Plan &best) {
    vector<int> freeAgents, freeCars;
    for (int i = 0; i < (int)agents.size(); i++)
        if (agents[i].alive && !agents[i].busy)
            freeAgents.push_back(i);
    sort(freeAgents.begin(), freeAgents.end(),
         [](int x, int y) { return agents[x].letter < agents[y].letter; });
    for (int i = 0; i < (int)cars.size(); i++)
        if (!cars[i].broken && !cars[i].busy && cars[i].passed < types[cars[i].kind].limit)
            freeCars.push_back(i);
    sort(freeCars.begin(), freeCars.end(), [](int x, int y) { return cars[x].id < cars[y].id; });
    vector<vector<int>> teams;
    for (int a : freeAgents)
        teams.push_back({a});
    for (size_t i = 0; i < freeAgents.size(); i++)
        for (size_t j = i + 1; j < freeAgents.size(); j++)
            teams.push_back({freeAgents[i], freeAgents[j]});
    bool found = false;
    Plan p;
    for (const vector<int> &team : teams)
        if (bestForTeam(team, q, freeCars, p) && better(p, found ? &best : nullptr)) {
            best = p;
            found = true;
        }
    return found;
}

void start(int num, const Plan &p, int now) {
    quests[num - 1].state = 1;
    active[num] = p;
    if (p.broke != NONE)
        timeline.emplace(now + p.broke, BROKEN, num);
    if (p.kill != NONE)
        timeline.emplace(now + p.kill, KILLED, num);
    timeline.emplace(now + p.total, FINISHED, num);
    for (int a : p.team)
        agents[a].busy = true;
    string text = teamText(p.team) + " started quest " + to_string(num);
    if (p.car != NONE) {
        cars[p.car].busy = true;
        text += " using car " + cars[p.car].id;
    }
    logs.push_back({STARTED, text + "."});
}

void finish(int num) {
    Plan p = active[num];
    active.erase(num);
    Quest &q = quests[num - 1];
    logs.push_back({FINISHED, teamText(p.team) + " finished quest " + to_string(num) + "."});
    if (p.car != NONE) {
        Car &c = cars[p.car];
        if (!c.broken) {
            c.busy = false;
            c.passed = min(c.passed + p.drove, types[c.kind].limit);
        }
    }
    vector<string> gone;
    for (int i : p.team) {
        Agent &a = agents[i];
        a.busy = false;
        double acc = a.acc, walk = a.walk, intel = a.intel, exp = a.exp, drive = a.drive;
        if (p.walked > 0)
            a.walk = walk + (1 - walk) * p.walked / maxWalk;
        if (p.car != NONE && p.drove > 0)
            a.drive = drive + (1 - drive) * p.drove / maxWalk;
        if (q.kind == KILL) {
            const Monster &m = monsters[q.monster];
            a.exp = exp + (1 - exp) * m.value / maxValue;
            a.acc = acc + (1 - acc) * m.evade / maxEvade;
        } else if (q.kind == FINDOUT) {
            a.exp = exp + (1 - exp) * intel / q.mint;
            a.intel = intel + (1 - intel) * intel / q.mint;
        } else if (q.kind == TALK) {
            a.exp = exp + (1 - exp) * exp / q.mint;
        }
        if (a.alive && a.exp >= retireAt) {
            a.alive = false;
            gone.push_back(string(1, a.letter));
        }
    }
    sort(gone.begin(), gone.end());
    for (const string &letter : gone)
        logs.push_back({TIRED, "Agent " + letter + " has tired."});
    q.state = 2;
}

char newLetter(const string &name) {
    vector<bool> used(LETTERS, false);
    for (const Agent &a : agents)
        if (a.alive)
            used[a.letter - 'A'] = true;
    int target = toupper((unsigned char)name[0]);
    char best = 0;
    int bestDist = 0;
    for (char c = 'A'; c <= 'Z'; c++)
        if (!used[c - 'A'] && (best == 0 || abs(c - target) < bestDist)) {
            best = c;
            bestDist = abs(c - target);
        }
    return best;
}

// an outside event: a new agent, a bought car or a received quest
struct Outside {
    int time;
    string word, name, id;
    double values[TRAITS];
    int passed = 0;
    Quest q;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        Agent a;
        cin >> a.name >> a.acc >> a.walk >> a.intel >> a.exp >> a.drive >> a.letter;
        agents.push_back(a);
    }
    map<string, int> typeOf, monsterOf;
    cin >> n;
    for (int i = 0; i < n; i++) {
        CarType t;
        cin >> t.need >> t.limit >> t.name;
        typeOf[t.name] = types.size();
        types.push_back(t);
    }
    auto newCar = [&](const string &name, int passed, const string &id) {
        Car c;
        c.kind = typeOf[name];
        c.passed = passed;
        c.id = id;
        c.broken = passed >= types[c.kind].limit;
        cars.push_back(c);
    };
    cin >> n;
    for (int i = 0; i < n; i++) {
        string name, id;
        int passed;
        cin >> name >> passed >> id;
        newCar(name, passed, id);
    }
    cin >> n;
    for (int i = 0; i < n; i++) {
        Monster m;
        cin >> m.needExp >> m.needInt >> m.evade >> m.value >> m.name;
        monsterOf[m.name] = monsters.size();
        monsters.push_back(m);
    }
    cin >> maxWalk >> maxEvade >> maxValue >> retireAt;
    cin >> n;
    vector<Outside> outsides(n);
    for (Outside &e : outsides) {
        cin >> e.time >> e.word;
        if (e.word == "newagent") {
            cin >> e.name;
            for (double &v : e.values)
                cin >> v;
        } else if (e.word == "newcar") {
            cin >> e.name >> e.passed >> e.id;
        } else {
            string kind, monsterName;
            cin >> kind >> e.q.dist;
            if (kind == "kill") {
                e.q.kind = KILL;
                cin >> monsterName;
                e.q.monster = monsterOf[monsterName];
            } else if (kind != "run") {
                e.q.kind = kind == "talk" ? TALK : FINDOUT;
                cin >> e.q.need >> e.q.mint;
            }
        }
    }
    size_t next = 0;
    while (next < outsides.size() || !timeline.empty()) {
        int now = next < outsides.size() ? outsides[next].time : NONE;
        if (!timeline.empty() && (now == NONE || get<0>(timeline.top()) < now))
            now = get<0>(timeline.top());
        logs.clear();
        while (!timeline.empty() && get<0>(timeline.top()) == now) {
            auto [time, kind, num] = timeline.top();
            timeline.pop();
            if (!active.count(num))
                continue; // a moment that came after the quest had ended
            const Plan &p = active[num];
            if (kind == BROKEN) {
                Car &c = cars[p.car];
                if (!c.broken) {
                    c.broken = true;
                    c.busy = false;
                    c.passed = types[c.kind].limit;
                    logs.push_back({BROKEN, "Car " + c.id + " was broken."});
                }
            } else if (kind == KILLED) {
                logs.push_back({KILLED, teamText(p.team) + " killed monster " +
                                            monsters[quests[num - 1].monster].name + "."});
            } else {
                finish(num);
            }
        }
        if (next < outsides.size() && outsides[next].time == now) {
            const Outside &e = outsides[next++];
            if (e.word == "newagent") {
                Agent a;
                a.name = e.name;
                a.letter = newLetter(e.name);
                a.acc = e.values[ACC];
                a.walk = e.values[WALK];
                a.intel = e.values[INTEL];
                a.exp = e.values[EXP];
                a.drive = e.values[DRIVE];
                agents.push_back(a);
                logs.push_back(
                    {JOINED, "New agent " + e.name + " got a letter " + string(1, a.letter) + "."});
            } else if (e.word == "newcar") {
                newCar(e.name, e.passed, e.id);
                logs.push_back({BOUGHT, "MIB bought a car of class " + e.name + "."});
            } else {
                quests.push_back(e.q);
            }
        }
        // all quests that can start now, the earliest received first
        for (bool again = true; again;) {
            again = false;
            Plan p;
            for (size_t i = 0; i < quests.size() && !again; i++)
                if (quests[i].state == 0 && bestPlan(quests[i], p)) {
                    start(i + 1, p, now);
                    again = true;
                }
        }
        sort(logs.begin(), logs.end());
        char stamp[STAMP];
        snprintf(stamp, sizeof stamp, "%04d:%02d:%02d", now / DAY, now % DAY / HOUR, now % HOUR);
        for (const auto &m : logs)
            printf("%s    %s\n", stamp, m.second.c_str());
    }
}
