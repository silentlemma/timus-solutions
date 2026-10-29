use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let numbers: Vec<i32> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let n = numbers[0] as usize;
    let a = &numbers[1..=n];
    // try every section as the middle of the three
    let (mut best, mut middle) = (0, 0);
    for i in 1..n - 1 {
        let sum = a[i - 1] + a[i] + a[i + 1];
        if sum > best {
            best = sum;
            middle = i;
        }
    }
    println!("{} {}", best, middle + 1);
}
