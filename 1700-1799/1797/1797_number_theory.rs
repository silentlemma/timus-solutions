use std::io::{self, Read};

fn gcd(a: u128, b: u128) -> u128 {
    if b == 0 {
        a
    } else {
        gcd(b, a % b)
    }
}

// the sum of (a * i + b) / m over i = 0 .. n - 1
fn floor_sum(mut n: u128, mut m: u128, mut a: u128, mut b: u128) -> u128 {
    let mut total = 0;
    loop {
        if a >= m {
            total += n * (n - 1) / 2 * (a / m);
            a %= m;
        }
        if b >= m {
            total += n * (b / m);
            b %= m;
        }
        let top = a * n + b;
        if top < m {
            return total;
        }
        n = top / m;
        b = top % m;
        std::mem::swap(&mut m, &mut a);
    }
}

// how many numbers from 1 to limit are a * x + b * y with a, b >= 0
fn count_up_to(limit: u128, x: u128, y: u128) -> u128 {
    let g = gcd(x, y);
    let (limit, x, y) = (limit / g, x / g, y / g);
    // with x and y coprime every such number has exactly one form with
    // b < x; for each b the values of a run from 0 to (limit - b*y) / x
    let last = (limit / y).min(x - 1);
    let forms = floor_sum(last + 1, x, y, limit - y * last) + last + 1;
    forms - 1 // zero is not a volume size
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace().map(|v| v.parse::<u128>().unwrap());
    let tests = it.next().unwrap();
    let mut out = String::new();
    for _ in 0..tests {
        let mut next = || it.next().unwrap();
        let (x, y, l, r) = (next(), next(), next(), next());
        let answer = count_up_to(r, x, y) - count_up_to(l - 1, x, y);
        out.push_str(&format!("{}\n", answer));
    }
    print!("{}", out);
}
