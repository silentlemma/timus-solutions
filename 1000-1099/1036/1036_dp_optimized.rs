use std::io::{self, Read, Write};

const DIGITS: usize = 10;
const MAX_LENGTH: usize = 50;
const MAX_TARGET: usize = MAX_LENGTH * (DIGITS - 1) / 2;
const BASE: u32 = 1_000_000_000;
const LIMBS: usize = 6;
const LIMB_WIDTH: usize = 9;
type Number = [u32; LIMBS];

fn add(value: &mut Number, other: &Number) {
    let mut carry = 0;
    for (digit, &extra) in value.iter_mut().zip(other) {
        let sum = *digit + extra + carry;
        carry = u32::from(sum >= BASE);
        *digit = sum - carry * BASE;
    }
}

fn subtract(value: &mut Number, other: &Number) {
    let mut borrow = 0;
    for (digit, &extra) in value.iter_mut().zip(other) {
        let subtrahend = extra + borrow;
        borrow = u32::from(*digit < subtrahend);
        *digit = *digit + borrow * BASE - subtrahend;
    }
}

fn main() -> io::Result<()> {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input)?;
    let mut numbers = input
        .split_ascii_whitespace()
        .map(|s| s.parse::<usize>().unwrap());
    let length = numbers.next().unwrap();
    let sum = numbers.next().unwrap();
    let maximum = length * (DIGITS - 1);
    if sum % 2 != 0 || sum / 2 > maximum {
        println!("0");
        return Ok(());
    }
    let target = (sum / 2).min(maximum - sum / 2);
    let mut first = [[0; LIMBS]; MAX_TARGET + 1];
    let mut second = [[0; LIMBS]; MAX_TARGET + 1];
    let (mut current, mut next) = (&mut first, &mut second);
    current[0][0] = 1;
    for _ in 0..length {
        let mut window = [0; LIMBS];
        for t in 0..=target {
            add(&mut window, &current[t]);
            if t >= DIGITS {
                subtract(&mut window, &current[t - DIGITS]);
            }
            next[t] = window;
        }
        std::mem::swap(&mut current, &mut next);
    }

    let value = &current[target];
    let mut square = [0; 2 * LIMBS];
    let radix = u64::from(BASE);
    for (i, &left) in value.iter().enumerate() {
        let mut carry = 0;
        for (j, &right) in value.iter().enumerate() {
            let product = square[i + j] + u64::from(left) * u64::from(right) + carry;
            square[i + j] = product % radix;
            carry = product / radix;
        }
        square[i + LIMBS] = carry;
    }
    let highest = square.iter().rposition(|&digit| digit != 0).unwrap_or(0);
    let mut output = io::stdout().lock();
    write!(output, "{}", square[highest])?;
    for digit in square[..highest].iter().rev() {
        write!(output, "{digit:0LIMB_WIDTH$}")?;
    }
    writeln!(output)
}
