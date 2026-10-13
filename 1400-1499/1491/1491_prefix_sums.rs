use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|x| x.parse::<usize>().unwrap());
    let n = it.next().unwrap();
    // every gift adds c to the knights a..b: mark it at both ends of the
    // range, then a running sum gives each knight's total
    let mut diff = vec![0i64; n + 2];
    for _ in 0..=n {
        let (a, b, c) = (
            it.next().unwrap(),
            it.next().unwrap(),
            it.next().unwrap() as i64,
        );
        diff[a] += c;
        diff[b + 1] -= c;
    }
    let mut total = 0i64;
    let totals: Vec<String> = (1..=n)
        .map(|i| {
            total += diff[i];
            total.to_string()
        })
        .collect();
    println!("{}", totals.join(" "));
}
