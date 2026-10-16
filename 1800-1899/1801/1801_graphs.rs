use std::collections::HashMap;
use std::io::{self, Read, Write};

const NONE: usize = usize::MAX;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_ascii_whitespace();
    let groups: usize = words.next().unwrap().parse().unwrap();
    let pots: usize = words.next().unwrap().parse().unwrap();
    let total = groups * pots;
    // each team is an edge from its pot to its party; a colouring of the
    // edges with one colour per group, never repeated at a vertex, is an
    // answer
    let mut team = Vec::with_capacity(total);
    let mut party = Vec::with_capacity(total);
    let mut party_id: HashMap<&str, usize> = HashMap::new();
    let mut size: Vec<usize> = Vec::new();
    for _ in 0..total {
        team.push(words.next().unwrap());
        let name = words.next().unwrap();
        let next_id = size.len();
        let id = *party_id.entry(name).or_insert(next_id);
        if id == size.len() {
            size.push(0);
        }
        size[id] += 1;
        party.push(id);
    }
    if size.iter().any(|&s| s > groups) {
        println!("No");
        return;
    }
    let pot: Vec<usize> = (0..total).map(|e| e / groups).collect();
    // at_pot[u * groups + c], at_party[v * groups + c]: the edge of colour c
    let mut at_pot = vec![NONE; pots * groups];
    let mut at_party = vec![NONE; size.len() * groups];
    let mut colour = vec![0usize; total];
    let mut path: Vec<usize> = Vec::new();
    for e in 0..total {
        let (u, v) = (pot[e], party[e]);
        let a = (0..groups).find(|&c| at_pot[u * groups + c] == NONE).unwrap();
        let b = (0..groups).find(|&c| at_party[v * groups + c] == NONE).unwrap();
        // colour a is free at the pot and b at the party; swap a and b along
        // the path from the pot that alternates b and a, which cannot reach
        // the party, and b becomes free at both ends
        path.clear();
        let (mut at, mut want, mut on_pot) = (u, b, true);
        while a != b {
            let f = if on_pot { at_pot[at * groups + want] } else { at_party[at * groups + want] };
            if f == NONE {
                break;
            }
            path.push(f);
            at = if on_pot { party[f] } else { pot[f] };
            on_pot = !on_pot;
            want = a + b - want;
        }
        for &f in path.iter() {
            at_pot[pot[f] * groups + colour[f]] = NONE;
            at_party[party[f] * groups + colour[f]] = NONE;
        }
        for &f in path.iter().chain(std::iter::once(&e)) {
            let c = if f == e { b } else { a + b - colour[f] };
            colour[f] = c;
            at_pot[pot[f] * groups + c] = f;
            at_party[party[f] * groups + c] = f;
        }
    }
    let mut members = vec![vec![""; pots]; groups];
    for e in 0..total {
        members[colour[e]][pot[e]] = team[e];
    }
    let mut out = String::from("Yes\n");
    for group in members.iter() {
        out.push('\n');
        for name in group.iter() {
            out.push_str(name);
            out.push('\n');
        }
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}
