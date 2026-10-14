use std::io::{self, Read, Write};

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut nums = text
        .split_ascii_whitespace()
        .map(|t| t.parse::<u32>().unwrap());
    let n = nums.next().unwrap() as usize;
    // (passengers, city) pairs in order: the cities with one count are
    // consecutive and sorted by number
    let mut pairs: Vec<(u32, u32)> = (1..=n as u32)
        .map(|city| (nums.next().unwrap(), city))
        .collect();
    pairs.sort_unstable();
    let q = nums.next().unwrap() as usize;
    let mut out = Vec::with_capacity(q + 1);
    for _ in 0..q {
        let (lo, hi, x) = (
            nums.next().unwrap(),
            nums.next().unwrap(),
            nums.next().unwrap(),
        );
        // the first city with count x and number at least lo
        let k = pairs.partition_point(|&p| p < (x, lo));
        let found = k < n && pairs[k].0 == x && pairs[k].1 <= hi;
        out.push(if found { b'1' } else { b'0' });
    }
    out.push(b'\n');
    io::stdout().write_all(&out).unwrap();
}
