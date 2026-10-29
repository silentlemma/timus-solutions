use std::io::{self, Read, Write};

const TOTAL_TASKS: i32 = 12;
const FIRST_HOUR_MINUTES: i32 = 60;
const MINUTES_PER_TASK: i32 = 45;
const CONTEST_MINUTES: i32 = 300;

fn solve(first_hour: i32) -> bool {
    FIRST_HOUR_MINUTES + (TOTAL_TASKS - first_hour) * MINUTES_PER_TASK <= CONTEST_MINUTES
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let first_hour: i32 = input.trim().parse().unwrap();
    // the answer is written as bytes in one call instead of println!
    let answer: &[u8] = if solve(first_hour) { b"YES\n" } else { b"NO\n" };
    io::stdout().write_all(answer).unwrap();
}
