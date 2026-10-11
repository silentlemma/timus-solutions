use std::io::{self, Read};

const CENTS: i64 = 100;
const DIGITS: usize = 2;

struct Taxes {
    limits: Vec<i64>,
    rates: Vec<i64>,
    top_rate: i64,
    bonus_rate: i64,
}

// a non-negative amount with at most two decimals, in cents
fn cents(token: &str) -> i64 {
    let (whole, frac) = match token.find('.') {
        Some(dot) => (&token[..dot], &token[dot + 1..]),
        None => (token, ""),
    };
    let frac = format!("{}00", frac);
    let w: i64 = if whole.is_empty() {
        0
    } else {
        whole.parse().unwrap()
    };
    w * CENTS + frac[..DIGITS].parse::<i64>().unwrap()
}

// rate percent of an amount in cents, rounded half up to a cent
fn percent(amount: i64, rate: i64) -> i64 {
    (amount * rate + CENTS / 2) / CENTS
}

impl Taxes {
    fn tax(&self, amount: i64) -> i64 {
        let (mut raw, mut previous) = (0, 0);
        for (&limit, &rate) in self.limits.iter().zip(&self.rates) {
            if amount <= limit {
                return (raw + (amount - previous) * rate + CENTS / 2) / CENTS;
            }
            raw += (limit - previous) * rate;
            previous = limit;
        }
        (raw + (amount - previous) * self.top_rate + CENTS / 2) / CENTS
    }

    fn net(&self, gross: i64) -> i64 {
        let bonus = percent(gross, self.bonus_rate);
        gross - self.tax(gross) + bonus - self.tax(bonus)
    }

    // net never decreases as the salary grows, so the largest salary
    // whose net does not exceed the amount paid is found by bisection
    fn gross_for(&self, amount: i64) -> i64 {
        let (mut lo, mut hi) = (0i64, 1i64);
        while self.net(hi) <= amount {
            hi *= 2;
        }
        while hi - lo > 1 {
            let mid = (lo + hi) / 2;
            if self.net(mid) <= amount {
                lo = mid;
            } else {
                hi = mid;
            }
        }
        lo
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_ascii_whitespace();
    let mut taxes = Taxes {
        limits: Vec::new(),
        rates: Vec::new(),
        top_rate: 0,
        bonus_rate: words.next().unwrap().parse().unwrap(),
    };
    loop {
        let limit = cents(words.next().unwrap());
        let rate: i64 = words.next().unwrap().parse().unwrap();
        if limit == 0 {
            taxes.top_rate = rate;
            break;
        }
        taxes.limits.push(limit);
        taxes.rates.push(rate);
    }
    let (mut total, mut withheld) = (0i64, 0i64);
    for token in words.take_while(|&t| t != "-1") {
        let gross = taxes.gross_for(cents(token));
        total += gross;
        withheld += taxes.tax(gross) + taxes.tax(percent(gross, taxes.bonus_rate));
    }
    let owed = taxes.tax(total) + taxes.tax(percent(total, taxes.bonus_rate)) - withheld;
    let sign = if owed < 0 { "-" } else { "" };
    println!("{}{}.{:02}", sign, owed.abs() / CENTS, owed.abs() % CENTS);
}
