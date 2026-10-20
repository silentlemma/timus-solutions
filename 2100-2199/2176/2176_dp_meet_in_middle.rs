use std::io::{self, Read, Write};

const TERNARY_BASE: u64 = 3;
const WORD_BITS: usize = u64::BITS as usize;
const MAX_DP_SUM: usize = 50_000_000;

fn collect(value: u64, pattern: u64, mask: u64, limit: u64, coins: &mut Vec<u64>) {
    let mut shifted = value;
    while shifted >= pattern {
        if shifted & mask == pattern {
            coins.push(value);
            break;
        }
        shifted >>= 1;
    }
    let next = value * TERNARY_BASE;
    if next <= limit {
        collect(next, pattern << 1, (mask << 1) | 1, limit, coins);
    }
    if next + 1 <= limit {
        collect(next + 1, (pattern << 1) | 1, (mask << 1) | 1, limit, coins);
    }
}

fn subset_bits(coins: &[u64], total: usize) -> Vec<u64> {
    let mut bits = vec![0; total / WORD_BITS + 1];
    bits[0] = 1;
    let mut reachable = 0;
    for &coin in coins {
        let value = coin as usize;
        let words = value / WORD_BITS;
        let offset = value % WORD_BITS;
        // Descending sources keep each coin available only once.
        for source in (0..=reachable / WORD_BITS).rev() {
            let word = bits[source];
            let target = source + words;
            bits[target] |= word << offset;
            if offset != 0 && target + 1 < bits.len() {
                bits[target + 1] |= word >> (WORD_BITS - offset);
            }
        }
        reachable += value;
    }
    bits
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let count: usize = tokens.next().unwrap().parse().unwrap();
    let queries: Vec<u64> = tokens.take(count).map(|s| s.parse().unwrap()).collect();
    let limit = *queries.iter().max().unwrap();
    let mut coins = Vec::new();
    collect(1, 1, 1, limit, &mut coins);
    coins.sort_unstable();

    let mut small_count = 0;
    let mut small_total = 0;
    while small_count < coins.len() && small_total + coins[small_count] as usize <= MAX_DP_SUM {
        small_total += coins[small_count] as usize;
        small_count += 1;
    }
    let bits = subset_bits(&coins[..small_count], small_total);
    let mut high_sums = vec![0];
    for &coin in &coins[small_count..] {
        let count = high_sums.len();
        for i in 0..count {
            high_sums.push(high_sums[i] + coin);
        }
    }
    high_sums.sort_unstable();

    let mut output = String::new();
    for query in queries {
        let mut found = false;
        for &high in &high_sums {
            if high > query {
                break;
            }
            let low = (query - high) as usize;
            if low <= small_total && (bits[low / WORD_BITS] >> (low % WORD_BITS)) & 1 != 0 {
                found = true;
                break;
            }
        }
        output.push_str(if found { "YES\n" } else { "NO\n" });
    }
    io::stdout().lock().write_all(output.as_bytes()).unwrap();
}
