use std::io::{self, Read};

fn solve(text: &str, limit: usize) -> (usize, u64) {
    const ALPHABET: usize = 26;
    let mut counts = [0_usize; ALPHABET];
    for letter in text.bytes() {
        counts[(letter - b'a') as usize] += 1;
    }
    counts.sort_unstable_by(|a, b| b.cmp(a));
    let size = counts[..limit].iter().sum();
    let boundary = counts[limit - 1];
    if boundary == 0 {
        return (size, 1);
    }
    let greater = counts.iter().filter(|&&count| count > boundary).count();
    let tied = counts.iter().filter(|&&count| count == boundary).count();
    let chosen = (limit - greater).min(tied - (limit - greater));
    let mut ways = 1_u64;
    for index in 1..=chosen {
        ways = ways * (tied - index + 1) as u64 / index as u64;
    }
    (size, ways)
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let text = tokens.next().unwrap();
    let limit = tokens.next().unwrap().parse().unwrap();
    let (size, ways) = solve(text, limit);
    println!("{} {}", size, ways);
}
