use std::collections::HashSet;
use std::io::{self, Read};

const SIZE: usize = 3;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let k: usize = it.next().unwrap().parse().unwrap();
    let teams: Vec<HashSet<&str>> = (0..k)
        .map(|_| (0..SIZE).map(|_| it.next().unwrap()).collect())
        .collect();
    // clash[i]: the teams sharing a member with team i, i itself included
    let clash: Vec<usize> = (0..k)
        .map(|i| {
            (0..k)
                .filter(|&j| !teams[i].is_disjoint(&teams[j]))
                .fold(0, |m, j| m | 1 << j)
        })
        .collect();
    // the lowest team of a set is either skipped or taken with its clashes
    // out; both smaller sets come earlier in this order
    let mut best = vec![0u8; 1 << k];
    for mask in 1..1usize << k {
        let i = mask.trailing_zeros() as usize;
        best[mask] = best[mask & (mask - 1)].max(1 + best[mask & !clash[i]]);
    }
    println!("{}", best[(1 << k) - 1]);
}
