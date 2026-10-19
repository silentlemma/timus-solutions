use std::io::{self, Read};

const MAX_CARDS: usize = 100;
const MOD: u64 = 1_000_000_007;

fn power(mut base: u64, mut exponent: u64) -> u64 {
    let mut result = 1;
    while exponent > 0 {
        if exponent % 2 == 1 {
            result = result * base % MOD;
        }
        base = base * base % MOD;
        exponent /= 2;
    }
    result
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut values = input
        .split_whitespace()
        .map(|word| word.parse::<usize>().unwrap());
    let Some(colors) = values.next() else {
        return;
    };
    let drawn = values.next().unwrap();
    let total: Vec<usize> = values.by_ref().take(colors + 1).collect();
    let shown: Vec<usize> = values.by_ref().take(colors + 1).collect();
    let remaining: Vec<usize> = total.iter().zip(&shown).map(|(a, b)| a - b).collect();
    let unseen: usize = remaining.iter().sum();
    let required = values.next().unwrap();
    let revealed = values.next().unwrap();
    let deck = unseen - drawn;

    let mut choose = vec![vec![0_u128; MAX_CARDS + 1]; MAX_CARDS + 1];
    let mut binomial = vec![vec![0_u64; MAX_CARDS + 1]; MAX_CARDS + 1];
    for n in 0..=MAX_CARDS {
        choose[n][0] = 1;
        binomial[n][0] = 1;
        for r in 1..=n {
            choose[n][r] = choose[n - 1][r - 1] + choose[n - 1][r];
            binomial[n][r] = (choose[n][r] % u128::from(MOD)) as u64;
        }
    }

    let mut ways = vec![vec![0_u128; revealed + 1]; deck + 1];
    for matching in 0..=deck {
        let mut prefix = 0;
        for limit in 0..=revealed {
            prefix += choose[matching][limit] * choose[deck - matching][revealed - limit];
            ways[matching][limit] = prefix;
        }
    }

    let mut answer = 0;
    let other = unseen - remaining[0];
    let first = drawn.saturating_sub(other);
    let last = remaining[0].min(drawn);
    for wild in first..=last {
        let need = drawn - wild;
        let score = |color: usize, count: usize| -> u128 {
            let hand = shown[0] + wild + shown[color] + count;
            let matching = total[0] + total[color] - hand;
            if matching > deck || hand < required {
                return 0;
            }
            ways[matching][revealed.min(hand - required)]
        };
        let mut baseline = 0;
        for color in 1..=colors {
            baseline = baseline.max(score(color, 0));
        }
        let mut events = Vec::new();
        for (color, &available) in remaining.iter().enumerate().skip(1) {
            for count in 1..=available.min(need) {
                events.push((baseline.max(score(color, count)), color, count));
            }
        }
        events.sort_unstable();

        let mut dp = vec![0_u64; need + 1];
        let mut quotient = vec![0_u64; need + 1];
        let mut cap = vec![0; colors + 1];
        dp[0] = 1;
        let mut weighted = (baseline % u128::from(MOD)) as u64 * dp[need] % MOD;
        for (value, color, count) in events {
            let before = dp[need];
            let factor = &binomial[remaining[color]];
            // Divide out the old color factor, whose constant coefficient is one.
            for degree in 0..=need - count {
                let mut coefficient = dp[degree];
                for part in 1..=cap[color].min(degree) {
                    coefficient =
                        (coefficient + MOD - factor[part] * quotient[degree - part] % MOD) % MOD;
                }
                quotient[degree] = coefficient;
            }
            for degree in 0..=need - count {
                dp[degree + count] =
                    (dp[degree + count] + factor[count] * quotient[degree] % MOD) % MOD;
            }
            cap[color] = count;
            let added = (dp[need] + MOD - before) % MOD;
            weighted = (weighted + (value % u128::from(MOD)) as u64 * added % MOD) % MOD;
        }
        answer = (answer + binomial[remaining[0]][wild] * weighted % MOD) % MOD;
    }

    let denominator = binomial[unseen][drawn] * binomial[deck][revealed] % MOD;
    println!("{}", answer * power(denominator, MOD - 2) % MOD);
}
