use std::io::{self, Read};

const LIMIT: usize = 100000;
const BASE: usize = 10;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut n: usize = input.trim().parse().unwrap();
    let mut digits = vec![0usize; LIMIT];
    for i in 1..LIMIT {
        digits[i] = digits[i / BASE] + i % BASE;
    }
    // take numbers from the top whenever their digits still fit; the small
    // ones at the end fill any remainder, so the sum always comes out
    let mut chosen = Vec::new();
    for i in (1..LIMIT).rev() {
        if n == 0 {
            break;
        }
        if digits[i] <= n {
            chosen.push(i.to_string());
            n -= digits[i];
        }
    }
    println!("{}", chosen.len());
    println!("{}", chosen.join(" "));
}
