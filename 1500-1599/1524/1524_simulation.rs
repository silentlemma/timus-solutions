use std::cmp::Reverse;
use std::collections::{BinaryHeap, HashMap};
use std::fmt::Write as _;
use std::io::{self, Read, Write};

const EPS: f64 = 1e-9; // rounding to the closest minute must not suffer from 0.4999999
const HALF: f64 = 0.5;
const DAY: i64 = 24 * 60;
const HOUR: i64 = 60;
const NONE: i64 = -1;
const RUN: u8 = 0;
const KILL: u8 = 1;
const FINDOUT: u8 = 2;
const TALK: u8 = 3;
// message kinds in the order they are printed within one minute
const BOUGHT: u8 = 1;
const BROKEN: u8 = 2;
const KILLED: u8 = 3;
const FINISHED: u8 = 4;
const TIRED: u8 = 5;
const JOINED: u8 = 6;
const STARTED: u8 = 7;

fn minutes(x: f64) -> i64 {
    (x + HALF + EPS).floor() as i64
}

#[derive(Clone)]
struct Agent {
    letter: u8,
    acc: f64,
    walk: f64,
    intel: f64,
    exp: f64,
    drive: f64,
    busy: bool,
    alive: bool,
}

struct Car {
    kind: usize,
    passed: i64,
    id: String,
    busy: bool,
    broken: bool,
}

struct CarType {
    need: f64,
    limit: i64,
}

struct Monster {
    need_exp: f64,
    need_int: f64,
    evade: i64,
    value: i64,
    name: String,
}

#[derive(Clone)]
struct Quest {
    kind: u8,
    dist: i64,
    monster: usize,
    need: f64,
    mint: i64,
    state: u8, // 0 waiting, 1 under way, 2 done
}

// a team with its car (or none) and the moments of the quest counted from
// its start, NONE where there is no such moment
#[derive(Clone)]
struct Plan {
    team: Vec<usize>,
    car: i64,
    total: i64,
    broke: i64,
    kill: i64,
    walked: i64,
    drove: i64,
}

struct Stats {
    walk: f64,
    drive: f64,
    acc: f64,
    exp: f64,
    intel: f64,
}

struct Agency {
    agents: Vec<Agent>,
    types: Vec<CarType>,
    cars: Vec<Car>,
    monsters: Vec<Monster>,
    quests: Vec<Quest>,
    active: HashMap<usize, Plan>,
    timeline: BinaryHeap<Reverse<(i64, u8, usize)>>,
    log: Vec<(u8, String)>,
    max_walk: f64,
    max_evade: f64,
    max_value: f64,
    retire: f64,
}

impl Agency {
    fn letters(&self, team: &[usize]) -> Vec<u8> {
        team.iter().map(|&a| self.agents[a].letter).collect()
    }

    fn team_text(&self, team: &[usize]) -> String {
        let mut s = format!("Agent {}", self.agents[team[0]].letter as char);
        if team.len() > 1 {
            write!(s, " and agent {}", self.agents[team[1]].letter as char).unwrap();
        }
        s
    }

    fn stats(&self, team: &[usize]) -> Stats {
        let a = &self.agents[team[0]];
        if team.len() == 1 {
            return Stats {
                walk: a.walk,
                drive: a.drive,
                acc: a.acc,
                exp: a.exp,
                intel: a.intel,
            };
        }
        let b = &self.agents[team[1]];
        Stats {
            walk: a.walk.min(b.walk),
            drive: a.drive.max(b.drive),
            acc: (a.acc + b.acc) / 2.0,
            exp: 1.0 - (1.0 - a.exp) * (1.0 - b.exp),
            intel: 1.0 - (1.0 - a.intel) * (1.0 - b.intel),
        }
    }

    // the time of the work at the place, or NONE when the team may not do it
    fn action_time(&self, q: &Quest, st: &Stats) -> i64 {
        match q.kind {
            KILL => {
                let m = &self.monsters[q.monster];
                if st.exp >= m.need_exp && st.intel >= m.need_int {
                    minutes(m.evade as f64 / st.acc)
                } else {
                    NONE
                }
            }
            FINDOUT if st.intel >= q.need => minutes(q.mint as f64 / st.intel),
            TALK if st.exp >= q.need => minutes(q.mint as f64 / st.exp),
            RUN => 0,
            _ => NONE,
        }
    }

