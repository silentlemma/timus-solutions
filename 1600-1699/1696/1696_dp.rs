use std::io::{self, Read};

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let v: Vec<i64> = text.split_ascii_whitespace().map(|w| w.parse().unwrap()).collect();
    let (n, k, p) = (v[0] as usize, v[1] as usize, v[2]);
    // salaries by rank must avoid a strictly decreasing triple; the state is
    // a, the largest salary so far, and b, the largest salary that follows a
    // larger one (0 if none); ways[a][b] counts such prefixes modulo p
    let mut ways = vec![vec![0i64; k + 1]; k + 1];
    for z in 1..=k {
        ways[z][0] = 1 % p;
    }
    for _ in 1..n {
        let mut next = vec![vec![0i64; k + 1]; k + 1];
        // a new salary z is allowed when z >= b, and turns (a, b) into (a, z) if
        // z < a, or into (z, b) if z >= a
        // z < a: (a, b) -> (a, z) for every b <= z, a prefix sum along the row
        for a in 1..=k {
            let mut running = 0;
            for c in 0..a {
                running = (running + ways[a][c]) % p;
                if c > 0 {
                    next[a][c] = running;
                }
            }
        }
        // z >= a: (a, b) -> (z, b) for every a <= z, a prefix sum down the column
        for b in 0..k {
            let mut running = 0;
            for z in b + 1..=k {
                running = (running + ways[z][b]) % p;
                next[z][b] = (next[z][b] + running) % p;
            }
        }
        ways = next;
    }
    let total = ways.iter().flatten().fold(0, |acc, &x| (acc + x) % p);
    // month total + 1 counted from the first month, numbered 1..p in its year
    println!("{}", total + 1);
}
