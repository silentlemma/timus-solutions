use std::io::{self, Read};

const TIME: usize = 30000;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<usize> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let n = v[0];
    // the latest start among the talks that end at each minute
    let mut latest = vec![0; TIME + 1];
    for talk in v[1..1 + 2 * n].chunks(2) {
        latest[talk[1]] = latest[talk[1]].max(talk[0]);
    }
    // take the talk that ends first among those starting after the last one
    let (mut count, mut last) = (0, 0);
    for (e, &s) in latest.iter().enumerate() {
        if s > last {
            count += 1;
            last = e;
        }
    }
    println!("{}", count);
}
