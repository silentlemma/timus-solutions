use std::io::{self, Read, Write};

// a pair of v without a winner yet
fn open(incident: &[Vec<usize>], winner: &[usize], v: usize) -> usize {
    *incident[v].iter().find(|&&i| winner[i] == 0).unwrap()
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace().map(|t| t.parse::<usize>().unwrap());
    let (n, k) = (it.next().unwrap(), it.next().unwrap());
    let mut ends = Vec::with_capacity(n);
    let mut incident = vec![Vec::new(); k + 1];
    for i in 0..n {
        let (x, y) = (it.next().unwrap(), it.next().unwrap());
        ends.push(x + y);
        incident[x].push(i);
        incident[y].push(i);
    }
    let mut winner = vec![0usize; n];
    let mut degree: Vec<usize> = incident.iter().map(|e| e.len()).collect();
    // every team may win at most one pair: a team with a single open pair takes
    // it, which never hurts, and the pair is closed for the other team
    let mut leaves: Vec<usize> = (1..=k).filter(|&v| degree[v] == 1).collect();
    while let Some(v) = leaves.pop() {
        if degree[v] != 1 {
            continue;
        }
        let i = open(&incident, &winner, v);
        let u = ends[i] - v; // ends[i] holds the sum of both teams
        winner[i] = v;
        degree[v] = 0;
        degree[u] -= 1;
        if degree[u] == 1 {
            leaves.push(u);
        }
    }
    // what is left must be disjoint cycles (every degree 2); each cycle is walked
    // and every pair is won by the team it leads to
    if degree.iter().any(|&d| d > 2) {
        println!("No");
        return;
    }
    for start in 1..=k {
        if degree[start] != 2 {
            continue;
        }
        let mut v = start;
        loop {
            let i = open(&incident, &winner, v);
            let u = ends[i] - v;
            winner[i] = u;
            degree[v] -= 1;
            degree[u] -= 1;
            v = u;
            if v == start {
                break;
            }
        }
    }
    let mut out = String::from("Yes\n");
    for w in winner {
        out.push_str(&w.to_string());
        out.push('\n');
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}
