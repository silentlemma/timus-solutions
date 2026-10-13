use std::fmt::Write as _;
use std::io::{self, Read};

const ROUNDS: i64 = 300_000; // large neighbourhood search rounds
const SHARE: i64 = 50; // the first threshold is the first cost over this
const MOST: usize = 8; // at most this many random items removed at once

const KINDS: usize = 3; // removal kinds: random items, a whole trip, one client
const UNREACHED: u16 = 0xFFFF; // no path yet in the subset table

// xorshift64 from a fixed seed: the same numbers in every language
const SEED: u64 = 88172645463325252;
const SHIFTS: (u32, u32, u32) = (13, 7, 17);

struct Rng(u64);

impl Rng {
    fn below(&mut self, k: usize) -> usize {
        self.0 ^= self.0 << SHIFTS.0;
        self.0 ^= self.0 >> SHIFTS.1;
        self.0 ^= self.0 << SHIFTS.2;
        (self.0 % k as u64) as usize
    }
}

/// The plan: the trip of each item and per trip the load and the client set.
struct Plan<'a> {
    weight: &'a [usize],
    client: &'a [usize],
    tour: &'a [i64],
    m: usize,
    cap: usize,
    trip: Vec<usize>,
    load: Vec<usize>,
    clients: Vec<usize>,
    per_client: Vec<Vec<usize>>,
    cost: i64,
}

impl<'a> Plan<'a> {
    fn put(&mut self, i: usize, t: usize) {
        if t == self.load.len() {
            self.load.push(0);
            self.clients.push(0);
            self.per_client.push(vec![0; self.m]);
        }
        self.cost -= self.tour[self.clients[t]];
        self.trip[i] = t;
        self.load[t] += self.weight[i];
        self.per_client[t][self.client[i]] += 1;
        if self.per_client[t][self.client[i]] == 1 {
            self.clients[t] |= 1 << self.client[i];
        }
        self.cost += self.tour[self.clients[t]];
    }

    fn take(&mut self, i: usize) {
        let t = self.trip[i];
        self.cost -= self.tour[self.clients[t]];
        self.load[t] -= self.weight[i];
        self.per_client[t][self.client[i]] -= 1;
        if self.per_client[t][self.client[i]] == 0 {
            self.clients[t] &= !(1 << self.client[i]);
        }
        self.cost += self.tour[self.clients[t]];
        self.trip[i] = usize::MAX;
    }

