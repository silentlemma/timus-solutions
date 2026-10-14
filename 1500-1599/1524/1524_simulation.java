import java.io.*;
import java.util.*;

public class Main {
    static final double EPS = 1e-9; // rounding to the closest minute must not suffer from 0.4999999
    static final double HALF = 0.5;
    static final int HOUR = 60;
    static final int DAY = 24 * HOUR;
    static final int NONE = -1;
    static final int RUN = 0;
    static final int KILL = 1;
    static final int FINDOUT = 2;
    static final int TALK = 3;
    // message kinds in the order they are printed within one minute
    static final int BOUGHT = 1;
    static final int BROKEN = 2;
    static final int KILLED = 3;
    static final int FINISHED = 4;
    static final int TIRED = 5;
    static final int JOINED = 6;
    static final int STARTED = 7;

    static int minutes(double x) { return (int)Math.floor(x + HALF + EPS); }

    static class Agent {
        String name;
        char letter;
        double acc, walk, intel, exp, drive;
        boolean busy = false, alive = true;
    }

    static class Car {
        int kind, passed;
        String id;
        boolean busy = false, broken = false;
    }

    static class Quest {
        int kind = RUN, dist, monster, mint, state; // state 0 waiting, 1 under way, 2 done
        double need;
    }

    // a team with its car (or none) and the moments of the quest counted from
    // its start, NONE where there is no such moment
    static class Plan {
        int[] team;
        int car = NONE, total, broke = NONE, kill = NONE, walked, drove;
    }

    static List<Agent> agents = new ArrayList<>();
    static List<Car> cars = new ArrayList<>();
    static List<Quest> quests = new ArrayList<>();
    static double[] typeNeed = new double[0];
    static int[] typeLimit = new int[0];
    static String[] typeName = new String[0];
    static double[] monsterExp, monsterInt;
    static int[] monsterEvade, monsterValue;
    static String[] monsterName;
    static Map<Integer, Plan> active = new HashMap<>();
    // a moment: time, kind of event, quest number
    static PriorityQueue<int[]> timeline =
        new PriorityQueue<>((x, y)
                                -> x[0] != y[0]   ? Integer.compare(x[0], y[0])
                                   : x[1] != y[1] ? Integer.compare(x[1], y[1])
                                                  : Integer.compare(x[2], y[2]));
    static List<String[]> logs = new ArrayList<>(); // kind as text of one digit, then the message
    static int maxWalk, maxEvade, maxValue;
    static double retireAt;

    static String letters(int[] team) {
        StringBuilder s = new StringBuilder();
        for (int a : team)
            s.append(agents.get(a).letter);
        return s.toString();
    }

    static String teamText(int[] team) {
        String s = "Agent " + agents.get(team[0]).letter;
        if (team.length > 1)
            s += " and agent " + agents.get(team[1]).letter;
        return s;
    }

    static void log(int kind, String text) { logs.add(new String[] {String.valueOf(kind), text}); }

    // the joint traits of a team; a single agent keeps his own
    static Agent teamStats(int[] team) {
        Agent a = agents.get(team[0]);
        if (team.length == 1)
            return a;
        Agent b = agents.get(team[1]), s = new Agent();
        s.walk = Math.min(a.walk, b.walk);
        s.drive = Math.max(a.drive, b.drive);
        s.acc = (a.acc + b.acc) / 2;
        s.exp = 1 - (1 - a.exp) * (1 - b.exp);
        s.intel = 1 - (1 - a.intel) * (1 - b.intel);
        return s;
    }

    // the time of the work at the place, or NONE when the team may not do it
    static int actionTime(Quest q, double acc, double exp, double intel) {
        if (q.kind == KILL) {
            int m = q.monster;
            return exp >= monsterExp[m] && intel >= monsterInt[m] ? minutes(monsterEvade[m] / acc)
                                                                  : NONE;
        }
        if (q.kind == FINDOUT)
            return intel >= q.need ? minutes(q.mint / intel) : NONE;
        if (q.kind == TALK)
            return exp >= q.need ? minutes(q.mint / exp) : NONE;
        return 0;
    }