    fn with_car(
        &self,
        team: &[usize],
        q: &Quest,
        action: i64,
        st: &Stats,
        c: usize,
    ) -> Option<Plan> {
        let car = &self.cars[c];
        let t = &self.types[car.kind];
        let (rest, d) = (t.limit - car.passed, q.dist);
        if rest <= 0 || st.drive < t.need {
            return None;
        }
        let by_car = |x: i64| minutes(x as f64 / st.drive);
        let on_foot = |x: i64| minutes(x as f64 / st.walk);
        let mut p = Plan {
            team: team.to_vec(),
            car: c as i64,
            total: 0,
            broke: NONE,
            kill: NONE,
            walked: 0,
            drove: 0,
        };
        let (there, back);
        if rest < d {
            // breaks on the way there, the rest is walked
            there = by_car(rest) + on_foot(d - rest);
            back = on_foot(d);
            p.broke = by_car(rest);
            p.walked = 2 * d - rest;
            p.drove = rest;
        } else if rest == d {
            // breaks on arrival
            there = by_car(d);
            back = on_foot(d);
            p.broke = there;
            p.walked = d;
            p.drove = d;
        } else if rest < 2 * d {
            // breaks on the way back
            there = by_car(d);
            back = by_car(rest - d) + on_foot(2 * d - rest);
            p.broke = there + action + by_car(rest - d);
            p.walked = 2 * d - rest;
            p.drove = rest;
        } else {
            there = by_car(d);
            back = there;
            p.drove = 2 * d;
            if rest == 2 * d {
                // breaks on return
                p.broke = there + action + back;
            }
        }
        p.total = there + action + back;
        if q.kind == KILL {
            p.kill = there + action;
        }
        Some(p)
    }

    fn best_for_team(&self, team: &[usize], q: &Quest, free_cars: &[usize]) -> Option<Plan> {
        let st = self.stats(team);
        let action = self.action_time(q, &st);
        if action == NONE {
            return None;
        }
        let there = minutes(q.dist as f64 / st.walk);
        let kill = if q.kind == KILL { there + action } else { NONE };
        let mut best = Plan {
            team: team.to_vec(),
            car: NONE,
            total: 2 * there + action,
            broke: NONE,
            kill,
            walked: 2 * q.dist,
            drove: 0,
        };
        for &c in free_cars {
            if let Some(p) = self.with_car(team, q, action, &st, c) {
                // a car only when strictly faster, then the smaller id
                if p.total < best.total
                    || (p.total == best.total
                        && best.car != NONE
                        && self.cars[c].id < self.cars[best.car as usize].id)
                {
                    best = p;
                }
            }
        }
        Some(best)
    }

    fn best_plan(&self, q: &Quest) -> Option<Plan> {
        let mut free: Vec<usize> = (0..self.agents.len())
            .filter(|&i| self.agents[i].alive && !self.agents[i].busy)
            .collect();
        free.sort_by_key(|&i| self.agents[i].letter);
        let mut free_cars: Vec<usize> = (0..self.cars.len())
            .filter(|&i| {
                let c = &self.cars[i];
                !c.broken && !c.busy && c.passed < self.types[c.kind].limit
            })
            .collect();
        free_cars.sort_by(|&x, &y| self.cars[x].id.cmp(&self.cars[y].id));
        let mut teams: Vec<Vec<usize>> = free.iter().map(|&a| vec![a]).collect();
        for (i, &a) in free.iter().enumerate() {
            for &b in &free[i + 1..] {
                teams.push(vec![a, b]);
            }
        }
        let mut best: Option<Plan> = None;
        for team in &teams {
            if let Some(p) = self.best_for_team(team, q, &free_cars) {
                let better = match &best {
                    None => true,
                    Some(b) => {
                        (p.total, p.team.len(), self.letters(&p.team))
                            < (b.total, b.team.len(), self.letters(&b.team))
                    }
                };
                if better {
                    best = Some(p);
                }
            }
        }
        best
    }

    fn start(&mut self, num: usize, p: Plan, now: i64) {
        self.quests[num - 1].state = 1;
        if p.broke != NONE {
            self.timeline.push(Reverse((now + p.broke, BROKEN, num)));
        }
        if p.kill != NONE {
            self.timeline.push(Reverse((now + p.kill, KILLED, num)));
        }
        self.timeline.push(Reverse((now + p.total, FINISHED, num)));
        for &a in &p.team {
            self.agents[a].busy = true;
        }
        let mut text = format!("{} started quest {}", self.team_text(&p.team), num);
        if p.car != NONE {
            let car = &mut self.cars[p.car as usize];
            car.busy = true;
            write!(text, " using car {}", car.id).unwrap();
        }
        self.log.push((STARTED, text + "."));
        self.active.insert(num, p);
    }

