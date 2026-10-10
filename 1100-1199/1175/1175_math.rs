use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<i64>().unwrap());
    let mut next = || it.next().unwrap();
    let (a1, a2, a3, a4) = (next(), next(), next(), next());
    let (b1, b2, c) = (next(), next(), next());
    let first = (next(), next());
    let step = |(x, y): (i64, i64)| {
        let mut h = a1 * x * y + a2 * x + a3 * y + a4;
        if h > b1 && h > b2 && c > 0 {
            h -= (h - b2 + c - 1) / c * c;
        }
        (y, h)
    };
    // the next term depends only on the last two, so the pairs of
    // neighbouring terms run into a cycle; Brent's method finds it in O(1)
    // memory: the length first, then where it starts
    let (mut power, mut length) = (1u64, 1u64);
    let (mut slow, mut fast) = (first, step(first));
    while slow != fast {
        if power == length {
            slow = fast;
            power *= 2;
            length = 0;
        }
        fast = step(fast);
        length += 1;
    }
    slow = first;
    fast = first;
    for _ in 0..length {
        fast = step(fast);
    }
    let mut start = 1;
    while slow != fast {
        slow = step(slow);
        fast = step(fast);
        start += 1;
    }
    println!("{} {}", start, length);
}
