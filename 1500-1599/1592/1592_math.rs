use std::io::{self, Read};

const MINUTE: i64 = 60;
const HOUR: i64 = 60 * MINUTE;
const CYCLE: i64 = 12 * HOUR; // the dial shows the same after 12 hours
const TWELVE: i64 = 12;

fn main() {
    let mut s = String::new();
    io::stdin().read_to_string(&mut s).unwrap();
    let mut words = s.split_ascii_whitespace();
    let n: usize = match words.next() {
        Some(w) => w.parse().unwrap(),
        None => return,
    };
    let mut times: Vec<i64> = words
        .take(n)
        .map(|w| {
            let p: Vec<i64> = w.split(':').map(|x| x.parse().unwrap()).collect();
            p[0] % TWELVE * HOUR + p[1] * MINUTE + p[2] // 12 o'clock is 0
        })
        .collect();
    times.sort_unstable();
    let total: i64 = times.iter().sum();
    // winding clock i forward to t costs t - time_i, plus a full cycle when
    // the clock shows a later time than t; moving t back to the nearest
    // clock time only helps, so only the clock times are tried
    let (mut best, mut best_cost) = (0, -1);
    let mut j = 0; // clocks showing at most t
    for &t in &times {
        while j < n && times[j] <= t {
            j += 1;
        }
        let cost = n as i64 * t - total + CYCLE * (n - j) as i64;
        if best_cost < 0 || cost < best_cost {
            best = t;
            best_cost = cost;
        }
    }
    let (h, rest) = (best / HOUR, best % HOUR);
    let h = if h == 0 { TWELVE } else { h };
    println!("{}:{:02}:{:02}", h, rest / MINUTE, rest % MINUTE);
}
