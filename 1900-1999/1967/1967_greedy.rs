use std::fmt::Write;
use std::io::{self, Read};

const DECIMAL_BASE: u32 = 10;

fn times_ten(value: &[u8]) -> Vec<u8> {
    let mut carry = 0;
    let mut result = Vec::new();
    for &bit in value.iter().rev() {
        carry += u32::from(bit - b'0') * DECIMAL_BASE;
        result.push(b'0' + (carry % 2) as u8);
        carry /= 2;
    }
    while carry > 0 {
        result.push(b'0' + (carry % 2) as u8);
        carry /= 2;
    }
    result.reverse();
    result
}

fn optimal_lengths(bits: &[u8]) -> Vec<usize> {
    let mut powers: Vec<Vec<u8>> = Vec::new();
    let mut power = vec![b'1'];
    let mut end = bits.len();
    let mut lengths = Vec::new();
    while end > 0 {
        let mut index = 0;
        loop {
            if index == powers.len() {
                power = times_ten(&power);
                powers.push(power.clone());
            }
            let threshold = &powers[index];
            let length = threshold.len();
            if length >= end {
                lengths.push(end);
                lengths.reverse();
                return lengths;
            }
            let start = end - length;
            if bits[start] == b'1' && &bits[start..end] < threshold.as_slice() {
                lengths.push(length);
                end = start;
                break;
            }
            index += 1;
        }
    }
    lengths.reverse();
    lengths
}

fn make_bits(maximum: usize) -> Vec<u8> {
    let mut bits = String::new();
    for value in 1..=maximum {
        write!(&mut bits, "{:b}", value).unwrap();
    }
    bits.into_bytes()
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let maximum: usize = input.trim().parse().unwrap();
    let lengths = optimal_lengths(&make_bits(maximum));
    let mut output = format!("{}\n", lengths.len());
    for length in lengths {
        write!(&mut output, "{} ", length).unwrap();
    }
    output.push('\n');
    print!("{}", output);
}
