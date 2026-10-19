use std::io::{self, Read, Write};

const PERCENT_SCALE: usize = 100;

fn construct(size: usize, kept: usize, percentage: usize) -> Vec<u64> {
    let mut weights = vec![1_u64; size];
    for i in size - kept..size {
        weights[i] = weights[(percentage * i - 1) / PERCENT_SCALE] + 1;
    }
    weights
}
fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_ascii_whitespace();
    let size: usize = tokens.next().unwrap().parse().unwrap();
    let kept: usize = tokens.next().unwrap().parse().unwrap();
    let percentage: usize = tokens.next().unwrap().parse().unwrap();
    let weights = construct(size, kept, percentage);
    let total: u64 = weights.iter().sum();
    let mut output = total.to_string();
    output.push('\n');
    for (i, value) in weights.iter().enumerate() {
        if i > 0 {
            output.push(' ');
        }
        output.push_str(&value.to_string());
    }
    output.push('\n');
    io::stdout().write_all(output.as_bytes()).unwrap();
}
