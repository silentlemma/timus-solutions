use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<i32>().unwrap());
    let k = it.next().unwrap() as usize;
    let mut sleepers: Vec<(i32, i32)> = (0..k)
        .map(|_| (it.next().unwrap(), it.next().unwrap()))
        .collect();
    sleepers.sort();
    // two sleepers cross when their ends come in opposite orders, so the
    // kept ones form an increasing run of right ends
    let mut longest = vec![1usize; k];
    for i in 0..k {
        for j in 0..i {
            if sleepers[j].1 < sleepers[i].1 {
                longest[i] = longest[i].max(longest[j] + 1);
            }
        }
    }
    println!("{}", k - longest.iter().copied().max().unwrap_or(0));
}
