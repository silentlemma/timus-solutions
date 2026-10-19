use std::io::{self, Read};

fn minimum_common(population: i64, lower_bounds: &[i64]) -> i64 {
    let mut answer = population;
    for &lower in lower_bounds {
        answer -= population - lower;
    }
    answer.max(0)
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_whitespace();
    let population: i64 = words.next().unwrap().parse().unwrap();
    let count: usize = words.next().unwrap().parse().unwrap();
    let lower_bounds: Vec<i64> = words.take(count).map(|w| w.parse().unwrap()).collect();
    println!("{}", minimum_common(population, &lower_bounds));
}
