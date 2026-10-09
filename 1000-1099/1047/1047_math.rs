use std::io::{self, Read};

const CENTS: i64 = 100;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let n: i64 = it.next().unwrap().parse().unwrap();
    // the input numbers in hundredths
    let mut read_cents =
        || (it.next().unwrap().parse::<f64>().unwrap() * CENTS as f64).round() as i64;
    let (first, last) = (read_cents(), read_cents());
    // with d[i] = a[i] - a[i-1] the relation reads d[i+1] = d[i] + 2 c[i], so
    // a[N+1] - a[0] = (N + 1) d[1] + 2 sum (N + 1 - i) c[i]
    let weighted: i64 = (1..=n).map(|i| (n + 1 - i) * read_cents()).sum();
    let (num, den) = (n * first + last - 2 * weighted, n + 1);
    // the answer has two decimals; rounding only guards against bad input
    let q = (2 * num.abs() + den) / (2 * den);
    let sign = if num < 0 && q > 0 { "-" } else { "" };
    println!("{}{}.{:02}", sign, q / CENTS, q % CENTS);
}
