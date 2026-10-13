use std::io::{self, Read};

const WINDOW: usize = 10; // digits seen in the window

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let n: usize = it.next().unwrap().parse().unwrap();
    let m: usize = it.next().unwrap().parse().unwrap();
    let digits: Vec<&str> = it.take(n).collect();
    // each click moves the window one digit on, around the wheel
    let out: String = (0..WINDOW).map(|i| digits[(m + i) % n]).collect();
    println!("{}", out);
}
