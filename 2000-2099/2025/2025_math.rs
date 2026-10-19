use std::io::{self, Read};

fn solve(count: u64, groups: u64) -> u64 {
    let small = count / groups;
    let larger = count % groups;
    let squares = (groups - larger) * small * small + larger * (small + 1) * (small + 1);
    (count * count - squares) / 2
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let tests: usize = tokens.next().unwrap().parse().unwrap();
    for _ in 0..tests {
        let count = tokens.next().unwrap().parse().unwrap();
        let groups = tokens.next().unwrap().parse().unwrap();
        println!("{}", solve(count, groups));
    }
}