    fn finish(&mut self, num: usize) {
        let p = self.active.remove(&num).unwrap();
        let q = self.quests[num - 1].clone();
        let text = format!("{} finished quest {}.", self.team_text(&p.team), num);
        self.log.push((FINISHED, text));
        if p.car != NONE {
            let car = &mut self.cars[p.car as usize];
            if !car.broken {
                car.busy = false;
                car.passed = (car.passed + p.drove).min(self.types[car.kind].limit);
            }
        }
        let mut gone = Vec::new();
        for &i in &p.team {
            let (max_walk, max_evade, max_value, retire) =
                (self.max_walk, self.max_evade, self.max_value, self.retire);
            let (evade, value) = match self.monsters.get(q.monster) {
                Some(m) if q.kind == KILL => (m.evade as f64, m.value as f64),
                _ => (0.0, 0.0),
            };
            let a = &mut self.agents[i];
            a.busy = false;
            let (acc, walk, intel, exp, drive) = (a.acc, a.walk, a.intel, a.exp, a.drive);
            if p.walked > 0 {
                a.walk = walk + (1.0 - walk) * p.walked as f64 / max_walk;
            }
            if p.car != NONE && p.drove > 0 {
                a.drive = drive + (1.0 - drive) * p.drove as f64 / max_walk;
            }
            match q.kind {
                KILL => {
                    a.exp = exp + (1.0 - exp) * value / max_value;
                    a.acc = acc + (1.0 - acc) * evade / max_evade;
                }
                FINDOUT => {
                    a.exp = exp + (1.0 - exp) * intel / q.mint as f64;
                    a.intel = intel + (1.0 - intel) * intel / q.mint as f64;
                }
                TALK => a.exp = exp + (1.0 - exp) * exp / q.mint as f64,
                _ => {}
            }
            if a.alive && a.exp >= retire {
                a.alive = false;
                gone.push(a.letter);
            }
        }
        gone.sort_unstable();
        for letter in gone {
            self.log
                .push((TIRED, format!("Agent {} has tired.", letter as char)));
        }
        self.quests[num - 1].state = 2;
    }

    fn new_letter(&self, name: &str) -> u8 {
        let target = name.as_bytes()[0].to_ascii_uppercase() as i64;
        let used = |c: u8| self.agents.iter().any(|a| a.alive && a.letter == c);
        (b'A'..=b'Z')
            .filter(|&c| !used(c))
            .min_by_key(|&c| ((c as i64 - target).abs(), c))
            .unwrap()
    }
}

// the traits of an agent in the input order; the letter comes later
fn read_agent<'a>(next: &mut dyn FnMut() -> &'a str) -> Agent {
    let mut trait_value = || -> f64 { next().parse().unwrap() };
    Agent {
        letter: 0,
        acc: trait_value(),
        walk: trait_value(),
        intel: trait_value(),
        exp: trait_value(),
        drive: trait_value(),
        busy: false,
        alive: true,
    }
}

