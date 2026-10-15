use std::io::{self, Read};

const DAY: i64 = 1440;
const HOUR: i64 = 60;

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut words = text.split_ascii_whitespace();
    let n: usize = words.next().unwrap().parse().unwrap();
    let mut now: i64 = 0;
    for _ in 1..n {
        let mut num = || words.next().unwrap().parse::<i64>().unwrap();
        let (q, delay, flight) = (num(), num(), num());
        let mut best = i64::MAX;
        for _ in 0..q {
            let (hours, minutes) = words.next().unwrap().split_once(':').unwrap();
            let mut leave =
                hours.parse::<i64>().unwrap() * HOUR + minutes.parse::<i64>().unwrap() + delay;
            if leave < now {
                // the same flight on a later day
                leave += (now - leave + DAY - 1) / DAY * DAY;
            }
            best = best.min(leave);
        }
        now = best + flight;
    }
    println!("{}", now);
}
