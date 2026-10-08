use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|x| x.parse::<usize>().unwrap());
    let n = it.next().unwrap();
    let w: Vec<usize> = it.take(n).collect();
    let total: usize = w.iter().sum();
    // reach[s]: some stones weigh exactly s; the lighter pile is at most total/2
    let half = total / 2;
    let mut reach = vec![false; half + 1];
    reach[0] = true;
    for &x in &w {
        for s in (x..=half).rev() {
            if reach[s - x] {
                reach[s] = true;
            }
        }
    }
    let lighter = (0..=half).rev().find(|&s| reach[s]).unwrap();
    println!("{}", total - 2 * lighter);
}
