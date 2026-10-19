use std::io::{self, Read, Write};

const CYCLE: usize = 400;
const CENTURY: usize = 100;
const LEAP_STEP: usize = 4;
const WEEK: usize = 7;
const FRIDAY: usize = 4;
const TARGET_DAY: usize = 13;
const MONTHS: usize = 12;
const BUCKETS: usize = MONTHS + 1;
const MONTH_LENGTHS: [usize; MONTHS] = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

fn calendar_types() -> Vec<usize> {
    let mut weekday = 0;
    let mut types = Vec::with_capacity(CYCLE);
    for year in 1..=CYCLE {
        let leap = year % CYCLE == 0 || (year % LEAP_STEP == 0 && year % CENTURY != 0);
        let mut count = 0;
        for (month, &days) in MONTH_LENGTHS.iter().enumerate() {
            count += usize::from((weekday + TARGET_DAY - 1) % WEEK == FRIDAY);
            weekday = (weekday + days + usize::from(month == 1 && leap)) % WEEK;
        }
        types.push(count);
    }
    types
}

fn prefix(year: u64, types: &[usize], cycle_counts: &[u64; BUCKETS]) -> [u64; BUCKETS] {
    let mut answer = [0; BUCKETS];
    for k in 0..BUCKETS {
        answer[k] = year / CYCLE as u64 * cycle_counts[k];
    }
    for &count in types.iter().take((year % CYCLE as u64) as usize) {
        answer[count] += 1;
    }
    answer
}

fn solve(first: u64, last: u64, types: &[usize], cycle_counts: &[u64; BUCKETS]) -> [u64; BUCKETS] {
    let mut high = prefix(last, types, cycle_counts);
    let low = prefix(first - 1, types, cycle_counts);
    for k in 0..BUCKETS {
        high[k] -= low[k];
    }
    high
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut fields = input.split_whitespace();
    let first = fields.next().unwrap().parse().unwrap();
    let last = fields.next().unwrap().parse().unwrap();
    let types = calendar_types();
    let mut cycle_counts = [0; BUCKETS];
    for &count in &types {
        cycle_counts[count] += 1;
    }
    let answer = solve(first, last, &types, &cycle_counts);
    let mut out = io::BufWriter::new(io::stdout().lock());
    for (k, value) in answer.iter().enumerate() {
        writeln!(&mut out, "{}: {}", k, value).unwrap();
    }
}
