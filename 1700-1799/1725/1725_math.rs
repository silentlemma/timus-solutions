use std::io::{self, Read};

// everyone on the far side of Vasya can be made to trip except the two
// seats at the far end, who always come in from their own end
const SAFE: i32 = 2;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace().map(|w| w.parse::<i32>().unwrap());
    let (n, k) = (it.next().unwrap(), it.next().unwrap());
    let far = (k - 1).max(n - k);
    println!("{}", (far - SAFE).max(0));
}
