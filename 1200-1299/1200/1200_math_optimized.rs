use std::io::{self, Read};

const CENTS: i64 = 100;
const PEAK: i64 = 2 * CENTS;

fn cents(token: &str) -> i64 {
    let negative = token.starts_with('-');
    let digits = token.trim_start_matches(['+', '-']);
    let (whole, fraction) = digits.split_once('.').unwrap_or((digits, ""));
    let mut value: i64 = whole.parse::<i64>().unwrap() * CENTS;
    let mut weight = 10;
    for digit in fraction.bytes().take(2) {
        value += i64::from(digit - b'0') * weight;
        weight /= 10;
    }
    if negative {
        -value
    } else {
        value
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let t: Vec<&str> = input.split_ascii_whitespace().collect();
    let a = cents(t[0]);
    let b = cents(t[1]);
    let k: i64 = t[2].parse().unwrap();
    // everything is in kopecks: x horns earn a * x - 100 * x^2
    let (mut best, mut best_x, mut best_y) = (-1, 0, 0);
    let y_peak = b.max(0) / PEAK;
    // The reduced concave objective changes slope only at the free horn peak
    // or at the optimum on x + y = k. Check neighboring integers at both.
    let free = a.div_euclid(PEAK);
    let boundary = (a - b + PEAK * k).div_euclid(2 * PEAK);
    let mut candidates = [0, k, free, free + 1, boundary, boundary + 1];
    for x in &mut candidates {
        *x = (*x).clamp(0, k);
    }
    candidates.sort_unstable();
    for x in candidates {
        let (room, gain_x) = (k - x, a * x - CENTS * x * x);
        // the hoof profit is concave in y, so the best y is next to its peak
        for y in [y_peak.min(room), (y_peak + 1).min(room)] {
            let total = gain_x + b * y - CENTS * y * y;
            if total > best {
                best = total;
                best_x = x;
                best_y = y;
            }
        }
    }
    println!(
        "{}.{:02}\n{} {}",
        best / CENTS,
        best % CENTS,
        best_x,
        best_y
    );
}
