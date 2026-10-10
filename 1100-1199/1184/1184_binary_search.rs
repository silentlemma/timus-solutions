use std::io::{self, Read};

const CENTS: i64 = 100;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let n: usize = it.next().unwrap().parse().unwrap();
    let k: i64 = it.next().unwrap().parse().unwrap();
    // lengths have exactly two decimals, so in centimetres they are exact
    let cables: Vec<i64> = (0..n)
        .map(|_| it.next().unwrap().replace('.', "").parse().unwrap())
        .collect();
    // more pieces come out of shorter ones, so the longest length that still
    // gives k pieces is found by binary search; 0 means even 1 cm is too long
    let (mut low, mut high) = (0, *cables.iter().max().unwrap());
    while low < high {
        let mid = (low + high + 1) / 2;
        let pieces: i64 = cables.iter().map(|c| c / mid).sum();
        if pieces >= k {
            low = mid;
        } else {
            high = mid - 1;
        }
    }
    println!("{}.{:02}", low / CENTS, low % CENTS);
}
