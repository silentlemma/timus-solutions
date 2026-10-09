use std::collections::BTreeSet;
use std::io::{self, Read};

const JURY: i32 = 255;

struct Plot {
    w: i32,
    s: i32,
    x: i32,
    y: i32,
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<i32>().unwrap());
    let mut next = || it.next().unwrap();
    let (size, park, m) = (next(), next(), next());
    let plots: Vec<Plot> = (0..m)
        .map(|_| Plot {
            w: next(),
            s: next(),
            x: next(),
            y: next(),
        })
        .collect();
    let top = size - park + 1;
    // sliding the park left only drops plots until its left side reaches a
    // plot's right side or the border, so only those positions are tried
    let mut xs = BTreeSet::from([1]);
    let mut ys = BTreeSet::from([1]);
    for p in &plots {
        if p.x + p.s <= top {
            xs.insert(p.x + p.s);
        }
        if p.y + p.s <= top {
            ys.insert(p.y + p.s);
        }
    }
    let mut best = JURY;
    for &px in &xs {
        for &py in &ys {
            let worst = plots
                .iter()
                .filter(|p| px < p.x + p.s && p.x < px + park && py < p.y + p.s && p.y < py + park)
                .map(|p| p.w)
                .fold(1, i32::max);
            best = best.min(worst);
        }
    }
    if best == JURY {
        println!("IMPOSSIBLE");
    } else {
        println!("{}", best);
    }
}
