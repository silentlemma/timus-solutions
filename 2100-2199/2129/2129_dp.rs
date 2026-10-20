use std::io::{self, Read};

const MODULUS: u64 = 1_000_000_007;

fn count_ways(n: u64, base: u64, coins: u64) -> u64 {
    if n < coins {
        return 0;
    }
    let mut digits = Vec::new();
    let mut digit_sum = 0;
    let mut value = n;
    while value > 0 {
        digits.push(value % base);
        digit_sum += value % base;
        value /= base;
    }
    if digit_sum > coins || (coins - digit_sum) % (base - 1) != 0 {
        return 0;
    }
    let budget = ((coins - digit_sum) / (base - 1)) as usize;
    if budget == 0 {
        return 1;
    }
    let mut dp: Vec<Vec<u64>> = (0..=budget).map(|used| vec![0; used + 1]).collect();
    dp[0][0] = 1;
    for level in (1..digits.len()).rev() {
        let mut next: Vec<Vec<u64>> = (0..=budget).map(|used| vec![0; used + 1]).collect();
        for (used, row) in dp.iter().enumerate() {
            let mut suffix = 0;
            let mut has_value = false;
            for &ways in row {
                suffix += ways;
                if suffix >= MODULUS {
                    suffix -= MODULUS;
                }
                has_value |= ways != 0;
            }
            if !has_value {
                continue;
            }
            let mut threshold = 0;
            for splits in 0..=budget - used {
                // Previous splits must supply enough coins at this level.
                while threshold < row.len()
                    && digits[level] + base * (threshold as u64) < splits as u64
                {
                    suffix = (suffix + MODULUS - row[threshold]) % MODULUS;
                    threshold += 1;
                }
                if threshold == row.len() {
                    break;
                }
                next[used + splits][splits] = suffix;
            }
        }
        dp = next;
    }
    dp[budget]
        .iter()
        .fold(0, |answer, ways| (answer + ways) % MODULUS)
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let cases: usize = tokens.next().unwrap().parse().unwrap();
    let mut output = String::new();
    for _ in 0..cases {
        let n = tokens.next().unwrap().parse().unwrap();
        let base = tokens.next().unwrap().parse().unwrap();
        let coins = tokens.next().unwrap().parse().unwrap();
        output.push_str(&count_ways(n, base, coins).to_string());
        output.push('\n');
    }
    print!("{output}");
}
