use std::io::{self, Read};

// sum over even e <= n of tz(e) - 1, that is sum over y <= n/2 of tz(y)
fn evens(n: i64) -> i64 {
    let m = n / 2;
    m - m.count_ones() as i64
}

// tz(x) - 1 for an even x, 0 for an odd one
fn extra(x: i64) -> i64 {
    if x % 2 == 0 {
        x.trailing_zeros() as i64 - 1
    } else {
        0
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut v: Vec<i64> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    v.sort_unstable();
    let (i, j) = (v[0], v[1]);
    // numbers run through the tree in order, so a node's height is the count of
    // trailing zeros; between k and k + 1 the even one is an ancestor of the
    // odd leaf, and the message waits one day per node in between
    let days = if i == j {
        0
    } else {
        2 * (evens(j) - evens(i - 1)) - extra(i) - extra(j)
    };
    println!("{}", days);
}
