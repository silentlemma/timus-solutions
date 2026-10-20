use std::fmt::Write as FmtWrite;
use std::io::{self, Read};

const MOD: u64 = 998244353;
const ROOT: u64 = 3;

fn power(mut base: u64, mut exponent: u64) -> u64 {
    let mut result = 1;
    while exponent > 0 {
        if exponent & 1 != 0 {
            result = result * base % MOD;
        }
        base = base * base % MOD;
        exponent >>= 1;
    }
    result
}

fn transform(a: &mut [u64], inverse: bool) {
    let size = a.len();
    let mut j = 0;
    for i in 1..size {
        let mut bit = size >> 1;
        while j & bit != 0 {
            j ^= bit;
            bit >>= 1;
        }
        j ^= bit;
        if i < j {
            a.swap(i, j);
        }
    }
    let mut length = 2;
    while length <= size {
        let mut step = power(ROOT, (MOD - 1) / length as u64);
        if inverse {
            step = power(step, MOD - 2);
        }
        let half = length / 2;
        for start in (0..size).step_by(length) {
            let mut weight = 1;
            for j in 0..half {
                let left = a[start + j];
                let right = weight * a[start + j + half] % MOD;
                let mut sum = left + right;
                if sum >= MOD {
                    sum -= MOD;
                }
                a[start + j] = sum;
                a[start + j + half] = if left >= right {
                    left - right
                } else {
                    left + MOD - right
                };
                weight = weight * step % MOD;
            }
        }
        length <<= 1;
    }
    if inverse {
        let scale = power(size as u64, MOD - 2);
        for value in a {
            *value = *value * scale % MOD;
        }
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let n: usize = tokens.next().unwrap().parse().unwrap();
    let days: u64 = tokens.next().unwrap().parse().unwrap();
    let size = (2 * n - 1).next_power_of_two();
    let mut values = vec![0; size];
    let mut kernel = vec![0; size];
    let mut inverses = vec![0; n];
    for value in values.iter_mut().take(n) {
        *value = tokens.next().unwrap().parse().unwrap();
    }
    inverses[1] = 1;
    kernel[0] = 1;
    // Repeated prefix sums have coefficients C(days + i - 1, i).
    for i in 1..n {
        let index = i as u64;
        if i > 1 {
            inverses[i] = MOD - (MOD / index) * inverses[(MOD % index) as usize] % MOD;
        }
        kernel[i] = kernel[i - 1] * (days + index - 1) % MOD * inverses[i] % MOD;
    }
    transform(&mut values, false);
    transform(&mut kernel, false);
    for i in 0..size {
        values[i] = values[i] * kernel[i] % MOD;
    }
    transform(&mut values, true);
    let mut answer = String::new();
    for (i, value) in values.iter().take(n).enumerate() {
        if i > 0 {
            answer.push(' ');
        }
        write!(answer, "{}", value).unwrap();
    }
    println!("{}", answer);
}
