use std::io::{self, Read};

// inputs are at most this
const LARGEST: usize = 10;

fn main() {
    // a(n) counts weak orders of n objects: the k objects tied for the
    // smallest place are any k of them, followed by a weak order of the rest
    let mut binom = [[0u64; LARGEST + 1]; LARGEST + 1];
    let mut a = [0u64; LARGEST + 1];
    a[0] = 1;
    for n in 0..=LARGEST {
        binom[n][0] = 1;
        binom[n][n] = 1;
        for k in 1..n {
            binom[n][k] = binom[n - 1][k - 1] + binom[n - 1][k];
        }
    }
    for n in 1..=LARGEST {
        a[n] = (1..=n).map(|k| binom[n][k] * a[n - k]).sum();
    }
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut out = String::new();
    for token in input.split_ascii_whitespace() {
        let n: i64 = token.parse().unwrap();
        if n < 0 {
            break;
        }
        out.push_str(&format!("{}\n", a[n as usize]));
    }
    print!("{}", out);
}
