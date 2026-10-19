use std::io::{self, Read};

const MAX_DISCOUNT: usize = 100;
const MAX_PRICE: usize = 50000;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_ascii_whitespace();
    let n: usize = tokens.next().unwrap().parse().unwrap();
    let m: usize = tokens.next().unwrap().parse().unwrap();
    let mut prices = vec![Vec::<usize>::new(); MAX_DISCOUNT + 1];
    let mut required = vec![n + 1; MAX_DISCOUNT + 1];
    let mut singles = 0i64;
    for _ in 0..n {
        let price: usize = tokens.next().unwrap().parse().unwrap();
        let discount: usize = tokens.next().unwrap().parse().unwrap();
        prices[discount].push(price);
        singles += price as i64 * (MAX_DISCOUNT - discount) as i64;
    }
    for _ in 0..m {
        let count: usize = tokens.next().unwrap().parse().unwrap();
        let discount: usize = tokens.next().unwrap().parse().unwrap();
        required[discount] = required[discount].min(count);
    }

    let mut sums = vec![vec![0i64]; MAX_DISCOUNT + 1];
    let mut counts = vec![0; MAX_DISCOUNT + 1];
    let mut price_totals = vec![0i64; MAX_DISCOUNT + 1];
    let mut weighted_totals = vec![0i64; MAX_DISCOUNT + 1];
    for discount in 0..=MAX_DISCOUNT {
        prices[discount].sort_unstable();
        for &price in &prices[discount] {
            let total = sums[discount].last().unwrap() + price as i64;
            sums[discount].push(total);
        }
        counts[discount] = prices[discount].len();
        price_totals[discount] = *sums[discount].last().unwrap();
        weighted_totals[discount] = price_totals[discount] * discount as i64;
        if discount > 0 {
            counts[discount] += counts[discount - 1];
            price_totals[discount] += price_totals[discount - 1];
            weighted_totals[discount] += weighted_totals[discount - 1];
        }
    }

    let mut best = singles;
    for discount in 1..=MAX_DISCOUNT {
        if required[discount] > n {
            continue;
        }
        let mut candidate =
            singles + weighted_totals[discount] - discount as i64 * price_totals[discount];
        if candidate >= best {
            continue;
        }
        if required[discount] > counts[discount] {
            let need = required[discount] - counts[discount];
            // Find the least extra cost that supplies enough tickets.
            let mut low = 0;
            let mut high = MAX_PRICE * (MAX_DISCOUNT - discount);
            while low < high {
                let middle = low + (high - low) / 2;
                let mut taken = 0;
                for (other, group) in prices.iter().enumerate().skip(discount + 1) {
                    let limit = middle / (other - discount);
                    taken += group.partition_point(|&price| price <= limit);
                }
                if taken >= need {
                    high = middle;
                } else {
                    low = middle + 1;
                }
            }
            let mut taken = 0;
            for (other, group) in prices.iter().enumerate().skip(discount + 1) {
                let limit = low / (other - discount);
                let count = group.partition_point(|&price| price <= limit);
                taken += count;
                candidate += sums[other][count] * (other - discount) as i64;
            }
            // All surplus tickets have the threshold cost.
            candidate -= (taken - need) as i64 * low as i64;
        }
        best = best.min(candidate);
    }
    println!(
        "{}.{:02}",
        best / MAX_DISCOUNT as i64,
        best % MAX_DISCOUNT as i64
    );
}
