use std::io::{self, Read};

const MOD: i64 = 1_000_000_009;
// with six sectors the jumps forward and back by three land on the same
// sector, so that table is counted on its own
const SIX: i64 = 6;
const SIX_WAYS: i64 = 12;
// from seven sectors on the counts follow a linear recurrence of order 19,
// found with the Berlekamp-Massey method from counts made by a search over
// the sectors and checked on every table up to 200 sectors
const FIRST_SECTORS: i64 = 7;
const STEP_TEXT: &str = "1 2 -1 1 -2 -1 -2 -3 3 -1 5 2 2 1 -2 0 -3 0 -1";
const FIRST_TEXT: &str = concat!(
    "46 144 110 312 290 670 706 1538 1732 3504 4288 8098 ",
    "10568 19044 26042 45222 64220 108382 158324",
);

fn parse(text: &str) -> Vec<i64> {
    text.split_ascii_whitespace().map(|w| w.parse().unwrap()).collect()
}

// the product of two polynomials modulo the recurrence's characteristic
// polynomial x^k - sum of steps[j] x^(k-1-j)
fn times(p: &[i64], q: &[i64], steps: &[i64]) -> Vec<i64> {
    let k = steps.len();
    let mut full = vec![0i64; 2 * k - 1];
    for i in 0..k {
        if p[i] == 0 {
            continue;
        }
        for j in 0..k {
            full[i + j] = (full[i + j] + p[i] * q[j]) % MOD;
        }
    }
    for i in (k..2 * k - 1).rev() {
        if full[i] == 0 {
            continue;
        }
        for j in 0..k {
            full[i - 1 - j] = ((full[i - 1 - j] + full[i] * steps[j]) % MOD + MOD) % MOD;
        }
    }
    full.truncate(k);
    full
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let n: i64 = input.trim().parse().unwrap();
    if n == SIX {
        println!("{}", SIX_WAYS);
        return;
    }
    let steps = parse(STEP_TEXT);
    let first = parse(FIRST_TEXT);
    let k = steps.len();
    // x^(n - 7) reduced by the recurrence gives the count as a mix of the
    // first k counts
    let mut power = vec![0i64; k];
    let mut base = vec![0i64; k];
    power[0] = 1;
    base[1] = 1;
    let mut e = n - FIRST_SECTORS;
    while e > 0 {
        if e & 1 == 1 {
            power = times(&power, &base, &steps);
        }
        base = times(&base, &base, &steps);
        e >>= 1;
    }
    let answer = (0..k).fold(0, |acc, i| (acc + power[i] * first[i]) % MOD);
    println!("{}", answer);
}
