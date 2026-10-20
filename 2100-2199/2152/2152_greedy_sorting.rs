use std::fmt::Write as FmtWrite;
use std::io::{self, Read, Write};

const MAX_DIGIT: u64 = 9;
const CENTS: u128 = 100;
const OUTPUT_ROW_SIZE: usize = 24;

struct Scanner {
    input: Vec<u8>,
    position: usize,
}

impl Scanner {
    fn next(&mut self) -> u64 {
        while self.position < self.input.len() && self.input[self.position].is_ascii_whitespace() {
            self.position += 1;
        }
        let mut value = 0;
        while self.position < self.input.len() && self.input[self.position].is_ascii_digit() {
            value = value * 10 + u64::from(self.input[self.position] - b'0');
            self.position += 1;
        }
        value
    }
}

struct Package {
    weight: u64,
    price: u64,
}

struct Change {
    gain: u128,
    index: usize,
    value: u64,
    weight: bool,
}

fn increase(value: u64) -> u64 {
    let mut place = 1;
    while place <= value / 10 {
        place *= 10;
    }
    while place > 0 {
        let digit = value / place % 10;
        if digit != MAX_DIGIT {
            return value + (MAX_DIGIT - digit) * place;
        }
        place /= 10;
    }
    value
}

fn main() {
    let mut input = Vec::new();
    io::stdin().read_to_end(&mut input).unwrap();
    let mut scanner = Scanner { input, position: 0 };
    let count = scanner.next() as usize;
    let budget = scanner.next() as usize;
    let max_weight = scanner.next();
    let max_price = scanner.next();
    let weight_rate = u128::from(scanner.next());
    let price_rate = u128::from(scanner.next());
    let mut packages = Vec::with_capacity(count);
    let mut changes = Vec::with_capacity(count);
    let mut total = 0;

    for index in 0..count {
        let weight = scanner.next();
        let price = scanner.next();
        let weight_excess = weight.saturating_sub(max_weight);
        let price_excess = price.saturating_sub(max_price);
        let new_weight = increase(weight);
        let new_price = increase(price);
        let weight_gain =
            u128::from(new_weight.saturating_sub(max_weight) - weight_excess) * weight_rate * CENTS;
        let price_gain =
            u128::from(new_price.saturating_sub(max_price) - price_excess) * price_rate;
        total += u128::from(weight_excess) * weight_rate * CENTS;
        total += u128::from(price_excess) * price_rate;
        packages.push(Package { weight, price });
        if weight_gain >= price_gain && weight_gain > 0 {
            changes.push(Change {
                gain: weight_gain,
                index,
                value: new_weight,
                weight: true,
            });
        } else if price_gain > 0 {
            changes.push(Change {
                gain: price_gain,
                index,
                value: new_price,
                weight: false,
            });
        }
    }

    changes.sort_unstable_by(|left, right| {
        right
            .gain
            .cmp(&left.gain)
            .then_with(|| left.index.cmp(&right.index))
    });
    for change in changes.iter().take(budget) {
        total += change.gain;
        if change.weight {
            packages[change.index].weight = change.value;
        } else {
            packages[change.index].price = change.value;
        }
    }

    let mut output = String::with_capacity(count * OUTPUT_ROW_SIZE);
    writeln!(output, "{}.{:02}", total / CENTS, total % CENTS).unwrap();
    for package in packages {
        writeln!(output, "{} {}", package.weight, package.price).unwrap();
    }
    io::stdout().lock().write_all(output.as_bytes()).unwrap();
}
