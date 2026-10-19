use std::io::{self, Read};

const MODULUS: i64 = 40961;

fn power(mut base: i64, mut exponent: i64) -> i64 {
    let mut result = 1;
    while exponent > 0 {
        if exponent & 1 != 0 {
            result = result * base % MODULUS;
        }
        base = base * base % MODULUS;
        exponent /= 2;
    }
    result
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let text = input.split_whitespace().next().unwrap().as_bytes();
    let n = text.len();
    let mut row: Vec<i64> = text.iter().map(|&value| i64::from(value - b'0')).collect();
    let ones: i64 = row.iter().sum();

    let mut factorial = 1;
    for i in 1..=n {
        factorial = factorial * i as i64 % MODULUS;
    }
    let mut inverse_factorial = vec![0; n + 1];
    inverse_factorial[n] = power(factorial, MODULUS - 2);
    for i in (1..=n).rev() {
        inverse_factorial[i - 1] = inverse_factorial[i] * i as i64 % MODULUS;
    }

    let mut answer = vec![0; n + 1];
    let mut total = 1;
    let mut ones_total = ones;
    for k in (1..n).rev() {
        let mut squares = 0;
        // Scaling each row by (n-k)! removes division from the recurrence.
        for i in 0..k {
            let value = ((k - i) as i64 * row[i] + (i + 1) as i64 * row[i + 1]) % MODULUS;
            row[i] = value;
            squares += value * value;
        }
        total = total * (k + 1) as i64 % MODULUS;
        ones_total = ones_total * k as i64 % MODULUS;
        let difference = (total * ones_total - squares % MODULUS + MODULUS) % MODULUS;
        let inverse = inverse_factorial[n - k];
        answer[k] = difference * inverse % MODULUS * inverse % MODULUS;
    }

    let mut output = String::new();
    for (index, value) in answer.iter().skip(1).enumerate() {
        if index > 0 {
            output.push(' ');
        }
        output.push_str(&value.to_string());
    }
    println!("{}", output);
}
