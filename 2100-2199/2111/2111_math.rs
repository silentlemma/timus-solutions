use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let roads = input.split_ascii_whitespace().skip(1);
    let total: i64 = roads.map(|t| t.parse::<i64>().unwrap()).sum();
    // a trip to a city with load L costs L d there and (L - d) d back; summed over
    // any order this is (sum of d)^2, so the order does not matter
    println!("{}", total * total);
}
