use std::io::{self, Read};

const FOUR: u64 = 4;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut out = String::new();
    for m in input.split_ascii_whitespace().map(|x| x.parse::<u64>().unwrap()) {
        // by the Hull-Dobell theorem the full cycles come from a - 1
        // divisible by every prime of m, and by 4 when 4 divides m, with
        // any b coprime to m; so a runs over 1, 1 + c, ..., below m
        let (mut c, mut rest) = (1u64, m);
        let mut p = 2;
        while p * p <= rest {
            if rest % p == 0 {
                c *= p;
                while rest % p == 0 {
                    rest /= p;
                }
            }
            p += 1;
        }
        if rest > 1 {
            c *= rest;
        }
        if m % FOUR == 0 {
            c *= 2;
        }
        out.push_str(&format!("{}\n", (m - c + 2) / 2));
    }
    print!("{}", out);
}
