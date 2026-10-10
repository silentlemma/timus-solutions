use std::io::{self, Read};

const WHOLE: i64 = 10000;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let n: usize = it.next().unwrap().parse().unwrap();
    let given: Vec<Option<i64>> = (0..n)
        .map(|_| {
            it.next();
            if it.next().unwrap() == "1" {
                Some(it.next().unwrap().parse().unwrap())
            } else {
                None
            }
        })
        .collect();
    // shares never grow down the list, so an unknown share is at least the
    // next given one (or 1) and at most the last given one before it (or
    // 100%); every total between the two extremes can be reached
    let (mut low, mut floor) = (0, 1);
    for g in given.iter().rev() {
        floor = g.unwrap_or(floor);
        low += floor;
    }
    let (mut high, mut ceiling) = (0, WHOLE);
    for g in &given {
        ceiling = g.unwrap_or(ceiling);
        high += ceiling;
    }
    println!(
        "{}",
        if low <= WHOLE && WHOLE <= high {
            "YES"
        } else {
            "NO"
        }
    );
}
