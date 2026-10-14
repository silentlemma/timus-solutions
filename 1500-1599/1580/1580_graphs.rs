use std::fmt::Write as _;
use std::io::{self, Read};

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut it = text
        .split_ascii_whitespace()
        .map(|w| w.parse::<i64>().unwrap());
    let (n, m) = (it.next().unwrap() as usize, it.next().unwrap() as usize);
    let mut edges = Vec::with_capacity(m);
    let mut adj: Vec<Vec<(usize, i64)>> = vec![Vec::new(); n];
    for _ in 0..m {
        let u = it.next().unwrap() as usize - 1;
        let v = it.next().unwrap() as usize - 1;
        let a = it.next().unwrap();
        edges.push((u, v, a));
        adj[u].push((v, a));
        adj[v].push((u, a));
    }
    // in halves of a rouble, each debt in a component is sign * t + base for
    // the debt t of its first student; an edge closing an odd cycle fixes t
    let (mut sign, mut base, mut twice) = (vec![0i64; n], vec![0i64; n], vec![0i64; n]);
    for start in 0..n {
        if sign[start] != 0 {
            continue;
        }
        sign[start] = 1;
        let mut comp = vec![start];
        let mut fixed: Option<i64> = None;
        let mut head = 0;
        while head < comp.len() {
            let v = comp[head];
            head += 1;
            for &(u, a) in &adj[v] {
                if sign[u] == 0 {
                    sign[u] = -sign[v];
                    base[u] = 2 * a - base[v];
                    comp.push(u);
                } else if sign[u] == sign[v] && fixed.is_none() {
                    fixed = Some((2 * a - base[u] - base[v]) / (2 * sign[v]));
                }
            }
        }
        let Some(t) = fixed else {
            // no odd cycle: one debt can move freely against its neighbours
            println!("IMPOSSIBLE");
            return;
        };
        for &v in &comp {
            twice[v] = sign[v] * t + base[v];
        }
    }
    // the claims may also contradict each other
    if edges.iter().any(|&(u, v, a)| twice[u] + twice[v] != 2 * a) {
        println!("IMPOSSIBLE");
        return;
    }
    let mut out = String::new();
    for t in twice {
        let half = if t % 2 != 0 { "50" } else { "00" };
        writeln!(
            out,
            "{}{}.{}",
            if t < 0 { "-" } else { "" },
            t.abs() / 2,
            half
        )
        .unwrap();
    }
    print!("{}", out);
}
