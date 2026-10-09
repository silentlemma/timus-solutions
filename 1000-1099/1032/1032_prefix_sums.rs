use std::fmt::Write as _;
use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<usize> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let (n, a) = (v[0], &v[1..=v[0]]);
    // n + 1 prefix sums modulo n take at most n values: two of them are
    // equal, and the numbers between them sum to a multiple of n
    let mut first = vec![usize::MAX; n];
    first[0] = 0;
    let mut sum = 0;
    for i in 1..=n {
        sum = (sum + a[i - 1]) % n;
        if first[sum] != usize::MAX {
            let part = &a[first[sum]..i];
            let mut out = String::new();
            writeln!(out, "{}", part.len()).unwrap();
            for x in part {
                writeln!(out, "{}", x).unwrap();
            }
            print!("{}", out);
            return;
        }
        first[sum] = i;
    }
}
