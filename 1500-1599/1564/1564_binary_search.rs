use std::io::{self, Read};

const BASE: i64 = 10;
const TOP: i64 = 1_000_000_000_000_000_000; // more than 10^18 ones are counted below this floor

/// The number of digits 1 in the numbers from 1 to x: at each place p, every
/// full block of 10 p numbers holds p ones there, and the last part adds p,
/// the rest past the 1, or nothing, as its digit is above, at or below 1.
fn ones(x: i64) -> i64 {
    let mut total = 0;
    let mut p = 1;
    // x is at least 1; p stops before p * 10 could pass 10^19
    loop {
        let (high, digit, low) = (x / p / BASE, x / p % BASE, x % p);
        total += high * p
            + match digit {
                0 => 0,
                1 => low + 1,
                _ => p,
            };
        if p > x / BASE {
            return total;
        }
        p *= BASE;
    }
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let k: i64 = text.trim().parse().unwrap();
    // the floor where the k-th one was counted is the first x with ones(x) >= k
    let (mut lo, mut hi) = (1, TOP);
    while lo < hi {
        let mid = lo + (hi - lo) / 2;
        if ones(mid) >= k {
            hi = mid;
        } else {
            lo = mid + 1;
        }
    }
    if ones(lo) == k {
        println!("{}", lo);
    } else {
        println!("Petr lies");
    }
}
