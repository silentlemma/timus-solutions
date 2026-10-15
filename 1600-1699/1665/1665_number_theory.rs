use std::io::{self, Read};

const FIRST_ODD: u64 = 3; // the smallest divisor worth trying

/// Whether n is a product of an odd number of factors, each 2 or an odd
/// number above 1: n = 2^twos * rest with rest odd.
fn paid(mut n: u64) -> bool {
    let mut twos = 0;
    while n % 2 == 0 {
        n /= 2;
        twos += 1;
    }
    if n == 1 {
        return twos % 2 == 1;
    }
    if twos % 2 == 0 {
        return true; // rest as a single factor
    }
    // an odd count needs rest split into two factors, so not a prime
    let mut d = FIRST_ODD;
    while d * d <= n {
        if n % d == 0 {
            return true;
        }
        d += 2;
    }
    false
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let nums: Vec<u64> = text.split_ascii_whitespace().map(|w| w.parse().unwrap()).collect();
    let mut out = String::new();
    for &n in nums[1..].iter().take(nums[0] as usize) {
        out.push_str(if paid(n) { "YES\n" } else { "NO\n" });
    }
    print!("{}", out);
}
