use std::io::{self, Read};

const HOSTS: u32 = 2; // Marshall and Lily
const UNLUCKY: u32 = 13;
const PRICE: u32 = 100;
const PLUS: &str = "+one";

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_whitespace();
    let n: usize = words.next().unwrap().parse().unwrap();
    let mut people = HOSTS;
    for name in words.take(n) {
        people += if name.ends_with(PLUS) { 2 } else { 1 };
    }
    if people == UNLUCKY {
        people += 1; // a dummy takes the extra seat
    }
    println!("{}", people * PRICE);
}
