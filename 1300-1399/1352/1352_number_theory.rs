use std::io::{self, Read, Write};

// the exponents p of the first 38 Mersenne primes 2^p - 1 (OEIS A000043)
const EXPONENTS: [u32; 38] = [
    2, 3, 5, 7, 13, 17, 19, 31, 61, 89, 107, 127, 521, 607, 1279, 2203, 2281, 3217, 4253, 4423,
    9689, 9941, 11213, 19937, 21701, 23209, 44497, 86243, 110503, 132049, 216091, 756839, 859433,
    1257787, 1398269, 2976221, 3021377, 6972593,
];

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<usize>().unwrap());
    let count = it.next().unwrap();
    let mut out = String::new();
    for n in it.take(count) {
        out.push_str(&EXPONENTS[n - 1].to_string());
        out.push('\n');
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}