    static Plan withCar(int[] team, Quest q, int action, double walk, double drive, int c) {
        Car car = cars.get(c);
        int rest = typeLimit[car.kind] - car.passed, d = q.dist;
        if (rest <= 0 || drive < typeNeed[car.kind])
            return null;
        Plan p = new Plan();
        p.team = team;
        p.car = c;
        int there, back;
        if (rest < d) { // breaks on the way there, the rest is walked
            there = minutes(rest / drive) + minutes((d - rest) / walk);
            back = minutes(d / walk);
            p.broke = minutes(rest / drive);
            p.walked = 2 * d - rest;
            p.drove = rest;
        } else if (rest == d) { // breaks on arrival
            there = minutes(d / drive);
            back = minutes(d / walk);
            p.broke = there;
            p.walked = p.drove = d;
        } else if (rest < 2 * d) { // breaks on the way back
            there = minutes(d / drive);
            back = minutes((rest - d) / drive) + minutes((2 * d - rest) / walk);
            p.broke = there + action + minutes((rest - d) / drive);
            p.walked = 2 * d - rest;
            p.drove = rest;
        } else {
            there = back = minutes(d / drive);
            p.drove = 2 * d;
            if (rest == 2 * d) // breaks on return
                p.broke = there + action + back;
        }
        p.total = there + action + back;
        if (q.kind == KILL)
            p.kill = there + action;
        return p;
    }

    static Plan bestForTeam(int[] team, Quest q, List<Integer> freeCars) {
        Agent st = teamStats(team);
        double walk = st.walk, drive = st.drive;
        int action = actionTime(q, st.acc, st.exp, st.intel);
        if (action == NONE)
            return null;
        int there = minutes(q.dist / walk);
        Plan best = new Plan();
        best.team = team;
        best.total = 2 * there + action;
        best.walked = 2 * q.dist;
        if (q.kind == KILL)
            best.kill = there + action;
        for (int c : freeCars) {
            Plan p = withCar(team, q, action, walk, drive, c);
            // a car only when strictly faster, then the smaller id
            if (p != null &&
                (p.total < best.total || (p.total == best.total && best.car != NONE &&
                                          cars.get(c).id.compareTo(cars.get(best.car).id) < 0)))
                best = p;
        }
        return best;
    }

    static boolean better(Plan a, Plan b) {
        if (b == null)
            return true;
        if (a.total != b.total)
            return a.total < b.total;
        if (a.team.length != b.team.length)
            return a.team.length < b.team.length;
        return letters(a.team).compareTo(letters(b.team)) < 0;
    }

    static Plan bestPlan(Quest q) {
        List<Integer> free = new ArrayList<>(), freeCars = new ArrayList<>();
        for (int i = 0; i < agents.size(); i++)
            if (agents.get(i).alive && !agents.get(i).busy)
                free.add(i);
        free.sort((x, y) -> Character.compare(agents.get(x).letter, agents.get(y).letter));
        for (int i = 0; i < cars.size(); i++) {
            Car c = cars.get(i);
            if (!c.broken && !c.busy && c.passed < typeLimit[c.kind])
                freeCars.add(i);
        }
        freeCars.sort((x, y) -> cars.get(x).id.compareTo(cars.get(y).id));
        List<int[]> teams = new ArrayList<>();
        for (int a : free)
            teams.add(new int[] {a});
        for (int i = 0; i < free.size(); i++)
            for (int j = i + 1; j < free.size(); j++)
                teams.add(new int[] {free.get(i), free.get(j)});
        Plan best = null;
        for (int[] team : teams) {
            Plan p = bestForTeam(team, q, freeCars);
            if (p != null && better(p, best))
                best = p;
        }
        return best;
    }

    static void start(int num, Plan p, int now) {
        quests.get(num - 1).state = 1;
        active.put(num, p);
        if (p.broke != NONE)
            timeline.add(new int[] {now + p.broke, BROKEN, num});
        if (p.kill != NONE)
            timeline.add(new int[] {now + p.kill, KILLED, num});
        timeline.add(new int[] {now + p.total, FINISHED, num});
        for (int a : p.team)
            agents.get(a).busy = true;
        String text = teamText(p.team) + " started quest " + num;
        if (p.car != NONE) {
            cars.get(p.car).busy = true;
            text += " using car " + cars.get(p.car).id;
        }
        log(STARTED, text + ".");
    }

