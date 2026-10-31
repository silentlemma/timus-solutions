use std::io::{self, Read};

const TOP: usize = 99999;
const LAST_PARENT: usize = (TOP + 1) / 2;

fn main() {
    // n < 2^17 bounds every stern value by fibonacci(19) = 4181, fitting 16 bits.
    let mut a = vec![0u16; LAST_PARENT + 1];
    let mut best = vec![0u16; TOP + 1];
    a[1] = 1;
    best[1] = 1;
    for i in 2..=TOP {
        let value = if i % 2 == 0 {
            a[i / 2]
        } else {
            a[i / 2] + a[i / 2 + 1]
        };
        // later terms only refer to indices in the first half.
        if i <= LAST_PARENT {
            a[i] = value;
        }
        best[i] = best[i - 1].max(value);
    }
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut out = String::new();
    for n in input
        .split_ascii_whitespace()
        .map(|t| t.parse::<usize>().unwrap())
    {
        if n == 0 {
            break;
        }
        out.push_str(&best[n].to_string());
        out.push('\n');
    }
    print!("{}", out);
}
