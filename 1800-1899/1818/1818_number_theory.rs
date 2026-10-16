use std::io::{self, Read, Write};

// non-negative big numbers in base 10^9, least significant limb first
const BASE: u64 = 1_000_000_000;

fn trim(x: &mut Vec<u64>) {
    while x.last() == Some(&0) {
        x.pop();
    }
}

// x += y * s
fn add_mul(x: &mut Vec<u64>, y: &[u64], s: u64) {
    if x.len() < y.len() {
        x.resize(y.len(), 0);
    }
    let mut carry = 0;
    for i in 0..x.len() {
        let cur = x[i] + carry + if i < y.len() { y[i] * s } else { 0 };
        x[i] = cur % BASE;
        carry = cur / BASE;
    }
    while carry > 0 {
        x.push(carry % BASE);
        carry /= BASE;
    }
    trim(x);
}

fn mul_small(x: &mut Vec<u64>, m: u64) {
    let mut carry = 0;
    for limb in x.iter_mut() {
        let cur = *limb * m + carry;
        *limb = cur % BASE;
        carry = cur / BASE;
    }
    while carry > 0 {
        x.push(carry % BASE);
        carry /= BASE;
    }
    trim(x);
}

fn mod_small(x: &[u64], m: u64) -> u64 {
    x.iter().rev().fold(0, |r, &limb| (r * BASE + limb) % m)
}

// x -= s for s not above x
fn sub_small(x: &mut Vec<u64>, mut s: u64) {
    let mut i = 0;
    while s > 0 {
        let take = s % BASE;
        s /= BASE;
        if x[i] >= take {
            x[i] -= take;
        } else {
            x[i] += BASE - take;
            s += 1;
        }
        i += 1;
    }
    trim(x);
}

fn div_small(x: &mut Vec<u64>, m: u64) {
    let mut r = 0;
    for limb in x.iter_mut().rev() {
        let cur = r * BASE + *limb;
        *limb = cur / m;
        r = cur % m;
    }
    trim(x);
}

fn render(x: &[u64]) -> String {
    match x.split_last() {
        None => "0".to_string(),
        Some((top, rest)) => {
            let mut out = top.to_string();
            for limb in rest.iter().rev() {
                out.push_str(&format!("{:09}", limb));
            }
            out
        }
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace().map(|t| t.parse::<u64>().unwrap());
    let n = match it.next() {
        Some(v) => v,
        None => return,
    };
    let thrown: Vec<u64> = it.take(n as usize).collect();
    // build the catch X digit by digit in base n. Adding s n^j to X keeps
    // the first j fishermen happy and adds s (n - 1)^j to what fisherman
    // j + 1 finds, which is s (-1)^j modulo n: that fixes s
    let (mut caught, mut found) = (Vec::new(), Vec::new());
    let (mut power_n, mut power_m) = (vec![1u64], vec![1u64]);
    for (j, &a) in thrown.iter().enumerate() {
        let mut s = (a + n - mod_small(&found, n)) % n;
        if j % 2 == 1 {
            s = (n - s) % n;
        }
        add_mul(&mut caught, &power_n, s);
        add_mul(&mut found, &power_m, s);
        // the fisherman throws a fishes away and leaves (n - 1)/n of the rest
        sub_small(&mut found, a);
        div_small(&mut found, n);
        mul_small(&mut found, n - 1);
        mul_small(&mut power_n, n);
        mul_small(&mut power_m, n - 1);
    }
    // every catch of this residue modulo n^n works; at least one fish
    let answer = if caught.is_empty() { &power_n } else { &caught };
    writeln!(io::stdout(), "{}", render(answer)).unwrap();
}
