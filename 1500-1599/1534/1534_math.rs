use std::io::{self, Read};

fn main() {
    let mut s = String::new();
    io::stdin().read_to_string(&mut s).unwrap();
    let v: Vec<i64> = s
        .split_ascii_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();
    let (k, l, n) = (v[0], v[1], v[2]);
    let d = k - l;
    // with W wins and R losses the team has n + 2W - R points; the goals
    // split into a common part, scored and conceded alike, plus at least
    // one goal of margin per win and per loss
    let (mut best, mut worst) = if d >= 0 {
        // no losses: the margin d covers up to d wins, the rest are draws
        (n + 2 * d.min(n), if d == 0 { n } else { n + 2 })
    } else {
        // no wins: up to -d losses, at least one
        (n - 1, n - (-d).min(n))
    };
    if k >= 1 && l >= 1 && n >= 2 {
        // wins and losses together: one goal each is enough, so one loss
        // and up to k wins, or one win and up to l losses
        best = best.max(n - 1 + 2 * k.min(n - 1));
        worst = worst.min(n + 2 - l.min(n - 1));
    }
    println!("{} {}", best, worst);
}
