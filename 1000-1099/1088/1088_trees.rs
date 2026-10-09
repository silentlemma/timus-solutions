use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<i64> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let [d, e, f, dp, ep, h] = v[..] else {
        return;
    };
    // pier p - 1 written in F bits is the path to it, a left turn being 1 and
    // the first turn the highest bit; a stone k hours from the sea is that
    // path without its last k turns
    let (mut a, mut depth_a) = ((ep - 1) >> e, f - e);
    let (mut b, mut depth_b) = ((dp - 1) >> d, f - d);
    let mut hours = 0;
    while depth_a > depth_b {
        a >>= 1;
        depth_a -= 1;
        hours += 1;
    }
    while depth_b > depth_a {
        b >>= 1;
        depth_b -= 1;
        hours += 1;
    }
    while a != b {
        a >>= 1;
        b >>= 1;
        hours += 2;
    }
    println!("{}", if hours <= h { "YES" } else { "NO" });
}
