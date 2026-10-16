use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_ascii_whitespace().map(|w| w.parse::<i64>().unwrap());
    let mut next = || words.next().unwrap();
    let (n, k) = (next() as usize, next() as usize);
    let mut xs = vec![0i64; n];
    let mut ys = vec![0i64; n];
    for i in 0..n {
        xs[i] = next();
        ys[i] = next();
    }
    // a ball of diameter D hits the pins whose centres lie in a strip of width
    // D + 1 along its path, so the narrowest strip holding k centres decides, and
    // one side of that strip runs along two centres, so only those directions
    let mut best = if k > 1 { f64::INFINITY } else { 0.0 };
    let mut across = vec![0i64; n];
    for i in 0..n {
        for j in i + 1..n {
            let (dx, dy) = (xs[j] - xs[i], ys[j] - ys[i]);
            for t in 0..n {
                across[t] = dx * ys[t] - dy * xs[t];
            }
            across.sort_unstable();
            let gap = (0..=n - k).map(|t| across[t + k - 1] - across[t]).min().unwrap();
            best = best.min(gap as f64 / (dx as f64).hypot(dy as f64));
        }
    }
    // a ball of any size will do when the strip is no wider than a pin
    if best > 1.0 {
        println!("{:.10}", best - 1.0);
    } else {
        println!("0.000000");
    }
}
