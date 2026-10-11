use std::io::{self, Read};

fn gcd(a: usize, b: usize) -> usize {
    if b == 0 {
        a
    } else {
        gcd(b, a % b)
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<usize> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let n = v[0];
    let stones = &v[1..1 + n];
    let mut order: Vec<usize> = (0..n).collect();
    order.sort_by_key(|&i| stones[i]);
    // a swap moves a stone K + 1 places, so K + 1 must divide every stone's
    // distance to its place, in one order or the other; all weights differ
    let mut best = 0;
    for down in [false, true] {
        let mut g = 0;
        for (place, &at) in order.iter().enumerate() {
            let target = if down { n - 1 - place } else { place };
            g = gcd(g, target.abs_diff(at));
        }
        best = best.max(if g > 0 { g - 1 } else { n - 1 });
    }
    println!("{}", best);
}
