use std::collections::BTreeMap;
use std::io::{self, BufWriter, Read, Write};

fn main() {
    const TEAM_SIZE: usize = 3;
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_ascii_whitespace();
    let teams: usize = tokens.next().unwrap().parse().unwrap();
    // every name gets a number; the ordered map keeps the output sorted
    let mut ids = BTreeMap::new();
    let mut mates: Vec<Vec<usize>> = Vec::with_capacity(TEAM_SIZE * teams);
    for _ in 0..teams {
        let mut team = [0; TEAM_SIZE];
        for id in &mut team {
            let name = tokens.next().unwrap();
            let next_id = ids.len();
            *id = *ids.entry(name).or_insert(next_id);
            if *id == mates.len() {
                mates.push(Vec::new());
            }
        }
        for &a in &team {
            for &b in &team {
                if a != b {
                    mates[a].push(b);
                }
            }
        }
    }
    // breadth-first search from the champion over shared teams
    let mut distance = vec![None; ids.len()];
    let mut queue = Vec::with_capacity(ids.len());
    if let Some(&source) = ids.get("Isenbaev") {
        distance[source] = Some(0);
        queue.push(source);
    }
    let mut head = 0;
    while head < queue.len() {
        let current = queue[head];
        head += 1;
        for &next in &mates[current] {
            if distance[next].is_none() {
                distance[next] = Some(distance[current].unwrap() + 1);
                queue.push(next);
            }
        }
    }
    let mut out = BufWriter::new(io::stdout().lock());
    for (name, id) in ids {
        match distance[id] {
            Some(value) => writeln!(out, "{} {}", name, value).unwrap(),
            None => writeln!(out, "{} undefined", name).unwrap(),
        }
    }
}
