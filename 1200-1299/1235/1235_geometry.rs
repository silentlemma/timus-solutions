use std::io::{self, Read};

const HEADER: usize = 3;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<i32> = input
        .split_ascii_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();
    let (w, h) = (v[1], v[2]);
    let trees: Vec<(i32, i32)> = v[HEADER..].chunks(2).map(|c| (c[0], c[1])).collect();
    // a largest square slides left and down until its sides meet a tree or
    // the park border, so its corner has x = 0 or a tree x and y = 0 or a tree y
    let xs: Vec<i32> = std::iter::once(0)
        .chain(trees.iter().map(|t| t.0))
        .collect();
    let ys: Vec<i32> = std::iter::once(0)
        .chain(trees.iter().map(|t| t.1))
        .collect();
    let mut best = (0, 0, 0);
    for &p in &xs {
        for &q in &ys {
            let mut side = (w - p).min(h - q);
            // a tree up and to the right of the corner is inside unless the
            // side stops at its larger distance
            for &(x, y) in &trees {
                if x > p && y > q {
                    side = side.min((x - p).max(y - q));
                }
            }
            if side > best.2 {
                best = (p, q, side);
            }
        }
    }
    println!("{} {} {}", best.0, best.1, best.2);
}
