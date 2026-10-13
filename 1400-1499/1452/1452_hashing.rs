use std::collections::HashMap;
use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|x| x.parse::<i64>().unwrap());
    let n = it.next().unwrap() as usize;
    // a value and the number of one element holding it
    let mut place: HashMap<i64, usize> = HashMap::with_capacity(2 * n);
    let mut a: Vec<i64> = Vec::with_capacity(n);
    for i in 1..=n {
        let s = it.next().unwrap();
        if let std::collections::hash_map::Entry::Vacant(e) = place.entry(s) {
            e.insert(i);
            a.push(s);
        }
    }
    a.sort_unstable();
    let (mut best_length, mut best_first, mut best_step) = (1i64, a[0], 1i64);
    for i in 0..a.len() {
        for j in i + 1..a.len() {
            let d = a[j] - a[i];
            // walk each progression only from its first member, so every
            // pair of neighbours in it is visited once
            if place.contains_key(&(a[i] - d)) {
                continue;
            }
            let (mut length, mut last) = (2i64, a[j]);
            while place.contains_key(&(last + d)) {
                last += d;
                length += 1;
            }
            if length > best_length {
                best_length = length;
                best_first = a[i];
                best_step = d;
            }
        }
    }
    let parts: Vec<String> = (0..best_length)
        .map(|k| place[&(best_first + k * best_step)].to_string())
        .collect();
    println!("{}", best_length);
    println!("{}", parts.join(" "));
}
