use std::collections::BinaryHeap;
use std::io::{self, Read};

fn main() {
    let mut s = String::new();
    io::stdin().read_to_string(&mut s).unwrap();
    let v: Vec<usize> = s
        .split_ascii_whitespace()
        .map(|x| parse_integer(x))
        .collect();
    if v.is_empty() {
        return;
    }
    let k = v[0];
    // (signs left, kind), the most signs first
    let mut heap: BinaryHeap<(usize, usize)> = (1..=k).map(|t| (v[t], t)).collect();
    let mut order = Vec::new();
    let mut prev = 0;
    while let Some(mut top) = heap.pop() {
        if top.1 == prev {
            if let Some(other) = heap.pop() {
                // the most plentiful kind was just used: take the next one
                heap.push(top);
                top = other;
            }
        }
        order.push(top.1.to_string());
        prev = top.1;
        if top.0 > 1 {
            heap.push((top.0 - 1, top.1));
        }
    }
    println!("{}", order.join(" "));
}

// Input bounds guarantee that each decimal token fits its destination integer.
// Accumulate negative values directly so the minimum signed integer also fits.
fn parse_integer<T>(word: &str) -> T
where
    T: From<u8> + std::ops::Add<Output = T> + std::ops::Sub<Output = T> + std::ops::Mul<Output = T>,
{
    let digits = word.as_bytes();
    let negative = digits[0] == b'-';
    let start = usize::from(negative || digits[0] == b'+');
    let mut value = T::from(0);
    for &byte in &digits[start..] {
        let digit = T::from(byte - b'0');
        let scaled = value * T::from(10);
        value = if negative {
            scaled - digit
        } else {
            scaled + digit
        };
    }
    value
}
