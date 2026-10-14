use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let n: usize = it.next().unwrap().parse().unwrap();
    let p = it.next().unwrap().as_bytes();
    let q = it.next().unwrap().as_bytes();
    let zeros = |count: usize| "0".repeat(count);
    let text = |s: &[u8]| String::from_utf8_lossy(s).into_owned();
    // A xor B equals A + B exactly when no position holds two ones. With a
    // equal to p, b follows q up to a 0 that becomes 1, then zeros, and that
    // prefix of q must avoid the ones of p, so it ends before the first clash
    let clash = (0..n).find(|&i| p[i] == b'1' && q[i] == b'1').unwrap_or(n);
    if let Some(j) = (0..clash).rev().find(|&j| p[j] == b'0' && q[j] == b'0') {
        println!("{}\n{}1{}", text(p), text(&q[..j]), zeros(n - j - 1));
        return;
    }
    // otherwise the next a after p with b all zeros, or start over
    let a = match p.iter().rposition(|&c| c == b'0') {
        Some(last) => format!("{}1{}", text(&p[..last]), zeros(n - last - 1)),
        None => zeros(n),
    };
    println!("{}\n{}", a, zeros(n));
}
