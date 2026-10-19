use std::io::{self, Read};

fn best_count(sample: u64, successes: u64, population: u64) -> u64 {
    population.min(successes * (population + 1) / sample)
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_whitespace();
    let sample: u64 = words.next().unwrap().parse().unwrap();
    let successes: u64 = words.next().unwrap().parse().unwrap();
    let population: u64 = words.next().unwrap().parse().unwrap();
    println!("{}", best_count(sample, successes, population));
}
