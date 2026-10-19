use std::f64::consts::PI;
use std::io::{self, Read};

fn radius(count: u32) -> f64 {
    if count == 1 {
        return 1.0;
    }
    1.0 + 1.0 / (PI / f64::from(count)).sin()
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let count = input.trim().parse().unwrap();
    println!("{:.10}", radius(count));
}
