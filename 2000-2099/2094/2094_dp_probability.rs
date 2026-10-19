use std::io::{self, Read};

const PERCENT: usize = 100;
const OUTPUT_SCALE: u64 = 1_000_000_000;
const OUTPUT_DIGITS: usize = 9;
const MIN_DECIMALS: usize = 3;
const HALF: f64 = 0.5;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let _n: usize = tokens.next().unwrap().parse().unwrap();
    let vacancy_percent: usize = tokens.next().unwrap().parse().unwrap();
    let row = tokens.next().unwrap().as_bytes();
    let seat = row.iter().position(|&value| value == b'2').unwrap();
    let occupied = row[..seat].iter().filter(|&&value| value == b'1').count();
    let left = row[..seat].iter().filter(|&&value| value == b'0').count();
    let right = row[seat + 1..]
        .iter()
        .filter(|&&value| value == b'0')
        .count();
    let total = left + right;
    let mut step = vec![0.0; total + 1];
    let mut expected = vec![0.0; total + 1];
    let mut another = 0.0;
    let mut future = 0.0;

    // Condition the binomial arrival count on the prefix already observed.
    for remaining in 1..=total {
        let weight = (remaining * (PERCENT - vacancy_percent)) as f64;
        let absent = ((total - remaining + 1) * vacancy_percent) as f64;
        another = weight / (weight + absent * (1.0 - another));
        future = another * (1.0 + future);
        step[remaining] = another / remaining as f64;
        expected[remaining] = future / remaining as f64;
    }

    let mut dp = vec![0.0; right + 1];
    for empty_left in 1..=left {
        for empty_right in 1..=right {
            let remaining = empty_left + empty_right;
            let take_seat = empty_right as f64 * expected[remaining];
            let wait = step[remaining]
                * (empty_left as f64 * (1.0 + dp[empty_right])
                    + empty_right as f64 * dp[empty_right - 1]);
            dp[empty_right] = take_seat.min(wait);
        }
    }

    let rounded = ((occupied as f64 + dp[right]) * OUTPUT_SCALE as f64 + HALF) as u64;
    let whole = rounded / OUTPUT_SCALE;
    let mut digits = format!("{:0width$}", rounded % OUTPUT_SCALE, width = OUTPUT_DIGITS);
    while digits.len() > MIN_DECIMALS && digits.ends_with('0') {
        digits.pop();
    }
    println!("{}.{}", whole, digits);
}
