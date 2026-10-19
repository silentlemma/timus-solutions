use std::io::{self, Read};

fn visit(first: u32, last: u32, dimensions: u32, answer: &mut Vec<u32>) {
    if dimensions & (dimensions - 1) == 0 {
        answer.push(first);
        if last != first {
            answer.push(last);
        }
        return;
    }
    let difference = first ^ last;
    let split = difference & difference.wrapping_neg();
    let remaining = dimensions ^ split;
    let mut bridge = remaining & remaining.wrapping_neg();
    if first ^ bridge ^ split == last && remaining != bridge {
        let choices = remaining ^ bridge;
        bridge = choices & choices.wrapping_neg();
    }
    let middle = first ^ bridge;
    visit(first, middle, remaining, answer);
    visit(middle ^ split, last, remaining, answer);
}

fn build_path(start: u32, finish: u32, free: u32) -> Vec<u32> {
    let mut answer = Vec::with_capacity(1 << free.count_ones());
    visit(start, finish, free, &mut answer);
    answer
}

fn read_mask(tokens: &mut std::str::SplitWhitespace<'_>) -> u32 {
    let count: usize = tokens.next().unwrap().parse().unwrap();
    let mut mask = 0;
    for _ in 0..count {
        let bit: u32 = tokens.next().unwrap().parse().unwrap();
        mask |= 1 << (bit - 1);
    }
    mask
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let dimensions: u32 = tokens.next().unwrap().parse().unwrap();
    let start = read_mask(&mut tokens);
    let finish = read_mask(&mut tokens);
    let path = build_path(start, finish, (1 << dimensions) - 1);
    let mut out = path.len().to_string();
    out.push('\n');
    for mut mask in path {
        out.push_str(&mask.count_ones().to_string());
        while mask != 0 {
            let bit = mask & mask.wrapping_neg();
            out.push(' ');
            out.push_str(&(bit.trailing_zeros() + 1).to_string());
            mask ^= bit;
        }
        out.push('\n');
    }
    print!("{out}");
}