// an outside event: a new agent, a bought car or a received quest
enum Outside {
    NewAgent(String, Agent),
    NewCar(String, i64, String),
    NewQuest(Quest),
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut words = text.split_ascii_whitespace();
    let mut next = || words.next().unwrap();
    let mut agency = Agency {
        agents: Vec::new(),
        types: Vec::new(),
        cars: Vec::new(),
        monsters: Vec::new(),
        quests: Vec::new(),
        active: HashMap::new(),
        timeline: BinaryHeap::new(),
        log: Vec::new(),
        max_walk: 0.0,
        max_evade: 0.0,
        max_value: 0.0,
        retire: 0.0,
    };
    let n: usize = next().parse().unwrap();
    for _ in 0..n {
        next(); // the name
        let mut agent = read_agent(&mut next);
        agent.letter = next().as_bytes()[0];
        agency.agents.push(agent);
    }
    let mut type_of = HashMap::new();
    let n: usize = next().parse().unwrap();
    for i in 0..n {
        let need = next().parse().unwrap();
        let limit = next().parse().unwrap();
        type_of.insert(next().to_string(), i);
        agency.types.push(CarType { need, limit });
    }
    let n: usize = next().parse().unwrap();
    let mut cars = Vec::new();
    for _ in 0..n {
        let kind = type_of[next()];
        let passed: i64 = next().parse().unwrap();
        cars.push((kind, passed, next().to_string()));
    }
    for (kind, passed, id) in cars {
        let broken = passed >= agency.types[kind].limit;
        agency.cars.push(Car {
            kind,
            passed,
            id,
            busy: false,
            broken,
        });
    }
    let mut monster_of = HashMap::new();
    let n: usize = next().parse().unwrap();
    for i in 0..n {
        let need_exp = next().parse().unwrap();
        let need_int = next().parse().unwrap();
        let evade = next().parse().unwrap();
        let value = next().parse().unwrap();
        let name = next().to_string();
        monster_of.insert(name.clone(), i);
        agency.monsters.push(Monster {
            need_exp,
            need_int,
            evade,
            value,
            name,
        });
    }
    agency.max_walk = next().parse().unwrap();
    agency.max_evade = next().parse().unwrap();
    agency.max_value = next().parse().unwrap();
    agency.retire = next().parse().unwrap();
    let n: usize = next().parse().unwrap();
    let mut outsides = Vec::new();
    for _ in 0..n {
        let time: i64 = next().parse().unwrap();
        let e = match next() {
            "newagent" => {
                let name = next().to_string();
                Outside::NewAgent(name, read_agent(&mut next))
            }
            "newcar" => {
                let name = next().to_string();
                let passed = next().parse().unwrap();
                Outside::NewCar(name, passed, next().to_string())
            }
            _ => {
                let word = next();
                let mut q = Quest {
                    kind: RUN,
                    dist: next().parse().unwrap(),
                    monster: 0,
                    need: 0.0,
                    mint: 0,
                    state: 0,
                };
                match word {
                    "kill" => {
                        q.kind = KILL;
                        q.monster = monster_of[next()];
                    }
                    "run" => {}
                    _ => {
                        q.kind = if word == "talk" { TALK } else { FINDOUT };
                        q.need = next().parse().unwrap();
                        q.mint = next().parse().unwrap();
                    }
                }
                Outside::NewQuest(q)
            }
        };
        outsides.push((time, e));
    }
    let mut out = String::new();
    let mut at = 0;
    while at < outsides.len() || !agency.timeline.is_empty() {
        let mut now = if at < outsides.len() {
            outsides[at].0
        } else {
            i64::MAX
        };
        if let Some(Reverse((t, _, _))) = agency.timeline.peek() {
            now = now.min(*t);
        }
        agency.log.clear();
        while let Some(&Reverse((t, kind, num))) = agency.timeline.peek() {
            if t != now {
                break;
            }
            agency.timeline.pop();
            let Some(p) = agency.active.get(&num) else {
                continue; // a moment that came after the quest had ended
            };
            if kind == BROKEN {
                let car = &mut agency.cars[p.car as usize];
                if !car.broken {
                    car.broken = true;
                    car.busy = false;
                    car.passed = agency.types[car.kind].limit;
                    let text = format!("Car {} was broken.", car.id);
                    agency.log.push((BROKEN, text));
                }
            } else if kind == KILLED {
                let name = &agency.monsters[agency.quests[num - 1].monster].name;
                let text = format!("{} killed monster {}.", agency.team_text(&p.team), name);
                agency.log.push((KILLED, text));
            } else {
                agency.finish(num);
            }
        }
        if at < outsides.len() && outsides[at].0 == now {
            match &outsides[at].1 {
                Outside::NewAgent(name, joining) => {
                    let letter = agency.new_letter(name);
                    let mut agent = joining.clone();
                    agent.letter = letter;
                    agency.agents.push(agent);
                    agency.log.push((
                        JOINED,
                        format!("New agent {} got a letter {}.", name, letter as char),
                    ));
                }
                Outside::NewCar(name, passed, id) => {
                    let kind = type_of[name.as_str()];
                    let broken = *passed >= agency.types[kind].limit;
                    agency.cars.push(Car {
                        kind,
                        passed: *passed,
                        id: id.clone(),
                        busy: false,
                        broken,
                    });
                    agency
                        .log
                        .push((BOUGHT, format!("MIB bought a car of class {}.", name)));
                }
                Outside::NewQuest(q) => agency.quests.push(q.clone()),
            }
            at += 1;
        }
        // all quests that can start now, the earliest received first
        let mut again = true;
        while again {
            again = false;
            for i in 0..agency.quests.len() {
                if agency.quests[i].state != 0 {
                    continue;
                }
                if let Some(p) = agency.best_plan(&agency.quests[i]) {
                    agency.start(i + 1, p, now);
                    again = true;
                    break;
                }
            }
        }
        agency.log.sort();
        let stamp = format!("{:04}:{:02}:{:02}", now / DAY, now % DAY / HOUR, now % HOUR);
        for (_, m) in &agency.log {
            writeln!(out, "{}    {}", stamp, m).unwrap();
        }
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}
