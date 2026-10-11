use std::io::{self, Read};

const SIGNAL_DIGITS: usize = 6; // signal values are read in millionths
const FACTOR_DIGITS: usize = 3; // A has at most three decimals
const SIGNAL: i64 = 1_000_000;
const FACTOR: i64 = 1_000;
const WALL: i64 = 95;
const LOW: i64 = 35;
const CHANNELS: usize = 2;

// a non-negative decimal as an exact multiple of 1 / 10^digits
fn scaled(token: &str, digits: usize) -> i64 {
    let (whole, frac) = token.split_once('.').unwrap_or((token, ""));
    let frac: String = frac
        .chars()
        .chain(std::iter::repeat('0'))
        .take(digits)
        .collect();
    let whole: i64 = if whole.is_empty() {
        0
    } else {
        whole.parse().unwrap()
    };
    whole * 10i64.pow(digits as u32) + frac.parse::<i64>().unwrap()
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_ascii_whitespace();
    let mut int = || words.next().unwrap().parse::<usize>().unwrap();
    let (n, d) = (int(), int());
    let zones: Vec<(usize, usize, i64)> = (0..CHANNELS)
        .map(|_| (int(), int(), int() as i64))
        .collect();
    drop(int);
    let a = scaled(words.next().unwrap(), FACTOR_DIGITS);
    let raw: Vec<i64> = words.take(n).map(|w| scaled(w, SIGNAL_DIGITS)).collect();
    let unit = SIGNAL * FACTOR;
    // the front wall: the first value of 95 or more after a value of 35 or less
    let mut surface = None;
    let mut low = false;
    for (i, &x) in raw.iter().enumerate() {
        if low && x >= WALL * SIGNAL {
            surface = Some(i);
            break;
        }
        low = low || x <= LOW * SIGNAL;
    }
    let surface = match surface {
        Some(s) => s,
        None => {
            println!("No surface.");
            return;
        }
    };
    let mut out = format!("Surface found at {}.\n", surface + 1);
    // after the wall every value is multiplied by 1 + (m - f) A, here in
    // units of 1 / (SIGNAL * FACTOR)
    let value: Vec<i64> = raw
        .iter()
        .enumerate()
        .map(|(i, &x)| {
            if i <= surface {
                x * FACTOR
            } else {
                x * (FACTOR + (i - surface) as i64 * a)
            }
        })
        .collect();
    let mut bottom = None;
    low = false;
    for i in surface + 1..n {
        if low && i - surface >= d && value[i] >= WALL * unit {
            bottom = Some(i);
            break;
        }
        low = low || value[i] <= LOW * unit;
    }
    out += &match bottom {
        Some(b) => format!("Bottom found at {}.\n", b - surface),
        None => "No bottom.\n".to_string(),
    };
    let end = bottom.unwrap_or(n); // one past the last number searched
    for (c, &(start, stop, level)) in zones.iter().enumerate() {
        let (lo, hi) = (surface + start, (surface + stop + 1).min(end));
        if lo >= hi {
            out += &format!("Channel {}: No search.\n", c + 1);
            continue;
        }
        let mut best = lo;
        for i in lo + 1..hi {
            if value[i] > value[best] {
                best = i;
            }
        }
        if value[best] >= level * unit {
            out += &format!("Channel {}: Object at {}.\n", c + 1, best - surface);
        } else {
            out += &format!("Channel {}: No object.\n", c + 1);
        }
    }
    print!("{}", out);
}
