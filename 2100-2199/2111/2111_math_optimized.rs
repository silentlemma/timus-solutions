use std::io::{self, BufRead};

// the numbers are parsed by hand from the locked standard input instead of
// reading the whole input into a string
fn next_int(input: &mut impl BufRead) -> i64 {
    let mut value = 0;
    let mut sign = 1;
    let mut started = false;
    loop {
        let buffer = input.fill_buf().unwrap();
        if buffer.is_empty() {
            return value * sign;
        }
        let mut consumed = 0;
        let mut finished = false;
        for &c in buffer {
            consumed += 1;
            if c == b'-' {
                sign = -1;
                started = true;
            } else if c.is_ascii_digit() {
                value = value * 10 + i64::from(c - b'0');
                started = true;
            } else if started {
                finished = true;
                break;
            }
        }
        input.consume(consumed);
        if finished {
            return value * sign;
        }
    }
}

fn main() {
    let stdin = io::stdin();
    let mut input = stdin.lock();
    let n = next_int(&mut input);
    let mut total = 0i64;
    for _ in 0..n {
        total += next_int(&mut input);
    }
    // a trip to a city with load L costs L d there and (L - d) d back; summed over
    // any order this is (sum of d)^2, so the order does not matter
    println!("{}", total * total);
}
