use std::io::{self, Read, Write};

const HALF: i32 = 1000;

fn digit_sum(mut number: i32) -> i32 {
    let mut sum = 0;
    while number > 0 {
        sum += number % 10;
        number /= 10;
    }
    sum
}

fn lucky(number: i32) -> bool {
    digit_sum(number / HALF) == digit_sum(number % HALF)
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let number: i32 = input.trim().parse().unwrap();
    // the sums differ by one, so the ticket is neither 000000 nor 999999
    // and both neighbours are six-digit tickets
    let answer: &[u8] = if lucky(number - 1) || lucky(number + 1) {
        b"Yes\n"
    } else {
        b"No\n"
    };
    // the answer goes out as a byte string, without the formatting of println!
    io::stdout().write_all(answer).unwrap();
}
