use std::io::{self, Read};

const ALICE: i64 = 1;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace().map(|t| t.parse::<i64>().unwrap());
    let mut next = || it.next().unwrap();
    // tuple fields are read from left to right
    let (length, total, va, vb, n) = (next(), next(), next(), next(), next());
    // riding in opposite directions, they meet whenever the distance ridden by
    // both together reaches a new multiple of the length; the intervals of one
    // kid do not overlap, so their durations add up
    let mut resting = [0i64; 2];
    for _ in 0..n {
        let (kid, _start, duration) = (next(), next(), next());
        resting[if kid == ALICE { 0 } else { 1 }] += duration;
    }
    let ridden = va * (total - resting[0]) + vb * (total - resting[1]);
    println!("{}", ridden / length);
}