    static void finish(int num) {
        Plan p = active.remove(num);
        Quest q = quests.get(num - 1);
        log(FINISHED, teamText(p.team) + " finished quest " + num + ".");
        if (p.car != NONE) {
            Car c = cars.get(p.car);
            if (!c.broken) {
                c.busy = false;
                c.passed = Math.min(c.passed + p.drove, typeLimit[c.kind]);
            }
        }
        List<String> gone = new ArrayList<>();
        for (int i : p.team) {
            Agent a = agents.get(i);
            a.busy = false;
            double acc = a.acc, walk = a.walk, intel = a.intel, exp = a.exp, drive = a.drive;
            if (p.walked > 0)
                a.walk = walk + (1 - walk) * p.walked / maxWalk;
            if (p.car != NONE && p.drove > 0)
                a.drive = drive + (1 - drive) * p.drove / maxWalk;
            if (q.kind == KILL) {
                a.exp = exp + (1 - exp) * monsterValue[q.monster] / maxValue;
                a.acc = acc + (1 - acc) * monsterEvade[q.monster] / maxEvade;
            } else if (q.kind == FINDOUT) {
                a.exp = exp + (1 - exp) * intel / q.mint;
                a.intel = intel + (1 - intel) * intel / q.mint;
            } else if (q.kind == TALK) {
                a.exp = exp + (1 - exp) * exp / q.mint;
            }
            if (a.alive && a.exp >= retireAt) {
                a.alive = false;
                gone.add(String.valueOf(a.letter));
            }
        }
        Collections.sort(gone);
        for (String letter : gone)
            log(TIRED, "Agent " + letter + " has tired.");
        q.state = 2;
    }

    static char newLetter(String name) {
        Set<Character> used = new HashSet<>();
        for (Agent a : agents)
            if (a.alive)
                used.add(a.letter);
        int target = Character.toUpperCase(name.charAt(0));
        char best = 0;
        int bestDist = 0;
        for (char c = 'A'; c <= 'Z'; c++)
            if (!used.contains(c) && (best == 0 || Math.abs(c - target) < bestDist)) {
                best = c;
                bestDist = Math.abs(c - target);
            }
        return best;
    }

    // an outside event: a new agent, a bought car or a received quest
    static class Outside {
        int time, passed;
        String word, name, id;
        Agent agent;
        Quest quest;
    }

    static List<String> words = new ArrayList<>();
    static int pos = 0;

    static String next() { return words.get(pos++); }

    static int nextInt() { return Integer.parseInt(next()); }

    static double nextDouble() { return Double.parseDouble(next()); }

