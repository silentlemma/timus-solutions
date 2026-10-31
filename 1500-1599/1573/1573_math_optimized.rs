use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_whitespace();
    let blue: u64 = words.next().unwrap().parse().unwrap();
    let red: u64 = words.next().unwrap().parse().unwrap();
    let yellow: u64 = words.next().unwrap().parse().unwrap();
    let count: usize = words.next().unwrap().parse().unwrap();
    let mut ways = 1;
    // the three fixed color names can be matched directly, avoiding a hash table.
    for color in words.take(count) {
        ways *= match color {
            "Blue" => blue,
            "Red" => red,
            "Yellow" => yellow,
            _ => unreachable!(),
        };
    }
    println!("{}", ways);
}
