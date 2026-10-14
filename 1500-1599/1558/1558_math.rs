use std::io::{self, Read};

/// x as k digits, the least significant first.
fn low_first(mut x: u64, k: usize) -> Vec<u8> {
    let mut s = Vec::with_capacity(k);
    for _ in 0..k {
        s.push(b'0' + (x % 10) as u8);
        x /= 10;
    }
    s
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    // the digits of each line, without the brackets
    let nums: Vec<String> = text
        .lines()
        .map(|line| {
            line.chars()
                .filter(|c| c.is_ascii_digit())
                .collect::<String>()
        })
        .filter(|s| !s.is_empty())
        .take(2)
        .collect();
    let k = nums[0].len();
    let top = 10u64.pow(k as u32);
    let total: u64 = nums.iter().map(|s| s.parse::<u64>().unwrap()).sum();
    // without a carry every block is the plain sum; with one, the lowest block
    // sends a carry on, and every block above it gets the carry and sends one
    let (p, mut digits) = if total < top {
        let p = low_first(total, k);
        (p.clone(), p)
    } else {
        let p = low_first(total + 1 - top, k);
        let mut digits = low_first(total - top, k);
        digits.extend_from_slice(&p);
        (p, digits)
    };
    // the shortest period of the repeated block, then the shortest tail after
    // which every digit repeats the digit that period further up
    let d = (1..=k)
        .find(|&d| k % d == 0 && (0..k).all(|i| p[i] == p[(i + d) % k]))
        .unwrap();
    digits.extend_from_slice(&p);
    digits.extend_from_slice(&p);
    let mut start = digits.len() - 2 * k;
    while start > 0 && digits[start - 1] == digits[start - 1 + d] {
        start -= 1;
    }
    let period: String = digits[start..start + d]
        .iter()
        .rev()
        .map(|&c| c as char)
        .collect();
    let tail: String = digits[..start].iter().rev().map(|&c| c as char).collect();
    println!("({}){}", period, tail);
}
