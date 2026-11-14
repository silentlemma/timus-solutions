use std::io::{self, BufWriter, Read, Write};

const FIRST_ODD_PRIME: usize = 3;
const LIMIT: usize = 1 << 16;
const MAX_FACTORS: usize = 6;

fn power(mut base: u32, mut exponent: usize, modulus: u32) -> u32 {
    let mut result = 1;
    while exponent != 0 {
        if exponent & 1 != 0 {
            result = result * base % modulus;
        }
        base = base * base % modulus;
        exponent >>= 1;
    }
    result
}

fn largest_root(prime: usize, factors: &[u8]) -> u16 {
    let order = prime - 1;
    let mut odd = order >> order.trailing_zeros();
    let mut powers = [0; MAX_FACTORS];
    let mut count = 1;
    powers[0] = order / 2;
    while odd > 1 {
        let factor = match factors[odd / 2] {
            0 => odd,
            small => usize::from(small),
        };
        powers[count] = order / factor;
        count += 1;
        while odd % factor == 0 {
            odd /= factor;
        }
    }
    (2..=order)
        .rev()
        .find(|&g| {
            powers[..count]
                .iter()
                .all(|&e| power(g as u32, e, prime as u32) != 1)
        })
        .unwrap() as u16
}

fn main() -> io::Result<()> {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input)?;
    let mut numbers = input
        .split_ascii_whitespace()
        .map(|s| s.parse::<usize>().unwrap());
    let count = numbers.next().unwrap();
    let mut factors = vec![0u8; LIMIT / 2];
    for p in (FIRST_ODD_PRIME..).step_by(2).take_while(|p| p * p < LIMIT) {
        if factors[p / 2] == 0 {
            for i in (p * p / 2..factors.len()).step_by(p) {
                if factors[i] == 0 {
                    factors[i] = p as u8;
                }
            }
        }
    }

    let mut known = vec![0u16; LIMIT / 2];
    let mut output = BufWriter::new(io::stdout().lock());
    for prime in numbers.take(count) {
        let answer = &mut known[prime / 2];
        if *answer == 0 {
            *answer = largest_root(prime, &factors);
        }
        writeln!(output, "{}", answer)?;
    }
    output.flush()
}
