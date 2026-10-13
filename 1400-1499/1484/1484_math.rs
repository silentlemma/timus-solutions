use std::io::{self, Read};

const TOP: i64 = 10; // the highest vote
const HALVES: i64 = 20; // a rating counts in half tenths

fn tenths(s: &str) -> i64 {
    let (whole, part) = match s.find('.') {
        Some(i) => (&s[..i], format!("{}0", &s[i + 1..])),
        None => (s, String::from("0")),
    };
    whole.parse::<i64>().unwrap() * 10 + (part.as_bytes()[0] - b'0') as i64
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let (x, y) = (tenths(it.next().unwrap()), tenths(it.next().unwrap()));
    let n: i64 = it.next().unwrap().parse().unwrap();
    // n votes from 1 to 10 show x when (2x - 1) n <= 20 sum < (2x + 1) n,
    // and the worst case is the largest such sum, and there may be none at all
    let total = (TOP * n).min(((2 * x + 1) * n - 1) / HALVES);
    let least = n.max(((2 * x - 1) * n + HALVES - 1) / HALVES);
    // k votes of 1 show at most y when 20 (total + k) < (2y + 1)(n + k)
    let excess = HALVES * total - (2 * y + 1) * n;
    let step = 2 * y + 1 - HALVES;
    if least > total || (excess >= 0 && step <= 0) {
        println!("Impossible");
    } else if excess < 0 {
        println!("0");
    } else {
        println!("{}", excess / step + 1);
    }
}
