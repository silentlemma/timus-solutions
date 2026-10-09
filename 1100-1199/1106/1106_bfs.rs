use std::collections::VecDeque;
use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tok = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<usize>().unwrap());
    let n = tok.next().unwrap();
    let mut adj = vec![Vec::new(); n + 1];
    for list in adj.iter_mut().skip(1) {
        list.extend(tok.by_ref().take_while(|&u| u != 0));
    }
    // colour a BFS tree of every component by depth parity: each member has a
    // tree neighbour, its parent or a child, in the other team
    let mut side: Vec<Option<bool>> = vec![None; n + 1];
    for root in 1..=n {
        if side[root].is_some() {
            continue;
        }
        side[root] = Some(true);
        let mut queue = VecDeque::from(vec![root]);
        while let Some(v) = queue.pop_front() {
            let next = side[v].map(|s| !s);
            for &u in &adj[v] {
                if side[u].is_none() {
                    side[u] = next;
                    queue.push_back(u);
                }
            }
        }
    }
    let team: Vec<String> = (1..=n)
        .filter(|&v| side[v] == Some(true))
        .map(|v| v.to_string())
        .collect();
    println!("{}\n{}", team.len(), team.join(" "));
}
