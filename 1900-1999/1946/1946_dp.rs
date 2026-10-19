use std::io::{self, Read};

const GOALS: i32 = 3;
const MODULUS: i64 = 1000000007;

fn count_forecasts(size: i32) -> i32 {
    let total = GOALS * size * (size - 1) / 2;
    let maximum = GOALS * (size - 1);
    let stride = (maximum + 1) as usize;
    let mut max_rows: i32 = 1;
    for used in 0..=size {
        max_rows = max_rows.max(total * used / size - GOALS * used * (used - 1) / 2 + 1);
    }
    let capacity = max_rows as usize * stride;
    let mut current: Vec<i32> = vec![0; capacity];
    let mut following: Vec<i32> = vec![0; capacity];
    current[0] = 1;
    let (mut lower, mut upper) = (0, 0);
    for used in 0..size {
        let next_used = used + 1;
        let next_lower = GOALS * next_used * used / 2;
        let next_upper = total * next_used / size;
        following.fill(0);
        for partial in lower..=upper {
            let minimum_last = if used > 0 {
                (partial + used - 1) / used
            } else {
                0
            };
            let first = 0.max(next_lower - partial).max(minimum_last);
            let last = maximum
                .min(next_upper - partial)
                .min((total - partial) / (size - used));
            if first > last {
                continue;
            }
            let row = (partial - lower) as usize * stride;
            let mut prefix: i64 = 0;
            for value in 0..first {
                prefix += i64::from(current[row + value as usize]);
            }
            for value in first..=last {
                prefix += i64::from(current[row + value as usize]);
                if prefix != 0 {
                    let index = (partial + value - next_lower) as usize * stride + value as usize;
                    following[index] = (prefix % MODULUS) as i32;
                }
            }
        }
        std::mem::swap(&mut current, &mut following);
        lower = next_lower;
        upper = next_upper;
    }
    let answer: i64 = current[..stride]
        .iter()
        .map(|&value| i64::from(value))
        .sum();
    (answer % MODULUS) as i32
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    println!("{}", count_forecasts(input.trim().parse().unwrap()));
}
