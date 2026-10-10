use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tok = input.split_ascii_whitespace();
    let n: usize = tok.next().unwrap().parse().unwrap();
    let pts: Vec<(f64, f64)> = (0..n)
        .map(|_| {
            let x: f64 = tok.next().unwrap().parse().unwrap();
            let y: f64 = tok.next().unwrap().parse().unwrap();
            (x, y)
        })
        .collect();
    let dist = |a: usize, b: usize| (pts[a].0 - pts[b].0).hypot(pts[a].1 - pts[b].1);
    // a shortest path never crosses itself, so on a convex polygon the visited
    // camps form an arc and the path ends at one of its ends; at[i] and
    // at_end[i] are the best paths over the arc from camp i, ending at either end
    let mut at = vec![0.0f64; n];
    let mut at_end = vec![0.0f64; n];
    for length in 1..n {
        let mut grow = vec![f64::INFINITY; n];
        let mut grow_end = vec![f64::INFINITY; n];
        for i in 0..n {
            let (j, before, after) = ((i + length - 1) % n, (i + n - 1) % n, (i + length) % n);
            for (cost, here) in [(at[i], i), (at_end[i], j)] {
                grow[before] = grow[before].min(cost + dist(here, before));
                grow_end[i] = grow_end[i].min(cost + dist(here, after));
            }
        }
        at = grow;
        at_end = grow_end;
    }
    let best = at
        .iter()
        .chain(at_end.iter())
        .fold(f64::INFINITY, |b, &v| b.min(v));
    println!("{:.3}", best);
}
