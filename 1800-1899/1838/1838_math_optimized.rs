use std::io::{self, Read};

const DECIMAL: i32 = 10;

fn number(input: &mut impl Iterator<Item = io::Result<u8>>) -> i32 {
    input
        .by_ref()
        .map(Result::unwrap)
        .skip_while(u8::is_ascii_whitespace)
        .take_while(u8::is_ascii_digit)
        .fold(0, |value, digit| value * DECIMAL + i32::from(digit - b'0'))
}

fn main() {
    let stdin = io::stdin();
    let mut input = io::BufReader::new(stdin.lock()).bytes();
    let length = number(&mut input);
    let count = number(&mut input);
    let supports: Vec<_> = (0..count).map(|_| number(&mut input)).collect();
    let min_cut = 2 * supports[0];
    let max_cut = 2 * supports[supports.len() - 1] - length;
    let mut safe = 0;
    if min_cut < max_cut {
        let start = supports
            .partition_point(|&position| position <= min_cut)
            .saturating_sub(1);
        for pair in supports[start..].windows(2) {
            let (left, right) = (pair[0], pair[1]);
            if left >= max_cut {
                break;
            }
            let lo = left.max(min_cut).max(2 * right - length);
            let hi = right.min(max_cut).min(2 * left);
            safe += (hi - lo).max(0);
        }
    }
    println!("{}", length - safe);
}
