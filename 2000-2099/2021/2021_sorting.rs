use std::io::{self, Read};
use std::str::SplitWhitespace;

fn solve(first: &[i32], second: &[i32]) -> Vec<(usize, usize)> {
    let mut a: Vec<usize> = (0..first.len()).collect();
    let mut b: Vec<usize> = (0..second.len()).collect();
    a.sort_unstable_by_key(|&i| (first[i], i));
    b.sort_unstable_by_key(|&i| (second[i], i));
    let total_a: i32 = first.iter().sum();
    let total_b: i32 = second.iter().sum();
    if total_a > total_b {
        b.reverse();
    } else if total_a < total_b {
        a.reverse();
    }
    a.into_iter().zip(b).collect()
}

fn run(tokens: &mut SplitWhitespace<'_>) -> String {
    let n: usize = tokens.next().unwrap().parse().unwrap();
    let first: Vec<i32> = (0..n)
        .map(|_| tokens.next().unwrap().parse().unwrap())
        .collect();
    let second: Vec<i32> = (0..n)
        .map(|_| tokens.next().unwrap().parse().unwrap())
        .collect();
    let lines: Vec<String> = solve(&first, &second)
        .into_iter()
        .map(|(a, b)| format!("{} {}", a + 1, b + 1))
        .collect();
    lines.join("\n") + "\n"
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    print!("{}", run(&mut input.split_whitespace()));
}
