use std::fmt::Write as FmtWrite;
use std::io::{self, Read};

const DAY_SLOTS: usize = 32;
const HOURS_PER_DAY: usize = 24;
const MINUTES_PER_HOUR: usize = 60;

fn solve(keys: &[usize], amounts: &[i64]) -> Vec<i64> {
    let n = keys.len();
    let mut order: Vec<usize> = (0..n).collect();
    order.sort_unstable_by_key(|&i| keys[i]);
    let mut ranks = vec![0; n];
    for (rank, &event) in order.iter().enumerate() {
        ranks[event] = rank;
    }
    let size = n.next_power_of_two();
    let mut sums = vec![0_i64; 2 * size];
    let mut prefixes = vec![0_i64; 2 * size];
    let mut result = Vec::with_capacity(n);
    for (i, &amount) in amounts.iter().enumerate() {
        let mut index = size + ranks[i];
        sums[index] = amount;
        prefixes[index] = amount.min(0);
        index >>= 1;
        while index != 0 {
            let left = index << 1;
            let right = left + 1;
            sums[index] = sums[left] + sums[right];
            prefixes[index] = prefixes[left].min(sums[left] + prefixes[right]);
            index >>= 1;
        }
        result.push(prefixes[1]);
    }
    result
}

fn number(data: &[u8], at: &mut usize) -> i64 {
    while *at < data.len() && !data[*at].is_ascii_digit() && data[*at] != b'-' && data[*at] != b'+'
    {
        *at += 1;
    }
    let mut sign = 1;
    if data[*at] == b'-' || data[*at] == b'+' {
        if data[*at] == b'-' {
            sign = -1;
        }
        *at += 1;
    }
    let mut value = 0_i64;
    while *at < data.len() && data[*at].is_ascii_digit() {
        value = value * 10 + i64::from(data[*at] - b'0');
        *at += 1;
    }
    sign * value
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let data = input.as_bytes();
    let mut at = 0;
    let n = number(data, &mut at) as usize;
    let mut keys = Vec::with_capacity(n);
    let mut amounts = Vec::with_capacity(n);
    for _ in 0..n {
        amounts.push(number(data, &mut at));
        let day = number(data, &mut at) as usize;
        let month = number(data, &mut at) as usize;
        let hour = number(data, &mut at) as usize;
        let minute = number(data, &mut at) as usize;
        keys.push(((month * DAY_SLOTS + day) * HOURS_PER_DAY + hour) * MINUTES_PER_HOUR + minute);
    }
    let mut output = String::new();
    for value in solve(&keys, &amounts) {
        writeln!(output, "{}", value).unwrap();
    }
    print!("{}", output);
}
