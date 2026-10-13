use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<usize> = input
        .split_ascii_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();
    let n = v[0];
    let taken = &v[1..=n];
    // the pocket is a stack: roll the balls in order, and whenever the top
    // one is the next ball the inspector took out, take it out
    let mut pocket: Vec<usize> = Vec::with_capacity(n);
    let mut next = 0;
    for ball in 1..=n {
        pocket.push(ball);
        while next < n && pocket.last() == Some(&taken[next]) {
            pocket.pop();
            next += 1;
        }
    }
    println!("{}", if next == n { "Not a proof" } else { "Cheater" });
}
