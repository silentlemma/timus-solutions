use std::io::{self, Read};

const INF: u64 = u64::MAX;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let n: usize = it.next().unwrap().parse().unwrap();
    let m: usize = it.next().unwrap().parse().unwrap();
    // each update: (new version, size, first letter of its kind)
    let mut updates: Vec<Vec<(usize, u64, u8)>> = vec![Vec::new(); n + 1];
    for _ in 0..m {
        let x: usize = it.next().unwrap().parse().unwrap();
        let y: usize = it.next().unwrap().parse().unwrap();
        let d: u64 = it.next().unwrap().parse().unwrap();
        let kind = it.next().unwrap().as_bytes()[0];
        updates[x].push((y, d, kind));
    }
    // updates only go up, so the versions can be taken in order; the
    // client is either still licensed (0) or already pirated (1)
    let mut best = vec![[INF, INF]; n + 1];
    best[1][0] = 0;
    for v in 1..=n {
        for &(to, size, kind) in &updates[v] {
            for state in 0..2 {
                if best[v][state] == INF || (kind == b'L' && state == 1) {
                    continue;
                }
                let after = if kind == b'P' { 1 } else { state };
                best[to][after] = best[to][after].min(best[v][state] + size);
            }
        }
    }
    let answer = best[n][0].min(best[n][1]);
    if answer == INF {
        println!("Offline");
    } else {
        println!("Online\n{}", answer);
    }
}
