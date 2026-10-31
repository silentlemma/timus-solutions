use std::io::{self, BufWriter, Read, Write};
const MAX_SUM: usize = 1800;
const LIMB_DIGITS: usize = 9;
// big numbers: base 10^9 digits, least significant first.
const BASE: u64 = 1_000_000_000;
fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input
        .split_ascii_whitespace()
        .map(|w| w.parse::<u64>().unwrap());
    let (n, k) = (words.next().unwrap(), words.next().unwrap());
    // the answer is below 10^n and n < 1800, so fixed limb arrays suffice.
    let mut zero = [0u64; MAX_SUM / LIMB_DIGITS + 1];
    let mut other = zero;
    // numbers of valid prefixes ending with a zero and with another digit,
    // where the first digit is not zero.
    other[0] = k - 1;
    let mut used = 1;
    for _ in 1..n {
        let mut carry = 0;
        for j in 0..used {
            // k <= 10 keeps the intermediate below 18 * base, within u64.
            let next = (zero[j] + other[j]) * (k - 1) + carry;
            zero[j] = other[j];
            other[j] = next % BASE;
            carry = next / BASE;
        }
        if carry != 0 {
            other[used] = carry;
            used += 1;
        }
    }
    let mut carry = 0;
    for limb in 0..used {
        let next = zero[limb] + other[limb] + carry;
        other[limb] = next % BASE;
        carry = next / BASE;
    }
    if carry != 0 {
        other[used] = carry;
        used += 1;
    }
    let mut out = BufWriter::new(io::stdout().lock());
    write!(out, "{}", other[used - 1]).unwrap();
    for &limb in other[..used - 1].iter().rev() {
        write!(out, "{:0width$}", limb, width = LIMB_DIGITS).unwrap();
    }
    writeln!(out).unwrap();
}
