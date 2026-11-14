use std::io::{self, BufRead};

fn number(input: &mut impl BufRead) -> usize {
    let mut value = 0;
    let mut started = false;
    loop {
        let bytes = input.fill_buf().unwrap();
        if bytes.is_empty() {
            return value;
        }
        let mut consumed = 0;
        for &byte in bytes {
            consumed += 1;
            if byte.is_ascii_digit() {
                started = true;
                value = value * 10 + usize::from(byte - b'0');
            } else if started {
                input.consume(consumed);
                return value;
            }
        }
        input.consume(consumed);
    }
}

fn main() {
    let mut input = io::stdin().lock();
    let (floors, elevators) = (number(&mut input), number(&mut input));
    if floors == 1 {
        println!("-1");
        return;
    }
    let mut difference = vec![0i32; floors];
    for _ in 0..elevators {
        let (left, right) = (number(&mut input), number(&mut input));
        difference[left - 1] += 1;
        difference[right - 1] -= 1;
    }
    // The final difference is beyond the last gap.
    let (mut load, mut best) = (0, elevators as i32);
    for delta in &difference[..floors - 1] {
        load += delta;
        best = best.min(load);
    }
    println!("{best}");
}
