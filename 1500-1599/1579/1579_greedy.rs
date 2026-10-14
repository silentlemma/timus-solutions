use std::fmt::Write as _;
use std::io::{self, Read};

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut it = text
        .split_ascii_whitespace()
        .map(|w| w.parse::<i64>().unwrap());
    let (n, r) = (it.next().unwrap() as usize, it.next().unwrap());
    let sizes: Vec<i64> = it.take(n).collect();
    // coats whose sizes lie within r of each other need different trips, so
    // the largest number of sizes in a window [x, x + r] is a lower bound
    let (mut trips, mut lo) = (0, 0);
    for hi in 0..n {
        while sizes[hi] - sizes[lo] > r {
            lo += 1;
        }
        trips = trips.max(hi - lo + 1);
    }
    // and it is enough: dealing the sorted coats round, the coat after coat i
    // in a trip is coat i + trips, which lies beyond that window
    let mut out = String::new();
    writeln!(out, "{}", trips).unwrap();
    for t in 0..trips {
        let coats: Vec<String> = (t + 1..=n).step_by(trips).map(|c| c.to_string()).collect();
        writeln!(out, "{} {}", coats.len(), coats.join(" ")).unwrap();
    }
    print!("{}", out);
}
