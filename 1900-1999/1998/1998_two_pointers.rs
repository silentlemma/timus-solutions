use std::io::{self, Read};

fn solve(weights: &[i64], events: &[i64], limit: i64) -> i64 {
    let size = weights.len();
    let mut prefix = vec![0; size + 1];
    for (i, &value) in weights.iter().enumerate() {
        prefix[i + 1] = prefix[i] + value;
    }
    let mut retreat = vec![0; size + 1];
    let mut left = 0;
    for height in 1..=size {
        while left + 1 < height && prefix[height] - prefix[left + 1] > limit {
            left += 1;
        }
        retreat[height] = left;
    }
    let mut time = 0;
    let mut height = 0;
    for &event in events {
        let ordinary = event - time - 1;
        if ordinary >= (size - height) as i64 {
            return time + (size - height) as i64;
        }
        height += ordinary as usize;
        height = retreat[height];
        time = event;
    }
    time + (size - height) as i64
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let n: usize = tokens.next().unwrap().parse().unwrap();
    let m: usize = tokens.next().unwrap().parse().unwrap();
    let limit: i64 = tokens.next().unwrap().parse().unwrap();
    let weights: Vec<i64> = (0..n)
        .map(|_| tokens.next().unwrap().parse().unwrap())
        .collect();
    let events: Vec<i64> = (0..m)
        .map(|_| tokens.next().unwrap().parse().unwrap())
        .collect();
    println!("{}", solve(&weights, &events, limit));
}
