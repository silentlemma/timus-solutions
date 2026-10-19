use std::io::{self, Read};

const DECIMAL_BASE: usize = 10;
const MAX_DIGIT: usize = DECIMAL_BASE - 1;
type Tables = Vec<Vec<i64>>;

fn build_tables(digits: usize) -> Tables {
    let maximum = MAX_DIGIT * digits;
    let mut ways = vec![0; maximum + 1];
    ways[0] = 1;
    let mut prefix = Vec::new();
    for length in 0..digits {
        let mut row = vec![0; maximum + 1];
        let mut running = 0;
        for total in 0..=maximum {
            running += ways[total];
            row[total] = running;
        }
        prefix.push(row);
        if length + 1 == digits {
            break;
        }
        let mut next_ways = vec![0; maximum + 1];
        let mut window = 0;
        for total in 0..=maximum {
            window += ways[total];
            if total >= DECIMAL_BASE {
                window -= ways[total - DECIMAL_BASE];
            }
            next_ways[total] = window;
        }
        ways = next_ways;
    }
    prefix
}

fn count_leq(value: i64, target: usize, prefix: &Tables) -> i64 {
    let digits = value.to_string();
    let maximum = prefix[0].len() - 1;
    let mut remaining = target as i32;
    let mut result = 0;
    for (position, word) in digits.bytes().enumerate() {
        let digit = i32::from(word - b'0');
        let row = &prefix[digits.len() - position - 1];
        if digit != 0 && remaining >= 0 {
            result += row[(remaining as usize).min(maximum)];
            if remaining >= digit {
                result -= row[((remaining - digit) as usize).min(maximum)];
            }
        }
        remaining -= digit;
        if remaining < 0 {
            return result;
        }
    }
    result + i64::from(remaining == 0)
}

fn digit_sum(mut value: i64) -> usize {
    let mut total = 0;
    while value != 0 {
        total += (value % (DECIMAL_BASE as i64)) as usize;
        value /= DECIMAL_BASE as i64;
    }
    total
}

fn solve(number: i64) -> usize {
    let digits = number.to_string().len();
    let prefix = build_tables(digits);
    let (mut lower, mut answer) = (0, 0);
    for target in 1..=MAX_DIGIT * digits {
        let count = count_leq(number, target, &prefix);
        if count == 0 {
            continue;
        }
        let start = lower + 1;
        let (mut left, mut right) = (start, lower + count);
        while left <= right {
            let middle = (left + right) / 2;
            if middle - count_leq(middle, target, &prefix) <= lower {
                left = middle + 1;
            } else {
                right = middle - 1;
            }
        }
        if right >= start
            && digit_sum(right) == target
            && right - count_leq(right, target, &prefix) == lower
        {
            answer += 1;
        }
        lower += count;
    }
    answer
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let number = input.trim().parse().unwrap();
    println!("{}", solve(number));
}
