use std::collections::HashMap;
use std::fmt::Write;
use std::io::{self, Read};

struct Search {
    adj: Vec<usize>,
    caller_of: Vec<Option<usize>>, // callee of each caller already busy
}

impl Search {
    fn place(&mut self, person: usize, informed: usize, seen: &mut usize) -> bool {
        for caller in 0..self.adj.len() {
            if self.adj[person] >> caller & 1 == 1
                && informed >> caller & 1 == 1
                && *seen >> caller & 1 == 0
            {
                *seen |= 1 << caller;
                let free = match self.caller_of[caller] {
                    None => true,
                    Some(other) => self.place(other, informed, seen),
                };
                if free {
                    self.caller_of[caller] = Some(person);
                    return true;
                }
            }
        }
        false
    }

    // who calls whom so that every person in fresh is called by a
    // different informed neighbour; None if that cannot be done
    fn calls(&mut self, informed: usize, fresh: usize) -> Option<Vec<(usize, usize)>> {
        self.caller_of = vec![None; self.adj.len()];
        for person in 0..self.adj.len() {
            let mut seen = 0;
            if fresh >> person & 1 == 1 && !self.place(person, informed, &mut seen) {
                return None;
            }
        }
        Some(
            (0..self.adj.len())
                .filter_map(|c| self.caller_of[c].map(|p| (c, p)))
                .collect(),
        )
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let words: Vec<&str> = input.split_ascii_whitespace().collect();
    let m: usize = words[1].parse().unwrap();
    let mut index: HashMap<&str, usize> = HashMap::new();
    let mut names: Vec<&str> = Vec::new();
    let (ends, leader) = (&words[2..2 + 2 * m], words[2 + 2 * m]);
    for &name in ends.iter().chain(std::iter::once(&leader)) {
        if !index.contains_key(name) {
            index.insert(name, names.len());
            names.push(name);
        }
    }
    let mut adj = vec![0usize; names.len()];
    for pair in ends.chunks(2) {
        let (a, b) = (index[pair[0]], index[pair[1]]);
        adj[a] |= 1 << b;
        adj[b] |= 1 << a;
    }
    let full = (1usize << names.len()) - 1;
    let start = 1usize << index[leader];
    let mut search = Search {
        adj,
        caller_of: Vec::new(),
    };
    // breadth-first search over the sets of people who know the news
    let mut came: Vec<Option<(usize, Vec<(usize, usize)>)>> = vec![None; full + 1];
    let mut queue = vec![start];
    let mut head = 0;
    while head < queue.len() && full != start && came[full].is_none() {
        let informed = queue[head];
        head += 1;
        let mut reach = 0;
        for p in 0..names.len() {
            if informed >> p & 1 == 1 {
                reach |= search.adj[p];
            }
        }
        reach &= !informed;
        let mut fresh = reach;
        while fresh > 0 {
            let next = informed | fresh;
            if came[next].is_none() {
                if let Some(plan) = search.calls(informed, fresh) {
                    came[next] = Some((informed, plan));
                    queue.push(next);
                }
            }
            fresh = (fresh - 1) & reach;
        }
    }
    let mut steps = Vec::new();
    let mut state = full;
    while state != start {
        let (before, plan) = came[state].as_ref().unwrap();
        steps.push(plan);
        state = *before;
    }
    let mut out = String::new();
    writeln!(out, "{}", steps.len()).unwrap();
    for plan in steps.iter().rev() {
        writeln!(out, "{}", plan.len()).unwrap();
        for &(a, b) in plan.iter() {
            writeln!(out, "{} {}", names[a], names[b]).unwrap();
        }
    }
    print!("{}", out);
}
