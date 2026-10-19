use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut values = input.split_ascii_whitespace();
    let count: usize = values.next().unwrap().parse().unwrap();
    let capacity: u64 = values.next().unwrap().parse().unwrap();
    let mut unused = 0_u64;
    let mut survivors = 0_u64;
    for _ in 0..count {
        let amount: u64 = values.next().unwrap().parse().unwrap();
        if amount > capacity {
            unused += amount - capacity;
        } else {
            survivors += capacity - amount;
        }
    }
    println!("{} {}", unused, survivors);
}
