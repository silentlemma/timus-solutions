use std::io::{self, BufRead};

const HOURS: usize = 12;
const MINUTE: usize = 60;
const HOUR: usize = MINUTE * MINUTE;
const DIAL: usize = HOURS * HOUR;

fn number(input: &mut impl BufRead) -> usize {
    let mut value = 0;
    let mut found = false;
    loop {
        let buffer = input.fill_buf().unwrap();
        if buffer.is_empty() {
            return value;
        }
        let mut consumed = 0;
        for &c in buffer {
            consumed += 1;
            if c.is_ascii_digit() {
                value = value * 10 + usize::from(c - b'0');
                found = true;
            } else if found {
                input.consume(consumed);
                return value;
            }
        }
        input.consume(consumed);
    }
}

fn main() {
    let stdin = io::stdin();
    let mut input = stdin.lock();
    let count = number(&mut input);
    let mut frequency = [0u16; DIAL];
    for _ in 0..count {
        let h = number(&mut input);
        let m = number(&mut input);
        let s = number(&mut input);
        frequency[h % HOURS * HOUR + m * MINUTE + s] += 1;
    }

    let mut later = count;
    let (mut best_time, mut best_cost) = (0, count as u64 * DIAL as u64);
    for (target, &clocks) in frequency.iter().enumerate() {
        if clocks == 0 {
            continue;
        }
        later -= usize::from(clocks);
        let cost = count as u64 * target as u64 + DIAL as u64 * later as u64;
        if cost < best_cost {
            best_time = target;
            best_cost = cost;
        }
    }
    let h = best_time / HOUR;
    let rest = best_time % HOUR;
    println!(
        "{}:{:02}:{:02}",
        if h == 0 { HOURS } else { h },
        rest / MINUTE,
        rest % MINUTE
    );
}
