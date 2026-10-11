use std::io::{self, BufWriter, Read, Write};

fn gcd(a: i64, b: i64) -> i64 {
    if b == 0 {
        a
    } else {
        gcd(b, a % b)
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<usize>().unwrap());
    let n = it.next().unwrap();
    let mut teeth = vec![0i64; n + 1];
    let mut adj = vec![Vec::new(); n + 1];
    for i in 1..=n {
        teeth[i] = it.next().unwrap() as i64;
        loop {
            let j = it.next().unwrap();
            if j == 0 {
                break;
            }
            // a link may be listed at one end only, so store it both ways
            adj[i].push(j);
            adj[j].push(i);
        }
    }
    let (root, speed) = (it.next().unwrap(), it.next().unwrap() as i64);
    // meshed gears share the speed of their rims, speed * teeth, and turn
    // opposite ways; so gear j turns at +-speed * teeth[root] / teeth[j]
    let rim = speed * teeth[root];
    let mut sign = vec![0i64; n + 1];
    sign[root] = 1;
    let mut queue = vec![root];
    let mut head = 0;
    while head < queue.len() {
        let u = queue[head];
        head += 1;
        for &v in &adj[u] {
            if sign[v] == 0 {
                sign[v] = -sign[u];
                queue.push(v);
            }
        }
    }
    let mut out = BufWriter::new(io::stdout().lock());
    for i in 1..=n {
        if sign[i] == 0 {
            writeln!(out, "0/1").unwrap();
        } else {
            let g = gcd(rim, teeth[i]);
            writeln!(out, "{}/{}", sign[i] * rim / g, teeth[i] / g).unwrap();
        }
    }
}
