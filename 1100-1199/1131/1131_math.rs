use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<i64> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let (n, k) = (v[0], v[1]);
    // as long as fewer computers than cables have the program, each hour doubles
    // the count; after that k computers get it each hour
    let (mut have, mut hours) = (1i64, 0i64);
    while have < n && have < k {
        have *= 2;
        hours += 1;
    }
    if have < n {
        hours += (n - have + k - 1) / k;
    }
    println!("{}", hours);
}
