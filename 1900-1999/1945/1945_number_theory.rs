use std::io::{self, Read};

const PRIME_THREE: i32 = 3;
const PRIME_FIVE: i32 = 5;
const MAX_THREE_WEIGHT: i32 = 3;
const FIVE_WEIGHT: i32 = 4;

fn hall(mut value: i32, groups: i32) -> i32 {
    let primes = [2, PRIME_THREE, PRIME_FIVE];
    let weights = [1, (groups - 1).min(MAX_THREE_WEIGHT), FIVE_WEIGHT];
    let mut color = 0;
    for (prime, weight) in primes.into_iter().zip(weights) {
        while value % prime == 0 {
            value /= prime;
            color += weight;
        }
    }
    color % groups + 1
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_whitespace();
    let size = words.next().unwrap().parse::<usize>().unwrap();
    let groups = words.next().unwrap().parse().unwrap();
    let mut output = String::from("Yes\n");
    for _ in 0..size {
        let value = words.next().unwrap().parse().unwrap();
        output.push_str(&format!("{}\n", hall(value, groups)));
    }
    print!("{}", output);
}
