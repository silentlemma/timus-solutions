use std::io::{self, Read};

fn pairs(k: i64) -> i64 {
    k * (k - 1) / 2
}

fn gcd(x: i64, y: i64) -> i64 {
    if y == 0 {
        x
    } else {
        gcd(y, x % y)
    }
}

// pairs among the first m sleepers on one page of both notebooks: walk the
// pages of the larger size, each cut by the smaller pages into a head,
// whole pages and a tail
fn shared(m: i64, big: i64, small: i64) -> i64 {
    let mut total = 0;
    let mut start = 0;
    while start < m {
        let end = (start + big).min(m);
        let cut = (start / small + 1) * small;
        if cut >= end {
            total += pairs(end - start);
        } else {
            let (whole, tail) = ((end - cut) / small, (end - cut) % small);
            total += pairs(cut - start) + whole * pairs(small) + pairs(tail);
        }
        start += big;
    }
    total
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_ascii_whitespace().map(|w| w.parse::<i64>().unwrap());
    let mut next = || words.next().unwrap();
    let (a, b, n) = (next(), next(), next());
    let (big, small) = (a.max(b), a.min(b));
    // both page breaks repeat every lcm(a, b) sleepers, and so do the pairs
    let period = a / gcd(a, b) * b;
    let both = if period <= n {
        n / period * shared(period, big, small) + shared(n % period, big, small)
    } else {
        shared(n, big, small)
    };
    let vasily = n / a * pairs(a) + pairs(n % a);
    println!("{}", vasily - both);
}
