use std::io::{self, Read};

const RADIUS: usize = 3; // the radius follows the three coordinates

fn find(parent: &mut [usize], mut v: usize) -> usize {
    while parent[v] != v {
        parent[v] = parent[parent[v]];
        v = parent[v];
    }
    v
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let data: Vec<i64> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let k = data[0] as usize;
    let ball = |i: usize| &data[1 + (RADIUS + 1) * i..=(RADIUS + 1) * (i + 1)];
    let mut parent: Vec<usize> = (0..k).collect();
    // two balls share more than one point when the centres are closer than r1 + r2
    for i in 0..k {
        for j in i + 1..k {
            let (a, b) = (ball(i), ball(j));
            let d2: i64 = (0..RADIUS).map(|t| (a[t] - b[t]) * (a[t] - b[t])).sum();
            let s = a[RADIUS] + b[RADIUS];
            if d2 < s * s {
                let root = find(&mut parent, i);
                let other = find(&mut parent, j);
                parent[other] = root;
            }
        }
    }
    // each group lists its planets in order, and groups come by their first planet
    let mut groups: Vec<Vec<usize>> = vec![Vec::new(); k];
    for v in 0..k {
        let root = find(&mut parent, v);
        groups[root].push(v);
    }
    let mut lists: Vec<Vec<usize>> = groups.into_iter().filter(|g| !g.is_empty()).collect();
    lists.sort();
    let lines: Vec<String> = lists
        .iter()
        .map(|g| {
            g.iter()
                .map(|v| v.to_string())
                .collect::<Vec<_>>()
                .join(", ")
        })
        .collect();
    println!("{}", lines.join("\n"));
}
