use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let n: usize = input.trim().parse().unwrap();
    // ways[s]: sets of distinct step sizes, each used at most once, summing
    // to s; sizes are added one by one, going over s downwards
    let mut ways = vec![0u64; n + 1];
    ways[0] = 1;
    for size in 1..=n {
        for s in (size..=n).rev() {
            ways[s] += ways[s - size];
        }
    }
    // a staircase needs at least two steps: drop the single step of n cubes
    println!("{}", ways[n] - 1);
}
