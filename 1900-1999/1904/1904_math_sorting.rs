use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace().map(|x| x.parse::<i32>().unwrap());
    let count = tokens.next().unwrap() as usize;
    let constants: Vec<_> = (0..count).map(|_| tokens.next().unwrap()).collect();
    let mut intervals = vec![(0, 1)];
    for reference in constants.iter().rev() {
        let mut candidates = Vec::with_capacity(2 * intervals.len());
        for &(left, right) in &intervals {
            if right < 0 {
                continue;
            }
            let left = left.max(0);
            candidates.push((reference - right, reference - left));
            candidates.push((reference + left, reference + right));
        }
        candidates.sort_unstable();
        let mut merged: Vec<(i32, i32)> = Vec::new();
        for (left, right) in candidates {
            if let Some(last) = merged.last_mut() {
                if left <= last.1 {
                    last.1 = last.1.max(right);
                    continue;
                }
            }
            merged.push((left, right));
        }
        intervals = merged;
    }
    println!("{}", intervals.len());
    for (left, right) in intervals {
        println!("{} {}", left, right);
    }
}