    /// The cheapest place for item i, an existing trip or a new one: the first
    /// trip that costs no more than a new one, so that emptied trips are reused.
    fn insert_best(&mut self, i: usize) {
        let fresh = self.load.len();
        let bit = 1 << self.client[i];
        let (mut best, mut extra) = (fresh, self.tour[bit]);
        for t in 0..fresh {
            if self.load[t] + self.weight[i] > self.cap {
                continue;
            }
            let d = self.tour[self.clients[t] | bit] - self.tour[self.clients[t]];
            if d < extra || (d == extra && best == fresh) {
                extra = d;
                best = t;
            }
        }
        self.put(i, best);
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<usize>().unwrap());
    let (m, n, cap) = (it.next().unwrap(), it.next().unwrap(), it.next().unwrap());
    let dist: Vec<Vec<usize>> = (0..=m)
        .map(|_| (0..=m).map(|_| it.next().unwrap()).collect())
        .collect();
    let (mut weight, mut client) = (vec![0usize; n], vec![0usize; n]);
    for i in 0..n {
        weight[i] = it.next().unwrap();
        client[i] = it.next().unwrap() - 1;
    }
    // Held-Karp over the clients: shortest walks from the depot through every subset
    let full = 1usize << m;
    let mut path = vec![UNREACHED; full * m];
    let mut tour = vec![0i64; full];
    for j in 0..m {
        path[(1 << j) * m + j] = dist[0][j + 1] as u16;
    }
    for s in 1..full {
        let mut best = UNREACHED as usize;
        // only the clients in s can end the walk, only the others can come next
        let mut js = s;
        while js != 0 {
            let j = js.trailing_zeros() as usize;
            js &= js - 1;
            let here = path[s * m + j] as usize;
            best = best.min(here + dist[j + 1][0]);
            let mut ks = !s & (full - 1);
            while ks != 0 {
                let k = ks.trailing_zeros() as usize;
                ks &= ks - 1;
                let at = (s | 1 << k) * m + k;
                let v = (here + dist[j + 1][k + 1]) as u16;
                if v < path[at] {
                    path[at] = v;
                }
            }
        }
        tour[s] = best as i64;
    }
    // a first plan by cheapest insertion; then rounds of removing some items
    // and putting them back in the cheapest places, undone when the cost grows
    // by more than a threshold that falls to zero
    let mut p = Plan {
        weight: &weight,
        client: &client,
        tour: &tour,
        m,
        cap,
        trip: vec![usize::MAX; n],
        load: Vec::new(),
        clients: Vec::new(),
        per_client: Vec::new(),
        cost: 0,
    };
    for i in 0..n {
        p.insert_best(i);
    }
    let mut rng = Rng(SEED);
    let (mut best_trip, mut best_cost, start) = (p.trip.clone(), p.cost, p.cost);
    let (mut removed, mut old): (Vec<usize>, Vec<usize>) = (Vec::new(), Vec::new());
    for round in 0..ROUNDS {
        let before = p.cost;
        removed.clear();
        old.clear();
        let kind = rng.below(KINDS);
        let count = 1 + rng.below(n.min(MOST));
        let pick = rng.below(n);
        let target = if kind == 1 {
            p.trip[pick]
        } else {
            client[pick]
        };
        for i in 0..n {
            if (kind == 1 && p.trip[i] == target) || (kind == 2 && client[i] == target) {
                removed.push(i);
                old.push(p.trip[i]);
            }
        }
        for _ in 0..if kind == 0 { count } else { 0 } {
            let i = rng.below(n);
            if !removed.contains(&i) {
                removed.push(i);
                old.push(p.trip[i]);
            }
        }
        for &i in &removed {
            p.take(i);
        }
        for k in (1..removed.len()).rev() {
            let r = rng.below(k + 1);
            removed.swap(k, r);
            old.swap(k, r);
        }
        for &i in &removed {
            p.insert_best(i);
        }
        let threshold = start * (ROUNDS - round) / ROUNDS / SHARE;
        if p.cost > before + threshold {
            for &i in &removed {
                p.take(i);
            }
            for (k, &i) in removed.iter().enumerate() {
                p.put(i, old[k]);
            }
        }
        if p.cost < best_cost {
            best_cost = p.cost;
            best_trip.copy_from_slice(&p.trip);
        }
    }
    // rebuild the best plan and print its non-empty trips, each route
    // recovered from the subset table
    let trips = best_trip.iter().max().unwrap() + 1;
    p.load = vec![0; trips];
    p.clients = vec![0; trips];
    p.per_client = vec![vec![0; m]; trips];
    p.cost = 0;
    for (i, &t) in best_trip.iter().enumerate() {
        p.put(i, t);
    }
    let used: Vec<usize> = (0..trips).filter(|&t| p.clients[t] != 0).collect();
    let mut out = String::new();
    writeln!(out, "{}\n", used.len()).unwrap();
    let mut total = 0i64;
    for &t in &used {
        let items: Vec<String> = (0..n)
            .filter(|&i| p.trip[i] == t)
            .map(|i| (i + 1).to_string())
            .collect();
        writeln!(out, "{}\n{}", items.join(" "), p.load[t]).unwrap();
        let mut s = p.clients[t];
        let length = tour[s];
        let mut last = (0..m)
            .find(|&j| s >> j & 1 == 1 && path[s * m + j] as i64 + dist[j + 1][0] as i64 == length)
            .unwrap();
        let mut route = Vec::new();
        while s != 0 {
            route.push(last + 1);
            let rest = s & !(1 << last);
            let mut prev = 0;
            if rest != 0 {
                prev = (0..m)
                    .find(|&j| {
                        rest >> j & 1 == 1
                            && path[rest * m + j] as usize + dist[j + 1][last + 1]
                                == path[s * m + last] as usize
                    })
                    .unwrap();
            }
            s = rest;
            last = prev;
        }
        let mut stops = vec!["0".to_string()];
        stops.extend(route.iter().rev().map(|c| c.to_string()));
        stops.push("0".to_string());
        writeln!(out, "{}\n{}\n", stops.join(" "), length).unwrap();
        total += length;
    }
    writeln!(out, "{}", total).unwrap();
    print!("{}", out);
}
