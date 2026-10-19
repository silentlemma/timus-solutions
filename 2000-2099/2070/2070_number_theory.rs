use std::io::{self, Read};

const LIMIT: usize = 1_000_000; // square root of the largest R

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<i64> = input.split_ascii_whitespace().map(|t| t.parse().unwrap()).collect();
    let (l, r) = (v[0], v[1]);
    let mut composite = vec![false; LIMIT + 1];
    composite[0] = true;
    composite[1] = true;
    let mut i = 2;
    while i * i <= LIMIT {
        if !composite[i] {
            let mut j = i * i;
            while j <= LIMIT {
                composite[j] = true;
                j += i;
            }
        }
        i += 1;
    }
    // the only unsatisfying numbers are p^k, k >= 2, with k + 1 divisors and k + 1 prime
    let mut bad = 0i64;
    let mut p = 2i64;
    while p * p <= r {
        if !composite[p as usize] {
            let mut power = p * p;
            let mut k = 2;
            loop {
                if power >= l && !composite[k + 1] {
                    bad += 1;
                }
                if power > r / p {
                    break;
                }
                power *= p;
                k += 1;
            }
        }
        p += 1;
    }
    println!("{}", r - l + 1 - bad);
}
