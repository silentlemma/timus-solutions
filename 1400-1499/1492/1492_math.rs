use std::fmt::Write as _;
use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<i64> = input
        .split_ascii_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();
    let n = v[0] as usize;
    let xs: Vec<i64> = (0..n).map(|i| v[1 + 2 * i]).collect();
    let ys: Vec<i64> = (0..n).map(|i| v[2 + 2 * i]).collect();

    // the segment of f that holds x, or the one to its right
    let segment = |x: i64| xs.partition_point(|&p| p <= x).saturating_sub(1).min(n - 2);
    let value = |x: i64| {
        let j = segment(x);
        ys[j] as f64 + (ys[j + 1] - ys[j]) as f64 * (x - xs[j]) as f64 / (xs[j + 1] - xs[j]) as f64
    };

    // f(x) = E(x) + O(x) with E(x) = (f(x) + f(-x)) / 2 and
    // O(x) = (f(x) - f(-x)) / 2; both are linear between the points of f
    // and their mirror images
    let mut points: Vec<i64> = xs.iter().flat_map(|&x| [x, -x]).collect();
    points.sort_unstable();
    points.dedup();

    let mut out = String::from("Yes\n");
    for sign in [1i64, -1] {
        // the even part, then the odd one; the slope of a part between two
        // neighbouring points is (a/b -+ c/d) / 2 with the slope a/b of f at
        // x and c/d of f at -x, numerator and denominator below 2 * 10^9
        let slopes: Vec<(i64, i64)> = points
            .windows(2)
            .map(|w| {
                let (j, i) = (segment(w[0]), segment(-w[1]));
                let (a, b) = (ys[j + 1] - ys[j], xs[j + 1] - xs[j]);
                let (c, d) = (ys[i + 1] - ys[i], xs[i + 1] - xs[i]);
                (a * d - sign * c * b, 2 * b * d)
            })
            .collect();
        for (k, &x) in points.iter().enumerate() {
            let bend = k == 0
                || k + 1 == points.len()
                || slopes[k - 1].0 * slopes[k].1 != slopes[k].0 * slopes[k - 1].1;
            if bend {
                // only real bends stay
                let y = (value(x) + sign as f64 * value(-x)) / 2.0;
                writeln!(out, "{:.6} {:.6}", x as f64, y).unwrap();
            }
        }
    }
    print!("{}", out);
}
