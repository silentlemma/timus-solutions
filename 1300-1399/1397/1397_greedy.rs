use std::fmt::Write as _;
use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<f64>().unwrap());
    let mut out = String::new();
    while let Some(n) = it.next() {
        let m = 2 * n as usize;
        let pts: Vec<(f64, f64)> = (0..m)
            .map(|_| (it.next().unwrap(), it.next().unwrap()))
            .collect();
        // total[i]: the sum of distances from point i to all the others
        let mut total = vec![0.0f64; m];
        for i in 0..m {
            for j in i + 1..m {
                let (dx, dy) = (pts[i].0 - pts[j].0, pts[i].1 - pts[j].1);
                let d = (dx * dx + dy * dy).sqrt();
                total[i] += d;
                total[j] += d;
            }
        }
        // a player's score is half the totals of the own points minus the
        // distances to the other colour, which both sides share: take the
        // largest total left, in turns
        total.sort_by(|a, b| b.partial_cmp(a).unwrap());
        let diff: f64 = total
            .iter()
            .enumerate()
            .map(|(i, t)| if i % 2 == 0 { *t } else { -t })
            .sum();
        writeln!(out, "{:.3}", (diff / 2.0).abs()).unwrap();
    }
    print!("{}", out);
}