    static void newCar(Map<String, Integer> typeOf, String name, int passed, String id) {
        Car c = new Car();
        c.kind = typeOf.get(name);
        c.passed = passed;
        c.id = id;
        c.broken = passed >= typeLimit[c.kind];
        cars.add(c);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        for (String line; (line = reader.readLine()) != null;) {
            StringTokenizer st = new StringTokenizer(line);
            while (st.hasMoreTokens())
                words.add(st.nextToken());
        }
        int n = nextInt();
        for (int i = 0; i < n; i++) {
            Agent a = new Agent();
            a.name = next();
            a.acc = nextDouble();
            a.walk = nextDouble();
            a.intel = nextDouble();
            a.exp = nextDouble();
            a.drive = nextDouble();
            a.letter = next().charAt(0);
            agents.add(a);
        }
        Map<String, Integer> typeOf = new HashMap<>(), monsterOf = new HashMap<>();
        n = nextInt();
        typeNeed = new double[n];
        typeLimit = new int[n];
        typeName = new String[n];
        for (int i = 0; i < n; i++) {
            typeNeed[i] = nextDouble();
            typeLimit[i] = nextInt();
            typeName[i] = next();
            typeOf.put(typeName[i], i);
        }
        n = nextInt();
        for (int i = 0; i < n; i++) {
            String name = next();
            int passed = nextInt();
            newCar(typeOf, name, passed, next());
        }
        n = nextInt();
        monsterExp = new double[n];
        monsterInt = new double[n];
        monsterEvade = new int[n];
        monsterValue = new int[n];
        monsterName = new String[n];
        for (int i = 0; i < n; i++) {
            monsterExp[i] = nextDouble();
            monsterInt[i] = nextDouble();
            monsterEvade[i] = nextInt();
            monsterValue[i] = nextInt();
            monsterName[i] = next();
            monsterOf.put(monsterName[i], i);
        }
        maxWalk = nextInt();
        maxEvade = nextInt();
        maxValue = nextInt();
        retireAt = nextDouble();
        n = nextInt();
        Outside[] outsides = new Outside[n];
        for (int i = 0; i < n; i++) {
            Outside e = outsides[i] = new Outside();
            e.time = nextInt();
            e.word = next();
            if (e.word.equals("newagent")) {
                e.agent = new Agent();
                e.agent.name = next();
                e.agent.acc = nextDouble();
                e.agent.walk = nextDouble();
                e.agent.intel = nextDouble();
                e.agent.exp = nextDouble();
                e.agent.drive = nextDouble();
            } else if (e.word.equals("newcar")) {
                e.name = next();
                e.passed = nextInt();
                e.id = next();
            } else {
                String kind = next();
                e.quest = new Quest();
                e.quest.dist = nextInt();
                if (kind.equals("kill")) {
                    e.quest.kind = KILL;
                    e.quest.monster = monsterOf.get(next());
                } else if (!kind.equals("run")) {
                    e.quest.kind = kind.equals("talk") ? TALK : FINDOUT;
                    e.quest.need = nextDouble();
                    e.quest.mint = nextInt();
                }
            }
        }
        StringBuilder out = new StringBuilder();
        int next = 0;
        while (next < n || !timeline.isEmpty()) {
            int now = next < n ? outsides[next].time : Integer.MAX_VALUE;
            if (!timeline.isEmpty() && timeline.peek()[0] < now)
                now = timeline.peek()[0];
            logs.clear();
            while (!timeline.isEmpty() && timeline.peek()[0] == now) {
                int[] e = timeline.poll();
                int num = e[2];
                Plan p = active.get(num);
                if (p == null)
                    continue; // a moment that came after the quest had ended
                if (e[1] == BROKEN) {
                    Car c = cars.get(p.car);
                    if (!c.broken) {
                        c.broken = true;
                        c.busy = false;
                        c.passed = typeLimit[c.kind];
                        log(BROKEN, "Car " + c.id + " was broken.");
                    }
                } else if (e[1] == KILLED) {
                    log(KILLED, teamText(p.team) + " killed monster " +
                                    monsterName[quests.get(num - 1).monster] + ".");
                } else {
                    finish(num);
                }
            }
            if (next < n && outsides[next].time == now) {
                Outside e = outsides[next++];
                if (e.word.equals("newagent")) {
                    Agent a = e.agent;
                    a.letter = newLetter(a.name);
                    agents.add(a);
                    log(JOINED, "New agent " + a.name + " got a letter " + a.letter + ".");
                } else if (e.word.equals("newcar")) {
                    newCar(typeOf, e.name, e.passed, e.id);
                    log(BOUGHT, "MIB bought a car of class " + e.name + ".");
                } else {
                    quests.add(e.quest);
                }
            }
            // all quests that can start now, the earliest received first
            for (boolean again = true; again;) {
                again = false;
                for (int i = 0; i < quests.size() && !again; i++) {
                    if (quests.get(i).state != 0)
                        continue;
                    Plan p = bestPlan(quests.get(i));
                    if (p != null) {
                        start(i + 1, p, now);
                        again = true;
                    }
                }
            }
            logs.sort((x, y) -> x[0].equals(y[0]) ? x[1].compareTo(y[1]) : x[0].compareTo(y[0]));
            String stamp = String.format("%04d:%02d:%02d", now / DAY, now % DAY / HOUR, now % HOUR);
            for (String[] m : logs)
                out.append(stamp).append("    ").append(m[1]).append('\n');
        }
        System.out.print(out);
    }
}
