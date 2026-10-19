use std::io::{self, Read};

// times in units of 1/50 s: a car (20 km/h) covers a metre in 9 units and
// Egor (5 km/h) crosses a 2 m lane in 72
const METRE: i64 = 9;
const LANE: i64 = 72;
const CAR: i64 = 5;
const UNITS: f64 = 50.0;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace().map(|t| t.parse::<i64>().unwrap());
    let mut blocked: Vec<(i64, i64)> = Vec::new();
    // a car is on the crossing from METRE d to METRE (d + CAR); a start time
    // s is bad when Egor's time in the car's lane overlaps that
    for lane in 0..2 {
        let count = it.next().unwrap();
        for _ in 0..count {
            let d = it.next().unwrap();
            let enter = lane * LANE;
            blocked.push((METRE * d - enter - LANE, METRE * (d + CAR) - enter));
        }
    }
    blocked.sort();
    let mut start = 0;
    for (low, high) in blocked {
        if low >= start {
            break;
        }
        start = start.max(high);
    }
    println!("{:.6}", start as f64 / UNITS);
}
