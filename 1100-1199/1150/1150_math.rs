use std::io::{self, Read};

const DIGITS: i64 = 10;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let n: i64 = input.trim().parse().unwrap();
    let mut count = [0i64; DIGITS as usize];
    let mut p = 1;
    while p <= n {
        // at this position the numbers up to n split into the part above, the
        // digit itself and the part below; every smaller upper part repeats
        // each digit p times here
        let (high, cur, low) = (n / (p * DIGITS), n / p % DIGITS, n % p);
        for d in 1..DIGITS {
            count[d as usize] += high * p
                + if d < cur {
                    p
                } else if d == cur {
                    low + 1
                } else {
                    0
                };
        }
        // a zero needs a nonzero digit above it, so the upper part 0 is skipped
        if high > 0 {
            count[0] += (high - 1) * p + if cur > 0 { p } else { low + 1 };
        }
        p *= DIGITS;
    }
    for c in count {
        println!("{}", c);
    }
}
