use std::io::{self, Read};

const FIRST: i64 = 2; // the first step removes every second day

// among the first n days, step k removes every k-th of those still left,
// which is n / k of a prefix of length n; it stops mattering once n < k
fn quiet(mut n: i64) -> i64 {
    let mut k = FIRST;
    while n >= k {
        n -= n / k;
        k += 1;
    }
    n
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<i64> = input.split_whitespace().map(|t| t.parse().unwrap()).collect();
    println!("{}", quiet(v[1]) - quiet(v[0] - 1));
}
