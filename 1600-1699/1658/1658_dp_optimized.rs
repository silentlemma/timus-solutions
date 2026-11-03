use std::io::{self, Read};

const LONGEST: usize = 100;
const TOP: usize = 9;
const MAX_SUM: usize = LONGEST * TOP;
const NONE: u8 = (LONGEST + 1) as u8;

fn lookup(
    total: i32,
    squares: i32,
    low: &[usize],
    high: &[usize],
    offset: &[usize],
    dp: &[u8],
) -> u8 {
    if total < 0 || total > MAX_SUM as i32 || squares < total || (squares - total) % 2 != 0 {
        return NONE;
    }
    let (sum, b) = (total as usize, ((squares - total) / 2) as usize);
    if b < low[sum] || b > high[sum] {
        return NONE;
    }
    dp[offset[sum] + b - low[sum]]
}

fn main() {
    let mut low = vec![0; MAX_SUM + 1];
    let mut high = vec![0; MAX_SUM + 1];
    let mut offset = vec![0; MAX_SUM + 2];
    for total in 0..=MAX_SUM {
        // Parity leaves b=(square_sum-total)/2. Balance 100 slots for its
        // minimum and pack nines for its maximum, bounding every row.
        let (q, r) = (total / LONGEST, total % LONGEST);
        let least = (LONGEST - r) * q * q + r * (q + 1) * (q + 1);
        let (q, r) = (total / TOP, total % TOP);
        let greatest = q * TOP * TOP + r * r;
        low[total] = (least - total) / 2;
        high[total] = (greatest - total) / 2;
        offset[total + 1] = offset[total] + high[total] - low[total] + 1;
    }
    let mut fewest = vec![NONE; offset[MAX_SUM + 1]];
    fewest[0] = 0;
    for total in 1..=MAX_SUM {
        let destination = offset[total] as isize - low[total] as isize;
        for digit in 1..=TOP.min(total) {
            let (previous, delta) = (total - digit, digit * (digit - 1) / 2);
            let first = low[total].max(low[previous] + delta);
            let last = high[total].min(high[previous] + delta);
            if first > last {
                continue;
            }
            let source = offset[previous] as isize - low[previous] as isize - delta as isize;
            for b in first..=last {
                let position = (destination + b as isize) as usize;
                let value = fewest[(source + b as isize) as usize] + 1;
                fewest[position] = fewest[position].min(value);
            }
        }
    }
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut numbers = input
        .split_ascii_whitespace()
        .map(|word| word.parse::<i32>().unwrap());
    let tests = numbers.next().unwrap();
    let mut output = String::new();
    for _ in 0..tests {
        let (mut total, mut squares) = (numbers.next().unwrap(), numbers.next().unwrap());
        let size = lookup(total, squares, &low, &high, &offset, &fewest);
        if size == NONE {
            output.push_str("No solution\n");
            continue;
        }
        let mut digit = 1;
        for left in (0..size).rev() {
            while lookup(
                total - digit,
                squares - digit * digit,
                &low,
                &high,
                &offset,
                &fewest,
            ) != left
            {
                digit += 1;
            }
            output.push((b'0' + digit as u8) as char);
            total -= digit;
            squares -= digit * digit;
        }
        output.push('\n');
    }
    print!("{}", output);
}
