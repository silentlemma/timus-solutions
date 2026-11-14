use std::io::{self, BufRead, BufWriter, Write};

const MODULUS: i32 = 2007;

fn inverse(value: i32) -> i32 {
    let (mut a, mut b, mut u, mut v) = (value, MODULUS, 1, 0);
    while b != 0 {
        let q = a / b;
        (a, b) = (b, a - q * b);
        (u, v) = (v, u - q * v);
    }
    u.rem_euclid(MODULUS)
}

fn number(input: &mut impl BufRead) -> i32 {
    let mut value = 0;
    let mut sign = 1;
    let mut started = false;
    loop {
        let bytes = input.fill_buf().unwrap();
        if bytes.is_empty() {
            return sign * value;
        }
        let mut consumed = 0;
        for &byte in bytes {
            consumed += 1;
            match byte {
                b'0'..=b'9' => {
                    started = true;
                    value = value * 10 + i32::from(byte - b'0');
                }
                b'-' => sign = -1,
                _ if started => {
                    input.consume(consumed);
                    return sign * value;
                }
                _ => (),
            }
        }
        input.consume(consumed);
    }
}

fn main() {
    let stdin = io::stdin();
    let mut input = stdin.lock();
    let n = number(&mut input) as usize;
    let mut values = vec![0u16; n + 1];
    for value in &mut values[1..] {
        *value = number(&mut input).rem_euclid(MODULUS) as u16;
    }
    let first = inverse(i32::from(values[1]));
    let mut sums = vec![0u16; n + 1];
    let mut output = BufWriter::new(io::stdout().lock());
    for d in 1..=n {
        let g = if d == 1 {
            first
        } else {
            write!(output, " ").unwrap();
            (-first * i32::from(sums[d])).rem_euclid(MODULUS)
        };
        write!(output, "{}", g).unwrap();
        // Zero coefficients never affect any multiple of d.
        if g != 0 {
            for (multiple, &value) in (2 * d..=n).step_by(d).zip(&values[2..]) {
                let sum = i32::from(sums[multiple]) + i32::from(value) * g;
                sums[multiple] = (sum % MODULUS) as u16;
            }
        }
    }
    writeln!(output).unwrap();
}
