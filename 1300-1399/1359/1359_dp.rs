use std::io::{self, Read};

const GRAVITY: f64 = 10.0;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<usize>().unwrap());
    let (n, m) = (it.next().unwrap(), it.next().unwrap());
    // the speed at depth d is sqrt(2 g d), whatever the way down was
    let speed: Vec<f64> = (0..=m).map(|d| (2.0 * GRAVITY * d as f64).sqrt()).collect();
    // best holds the least time to reach each depth and distance to the left,
    // where a board with constant acceleration takes 2 L / (v1 + v2)
    let mut best = vec![vec![f64::INFINITY; n + 1]; m + 1];
    best[0][0] = 0.0;
    for d in 1..=m {
        for e in 0..d {
            let vs = speed[d] + speed[e];
            for x in 0..=n {
                let t = best[e][x];
                if t.is_infinite() {
                    continue;
                }
                for y in x..=n {
                    let c = t + 2.0 * ((y - x) as f64).hypot((d - e) as f64) / vs;
                    if c < best[d][y] {
                        best[d][y] = c;
                    }
                }
            }
        }
    }
    println!("{:.4}", best[m][n]);
}
