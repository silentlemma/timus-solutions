use std::fmt::Write as FmtWrite;
use std::io::{self, Read, Write};

const MODULUS: u64 = 998244353;
const PRIMITIVE_ROOT: u64 = 3;

fn power(mut base: u64, mut exponent: u64) -> u64 {
    let mut result = 1;
    while exponent > 0 {
        if exponent & 1 != 0 {
            result = result * base % MODULUS;
        }
        base = base * base % MODULUS;
        exponent >>= 1;
    }
    result
}

fn make_roots(size: usize) -> Vec<u64> {
    let mut roots = vec![0; size];
    roots[1] = 1;
    let mut length = 2;
    while length < size {
        let step = power(PRIMITIVE_ROOT, (MODULUS - 1) / (length * 2) as u64);
        for index in length / 2..length {
            roots[index * 2] = roots[index];
            roots[index * 2 + 1] = roots[index] * step % MODULUS;
        }
        length <<= 1;
    }
    roots
}

fn forward_transform(values: &mut [u64], roots: &[u64]) {
    let size = values.len();
    let mut length = size;
    while length > 1 {
        let half = length / 2;
        for start in (0..size).step_by(length) {
            for offset in 0..half {
                let first = values[start + offset];
                let second = values[start + offset + half];
                let sum = first + second;
                let difference = first + MODULUS - second;
                values[start + offset] = if sum >= MODULUS { sum - MODULUS } else { sum };
                values[start + offset + half] = difference * roots[half + offset] % MODULUS;
            }
        }
        length >>= 1;
    }
}

fn reverse_transform(values: &mut [u64], roots: &[u64]) {
    let size = values.len();
    let mut length = 2;
    while length <= size {
        let half = length / 2;
        for start in (0..size).step_by(length) {
            for offset in 0..half {
                let first = values[start + offset];
                let second = values[start + offset + half] * roots[half + offset] % MODULUS;
                let sum = first + second;
                let difference = first + MODULUS - second;
                values[start + offset] = if sum >= MODULUS { sum - MODULUS } else { sum };
                values[start + offset + half] = if difference >= MODULUS {
                    difference - MODULUS
                } else {
                    difference
                };
            }
        }
        length <<= 1;
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let n: usize = tokens.next().unwrap().parse().unwrap();
    let m: usize = tokens.next().unwrap().parse().unwrap();
    let total = n + m;
    let mut size = 1;
    while size < n + total - 1 {
        size <<= 1;
    }

    let mut factorial = vec![1; total];
    let mut inverse_factorial = vec![1; total];
    for index in 1..total {
        factorial[index] = factorial[index - 1] * index as u64 % MODULUS;
    }
    inverse_factorial[total - 1] = power(factorial[total - 1], MODULUS - 2);
    for index in (1..total).rev() {
        inverse_factorial[index - 1] = inverse_factorial[index] * index as u64 % MODULUS;
    }

    let mut first = vec![0; size];
    let mut second = vec![0; size];
    for index in 0..n {
        let value: u64 = tokens.next().unwrap().parse().unwrap();
        let mut weight = value * inverse_factorial[index] % MODULUS;
        weight = weight * inverse_factorial[n - 1 - index] % MODULUS;
        if (n - 1 - index) & 1 != 0 && weight != 0 {
            weight = MODULUS - weight;
        }
        first[index] = weight;
    }
    for index in 1..total {
        second[index] = factorial[index - 1] * inverse_factorial[index] % MODULUS;
    }

    let roots = make_roots(size);
    forward_transform(&mut first, &roots);
    forward_transform(&mut second, &roots);
    for index in 0..size {
        first[index] = first[index] * second[index] % MODULUS;
    }
    reverse_transform(&mut first, &roots);

    // The paired passes leave coefficients reversed and multiplied by size.
    let inverse_size = power(size as u64, MODULUS - 2);
    let mut output = String::new();
    for index in n..total {
        let mut answer = first[size - index] * inverse_size % MODULUS;
        answer = answer * factorial[index] % MODULUS * inverse_factorial[index - n] % MODULUS;
        if index > n {
            output.push(' ');
        }
        write!(output, "{}", answer).unwrap();
    }
    output.push('\n');
    io::stdout().write_all(output.as_bytes()).unwrap();
}
