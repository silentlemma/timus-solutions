use std::io::{self, Read};

fn solve(values: &[u64], first: usize, second: usize) -> (u64, u64) {
    let total: u64 = values.iter().sum();
    let score = if first == second {
        let left: u64 = values[..first].iter().sum();
        let right = total - left - values[first];
        values[first] + left.max(right)
    } else if first < second {
        values[..=(first + second) / 2].iter().sum()
    } else {
        values[(first + second + 1) / 2..].iter().sum()
    };
    (score, total - score)
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let n: usize = tokens.next().unwrap().parse().unwrap();
    let values: Vec<u64> = (0..n)
        .map(|_| tokens.next().unwrap().parse().unwrap())
        .collect();
    let first = tokens.next().unwrap().parse::<usize>().unwrap() - 1;
    let second = tokens.next().unwrap().parse::<usize>().unwrap() - 1;
    let (a, b) = solve(&values, first, second);
    println!("{} {}", a, b);
}
