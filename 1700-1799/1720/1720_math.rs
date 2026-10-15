use std::io::{self, Read};

// numbers 1 .. t that are sums of contests: k contests give [kx, ky],
// once k (y - x) >= x - 1 the next interval touches this one, so from
// the first such k on everything is covered, and before it they are apart
fn covered(t: i64, x: i64, y: i64) -> i64 {
    if t < x {
        return 0;
    }
    if y == x {
        return t / x;
    }
    let joined = ((x - 1 + (y - x) - 1) / (y - x)).max(1);
    let full = (joined - 1).min(t / y); // the intervals that end by t
    let mut count = (y - x) * (full * (full + 1) / 2) + full;
    let k = full + 1;
    if k <= joined - 1 && k <= t / x {
        count += t - k * x + 1;
    }
    if joined <= t / x {
        count += t - joined * x + 1;
    }
    count
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut words = text.split_ascii_whitespace().map(|w| w.parse::<i64>().unwrap());
    let mut next = || words.next().unwrap();
    let (x, y, low, high) = (next(), next(), next(), next());
    println!("{}", covered(high, x, y) - covered(low - 1, x, y));
}
