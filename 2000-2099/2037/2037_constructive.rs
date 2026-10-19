use std::io::{self, Read, Write};

const SMALL_LIMIT: usize = 7;
const STABLE_MIN: usize = 8;
const EXTRA_COUNT: usize = 6;
const PERIOD: &str = "babbaa";
fn construct(n: usize, count: usize) -> String {
    let minimum = if n <= SMALL_LIMIT {
        n
    } else if n == STABLE_MIN {
        SMALL_LIMIT
    } else {
        STABLE_MIN
    };
    if count < minimum {
        return "NO".to_string();
    }
    if count == n {
        return "a".repeat(n);
    }
    if n == STABLE_MIN {
        return "aababbaa".to_string();
    }
    let run = count - EXTRA_COUNT;
    let tail = n - run;
    let mut word = "a".repeat(run);
    let periodic = PERIOD.repeat((tail + PERIOD.len() - 1) / PERIOD.len());
    word.push_str(&periodic[..tail]);
    word
}
fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let n: usize = input.trim().parse().unwrap();
    let stdout = io::stdout();
    let mut out = io::BufWriter::new(stdout.lock());
    for count in 1..=n {
        writeln!(out, "{} : {}", count, construct(n, count)).unwrap();
    }
}
