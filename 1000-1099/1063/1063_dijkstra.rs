use std::cmp::Reverse;
use std::collections::{BinaryHeap, HashMap};
use std::io::{self, Read};

const FACES: usize = 6;
const MASKS: u64 = 1 << FACES;

// the faces split into connected groups, the faces that have dominoes and
// the faces of odd degree
#[derive(Clone, Copy)]
struct State {
    group: [usize; FACES],
    active: u32,
    odd: u32,
}

// relabels the groups in order of first appearance and packs the state
fn normalize(s: &mut State) -> u64 {
    let mut name = [usize::MAX; FACES];
    let mut next = 0;
    let mut code = 0u64;
    for v in 0..FACES {
        if name[s.group[v]] == usize::MAX {
            name[s.group[v]] = next;
            next += 1;
        }
        code = code * FACES as u64 + name[s.group[v]] as u64;
    }
    for v in 0..FACES {
        s.group[v] = name[s.group[v]];
    }
    (code * MASKS + s.active as u64) * MASKS + s.odd as u64
}

fn join(s: &mut State, a: usize, b: usize) {
    let (ga, gb) = (s.group[a], s.group[b]);
    for g in s.group.iter_mut() {
        if *g == gb {
            *g = ga;
        }
    }
    s.active |= 1 << a | 1 << b;
    s.odd ^= 1 << a ^ 1 << b;
}

fn done(s: &State) -> bool {
    let mut groups = (0..FACES)
        .filter(|&v| s.active >> v & 1 == 1)
        .map(|v| s.group[v]);
    let first = groups.next();
    groups.all(|g| Some(g) == first) && s.odd.count_ones() <= 2
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<usize> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let n = v[0];
    let mut start = State {
        group: std::array::from_fn(|v| v),
        active: 0,
        odd: 0,
    };
    for k in 0..n {
        join(&mut start, v[1 + 2 * k] - 1, v[2 + 2 * k] - 1);
    }
    // Dijkstra over the states: adding the domino (a, b) costs a + b, joins
    // the groups of a and b and flips the parity of both faces
    let mut dist: HashMap<u64, usize> = HashMap::new();
    let mut states: HashMap<u64, State> = HashMap::new();
    let mut parent: HashMap<u64, (u64, usize, usize)> = HashMap::new();
    let mut key = normalize(&mut start);
    dist.insert(key, 0);
    states.insert(key, start);
    let mut heap = BinaryHeap::new();
    heap.push(Reverse((0usize, key)));
    while let Some(Reverse((d, k))) = heap.pop() {
        if d > dist[&k] {
            continue;
        }
        if done(&states[&k]) {
            key = k;
            break;
        }
        for a in 0..FACES {
            for b in a + 1..FACES {
                let mut next = states[&k];
                join(&mut next, a, b);
                let nk = normalize(&mut next);
                let cost = d + (a + 1) + (b + 1);
                if dist.get(&nk).map_or(true, |&old| cost < old) {
                    dist.insert(nk, cost);
                    states.insert(nk, next);
                    parent.insert(nk, (k, a + 1, b + 1));
                    heap.push(Reverse((cost, nk)));
                }
            }
        }
    }
    let mut added = Vec::new();
    let mut k = key;
    while let Some(&(prev, a, b)) = parent.get(&k) {
        added.push((a, b));
        k = prev;
    }
    let mut out = format!("{}\n{}\n", dist[&key], added.len());
    for (a, b) in added {
        out.push_str(&format!("{} {}\n", a, b));
    }
    print!("{}", out);
}
