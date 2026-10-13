use std::io::{self, Read};

const HALF: i32 = 1000;
const TICKETS: i32 = 1_000_000;
const BASE: i32 = 10;

fn digit_sum(mut n: i32) -> i32 {
    let mut s = 0;
    while n > 0 {
        s += n % BASE;
        n /= BASE;
    }
    s
}

fn lucky(n: i32) -> bool {
    digit_sum(n / HALF) == digit_sum(n % HALF)
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let number: i32 = input.trim().parse().unwrap();
    // the sums differ by one, so the ticket is neither 000000 nor 999999
    // and both neighbours are six-digit tickets
    let yes = [number - 1, number + 1]
        .iter()
        .any(|&n| (0..TICKETS).contains(&n) && lucky(n));
    println!("{}", if yes { "Yes" } else { "No" });
}
