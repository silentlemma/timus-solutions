use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tok = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<usize>().unwrap());
    let (n, m) = (tok.next().unwrap(), tok.next().unwrap());
    let total = 2 * n;
    let mut near = vec![Vec::new(); total + 1];
    for _ in 0..m {
        let (a, b) = (tok.next().unwrap(), tok.next().unwrap());
        near[a].push(b);
        near[b].push(a);
    }
    // similar problems must go to different rounds: colour every component of
    // the conflict graph in two colours, or give up on an odd cycle
    let mut colour: Vec<Option<usize>> = vec![None; total + 1];
    let mut comps: Vec<Vec<usize>> = Vec::new();
    for start in 1..=total {
        if colour[start].is_some() {
            continue;
        }
        colour[start] = Some(0);
        let (mut members, mut stack) = (vec![start], vec![start]);
        while let Some(v) = stack.pop() {
            let cv = colour[v].unwrap();
            for &w in &near[v] {
                match colour[w] {
                    None => {
                        colour[w] = Some(1 - cv);
                        members.push(w);
                        stack.push(w);
                    }
                    Some(cw) if cw == cv => {
                        println!("IMPOSSIBLE");
                        return;
                    }
                    _ => {}
                }
            }
        }
        comps.push(members);
    }
    // each component sends one of its colours to the first round; reach[k][s]
    // tells whether the first k components can give it s problems
    let c = comps.len();
    let sizes: Vec<[usize; 2]> = comps
        .iter()
        .map(|members| {
            let mut size = [0, 0];
            for &v in members {
                size[colour[v].unwrap()] += 1;
            }
            size
        })
        .collect();
    let mut reach = vec![vec![false; n + 1]; c + 1];
    reach[0][0] = true;
    for k in 0..c {
        for s in 0..=n {
            if reach[k][s] {
                for size in sizes[k] {
                    if s + size <= n {
                        reach[k + 1][s + size] = true;
                    }
                }
            }
        }
    }
    if !reach[c][n] {
        println!("IMPOSSIBLE");
        return;
    }
    let mut first = vec![false; total + 1];
    let mut s = n;
    for k in (0..c).rev() {
        let side = if s >= sizes[k][0] && reach[k][s - sizes[k][0]] {
            0
        } else {
            1
        };
        for &v in &comps[k] {
            if colour[v] == Some(side) {
                first[v] = true;
            }
        }
        s -= sizes[k][side];
    }
    for round in [true, false] {
        let line: Vec<String> = (1..=total)
            .filter(|&v| first[v] == round)
            .map(|v| v.to_string())
            .collect();
        println!("{}", line.join(" "));
    }
}
