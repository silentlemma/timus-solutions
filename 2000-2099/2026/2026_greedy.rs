use std::io::{self, Read};

fn solve(pattern: &str, limit: usize) -> String {
    const ALPHABET: usize = 26;
    let mut fixed = [false; ALPHABET + 1];
    let mut positive = Vec::new();
    let mut negative = Vec::new();
    for (index, letter) in pattern.bytes().enumerate() {
        if letter != b'?' {
            fixed[(letter - b'a' + 1) as usize] = true;
        } else if index % 2 == 0 {
            positive.push(index);
        } else {
            negative.push(index);
        }
    }
    let fixed_count = fixed.iter().filter(|&&used| used).count();
    let needed = limit.saturating_sub(fixed_count);
    if positive.len() + negative.len() < needed {
        return "-1".to_string();
    }
    let missing: Vec<usize> = (1..=ALPHABET).filter(|&value| !fixed[value]).collect();
    let count = missing.len();
    let mut low = vec![0; count + 1];
    let mut high = vec![0; count + 1];
    for index in 0..count {
        low[index + 1] = low[index] + missing[index] - 1;
        high[index + 1] = high[index] + ALPHABET - missing[count - 1 - index];
    }
    let lower = needed.saturating_sub(negative.len());
    let upper = needed.min(positive.len());
    let mut best_cost = ALPHABET * ALPHABET;
    let mut chosen = 0;
    for take in lower..=upper {
        let cost = high[take] + low[needed - take];
        if cost < best_cost {
            best_cost = cost;
            chosen = take;
        }
    }
    let mut answer = pattern.as_bytes().to_vec();
    for &index in &positive {
        answer[index] = b'z';
    }
    for &index in &negative {
        answer[index] = b'a';
    }
    for index in 0..chosen {
        answer[positive[index]] = b'a' + (missing[count - 1 - index] - 1) as u8;
    }
    for index in 0..needed - chosen {
        answer[negative[index]] = b'a' + (missing[index] - 1) as u8;
    }
    String::from_utf8(answer).unwrap()
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let pattern = tokens.next().unwrap();
    let limit = tokens.next().unwrap().parse().unwrap();
    println!("{}", solve(pattern, limit));
}
