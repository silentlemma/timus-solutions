use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let depth: u64 = tokens.next().unwrap().parse().unwrap();
    let index = tokens.next().unwrap().parse::<u64>().unwrap() - 1;

    let mut path_bits = 0u32;
    let mut remaining = index;
    while remaining > 0 {
        path_bits += 1;
        remaining >>= 1;
    }

    let (mut left_numerator, mut left_denominator) = (0u64, 1u64);
    let mut right_numerator = 1u64;
    // Leading left moves only increase the right denominator.
    let mut right_denominator = depth - 1 - u64::from(path_bits);
    for bit in (0..path_bits).rev() {
        if (index >> bit) & 1 == 0 {
            right_numerator += left_numerator;
            right_denominator += left_denominator;
        } else {
            left_numerator += right_numerator;
            left_denominator += right_denominator;
        }
    }

    println!(
        "{} {}",
        left_numerator + right_numerator,
        left_denominator + right_denominator
    );
}
