use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace().map(|v| v.parse::<i64>().unwrap());
    let (n, k) = (it.next().unwrap(), it.next().unwrap());
    // n - k + 1 zeros, then 1, -1, 2, -2, ...: k distinct values and only k
    // distinct segment sums, the least possible
    let mut values = vec![0i64; (n - k + 1) as usize];
    for i in 1..k {
        values.push(if i % 2 == 1 { (i + 1) / 2 } else { -(i / 2) });
    }
    let line: Vec<String> = values.iter().map(|v| v.to_string()).collect();
    println!("{}", line.join(" "));
}
