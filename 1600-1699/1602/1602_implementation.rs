use std::io::{self, Read};

const HUNDRED: i64 = 100; // times are kept in hundredths of a second, exactly
const STAND: i64 = 15 * HUNDRED; // the lift stands this long on the first floor
const BOARD: i64 = 5 * HUNDRED; // getting into the lift
const DIGITS: usize = 2;

/// A number with at most two decimals, as an exact integer of hundredths.
fn hundredths(word: &str) -> i64 {
    let mut parts = word.splitn(2, '.');
    let whole: i64 = parts.next().unwrap().parse().unwrap();
    let frac = format!("{}00", parts.next().unwrap_or(""));
    whole * HUNDRED + frac[..DIGITS].parse::<i64>().unwrap()
}

fn main() {
    let mut s = String::new();
    io::stdin().read_to_string(&mut s).unwrap();
    let w: Vec<&str> = s.split_ascii_whitespace().collect();
    let (n, k, u, v) = match w[..] {
        [n, k, u, v] => (
            n.parse::<i64>().unwrap(),
            k.parse::<i64>().unwrap(),
            hundredths(u),
            hundredths(v),
        ),
        _ => return,
    };
    // walking all the way down needs no lift
    let (mut best_floor, mut best_time) = (1, (n - 1) * u);
    let ready = (k - 1) * v + STAND; // the lift may leave the first floor from then on
    for f in 2..=n {
        // Petya calls the lift on reaching floor f; it comes up, waits for
        // the boarding and goes down again
        let start = ready.max((n - f) * u);
        let total = start + (f - 1) * v + BOARD + (f - 1) * v;
        // a later floor means less walking, so ties go to it
        if total <= best_time {
            best_floor = f;
            best_time = total;
        }
    }
    println!("{}", best_floor);
}
