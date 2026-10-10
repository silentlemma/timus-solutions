use std::cmp::Ordering;
use std::io::{self, Read};

// Nonnegative integers stored in base 100, with no rounding.
#[derive(Clone)]
struct Amount(Vec<u32>);

impl Amount {
    fn parse(text: &str) -> Self {
        let mut digits = Vec::new();
        let mut end = text.len();
        while end > 0 {
            let start = end.saturating_sub(2);
            digits.push(text[start..end].parse().unwrap());
            end = start;
        }
        let mut result = Self(digits);
        result.trim();
        result
    }

    fn trim(&mut self) {
        while self.0.len() > 1 && self.0.last() == Some(&0) {
            self.0.pop();
        }
    }

    fn cmp(&self, other: &Self) -> Ordering {
        self.0.len().cmp(&other.0.len()).then_with(|| self.0.iter().rev().cmp(other.0.iter().rev()))
    }

    fn mul(&self, factor: u32) -> Self {
        let mut digits = Vec::new();
        let mut carry = 0;
        for digit in &self.0 {
            carry += digit * factor;
            digits.push(carry % 100);
            carry /= 100;
        }
        while carry > 0 {
            digits.push(carry % 100);
            carry /= 100;
        }
        let mut result = Self(digits);
        result.trim();
        result
    }

    fn sub(&self, other: &Self) -> Self {
        let mut result = self.clone();
        let mut borrow = 0;
        for (i, digit) in self.0.iter().enumerate() {
            let value = *digit as i32 - borrow - other.0.get(i).copied().unwrap_or(0) as i32;
            borrow = i32::from(value < 0);
            result.0[i] = (value + borrow * 100) as u32;
        }
        result.trim();
        result
    }
}

fn scaled(text: &str, places: usize) -> String {
    let text = text.trim_start_matches(|c| c == '+' || c == '-');
    let digits = text.find('.').map_or(0, |dot| text.len() - dot - 1);
    text.replace('.', "") + &"0".repeat(places - digits)
}

struct Exchange {
    from: usize,
    to: usize,
    rate: u32,
    fee: u32,
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tok = input.split_ascii_whitespace();
    let n: usize = tok.next().unwrap().parse().unwrap();
    let m: usize = tok.next().unwrap().parse().unwrap();
    let s: usize = tok.next().unwrap().parse().unwrap();
    let text = tok.next().unwrap();
    let places = 2.max(text.find('.').map_or(0, |dot| text.len() - dot - 1));
    let mut v = Amount::parse(&scaled(text, places));
    let mut unit = Amount::parse(&("1".to_string() + &"0".repeat(places - 2)));
    let mut edges = Vec::new();
    for _ in 0..m {
        let a: usize = tok.next().unwrap().parse().unwrap();
        let b: usize = tok.next().unwrap().parse().unwrap();
        let mut cents = || scaled(tok.next().unwrap(), 2).parse::<u32>().unwrap();
        let (rab, cab, rba, cba) = (cents(), cents(), cents(), cents());
        edges.push(Exchange {
            from: a,
            to: b,
            rate: rab,
            fee: cab,
        });
        edges.push(Exchange {
            from: b,
            to: a,
            rate: rba,
            fee: cba,
        });
    }
    // All amounts share an exact denominator, multiplied by 100 each pass.
    // A change on pass n means a reachable gaining cycle.
    let mut best: Vec<Option<Amount>> = vec![None; n + 1];
    best[s] = Some(v.clone());
    let mut changed = false;
    for _ in 0..n {
        let mut after: Vec<Option<Amount>> =
            best.iter().map(|a| a.as_ref().map(|x| x.mul(100))).collect();
        changed = false;
        for e in &edges {
            let cost = unit.mul(e.fee);
            if let Some(amount) = &best[e.from] {
                if amount.cmp(&cost) != Ordering::Less {
                    let got = amount.sub(&cost).mul(e.rate);
                    if after[e.to].as_ref().map_or(true, |old| got.cmp(old) == Ordering::Greater) {
                        after[e.to] = Some(got);
                        changed = true;
                    }
                }
            }
        }
        best = after;
        unit = unit.mul(100);
        v = v.mul(100);
        if best[s].as_ref().unwrap().cmp(&v) == Ordering::Greater || !changed {
            break;
        }
    }
    let gain = best[s].as_ref().unwrap().cmp(&v) == Ordering::Greater || changed;
    println!("{}", if gain { "YES" } else { "NO" });
}
