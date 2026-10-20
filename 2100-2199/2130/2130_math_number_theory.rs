use std::fmt::Write as _;
use std::io::{self, Read, Write};

const MAX_VALUE: u64 = 1_000_000_000_000;

fn gcd(mut left: u64, mut right: u64) -> u64 {
    while right != 0 {
        let remainder = left % right;
        left = right;
        right = remainder;
    }
    left
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let count: usize = tokens.next().unwrap().parse().unwrap();
    let mut multiple: u64 = 1;
    let mut forbidden: Vec<u64> = Vec::with_capacity(count);
    let mut possible = true;
    let mut output = String::new();

    for _ in 0..count {
        let divisor: u64 = tokens.next().unwrap().parse().unwrap();
        let answer: u64 = tokens.next().unwrap().parse().unwrap();

        if possible {
            if answer == 0 {
                if multiple % divisor == 0 {
                    possible = false;
                } else {
                    forbidden.push(divisor);
                }
            } else {
                let factor = divisor / gcd(multiple, divisor);
                if multiple > MAX_VALUE / factor {
                    possible = false;
                } else if factor != 1 {
                    multiple *= factor;
                    // Each scan follows a growth by at least a factor of two.
                    for &denied in &forbidden {
                        if multiple % denied == 0 {
                            possible = false;
                            break;
                        }
                    }
                }
            }
        }

        if possible {
            writeln!(output, "{multiple}").unwrap();
        } else {
            writeln!(output, "-1").unwrap();
        }
    }

    io::stdout().lock().write_all(output.as_bytes()).unwrap();
}
