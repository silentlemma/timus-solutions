use std::io::{self, Read};

const HOUR: i32 = 60;
const DAY: i32 = 24 * HOUR;
const LONGEST: i32 = 6 * HOUR;
const SPREAD: i32 = 10;
const MAX_SHIFT: i32 = 5;

fn minutes(s: &str) -> i32 {
    let (h, m) = s.split_once('.').unwrap();
    h.parse::<i32>().unwrap() * HOUR + m.parse::<i32>().unwrap()
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let t: Vec<i32> = input.split_ascii_whitespace().map(minutes).collect();
    let [out1, in1, out2, in2] = t[..] else {
        return;
    };
    // when the second airport is k hours ahead, the real durations are the clock
    // differences minus and plus k hours, taken around the day
    for k in -MAX_SHIFT..=MAX_SHIFT {
        let t1 = (in1 - out1 - k * HOUR).rem_euclid(DAY);
        let t2 = (in2 - out2 + k * HOUR).rem_euclid(DAY);
        if t1 <= LONGEST && t2 <= LONGEST && (t1 - t2).abs() <= SPREAD {
            println!("{}", k.abs());
            return;
        }
    }
}
