use std::io::{self, Read};

const SWAPPED: usize = 2; // a single swap changes exactly two places

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let a: Vec<u64> = input.split_ascii_whitespace().skip(1).map(|t| t.parse().unwrap()).collect();
    let mut ascending = a.clone();
    ascending.sort_unstable();
    let descending: Vec<u64> = ascending.iter().rev().copied().collect();
    if a == ascending || a == descending {
        println!("Nothing to do here");
        return;
    }
    // one swap can only fix a line that differs from a sorted one in exactly
    // two places, and then the swap of those two places does it
    for t in [&ascending, &descending] {
        let wrong: Vec<usize> = (0..a.len()).filter(|&i| a[i] != t[i]).take(SWAPPED + 1).collect();
        if wrong.len() != SWAPPED {
            continue;
        }
        let (i, j) = (wrong[0], wrong[1]);
        if a[i] == t[j] && a[j] == t[i] {
            println!("Yes\n{} {}", i + 1, j + 1);
            return;
        }
    }
    println!("No hope");
}
