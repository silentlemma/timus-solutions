use std::fmt::Write as _;
use std::io::{self, Read, Write};

const MOST: usize = 4; // the highest K asked for

fn power(mut b: i64, mut e: i64, modulus: i64) -> i64 {
    let mut r = 1;
    b %= modulus;
    while e > 0 {
        if e & 1 == 1 {
            r = r * b % modulus;
        }
        b = b * b % modulus;
        e >>= 1;
    }
    r
}

fn number(words: &mut std::str::SplitAsciiWhitespace) -> i64 {
    words.next().unwrap().parse().unwrap()
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut words = text.split_ascii_whitespace();
    let (n, m) = (number(&mut words) as usize, number(&mut words) as usize);
    let modulus = number(&mut words);
    let mut values = vec![0i64; n + 1];
    // trees[j] is a Fenwick tree of the power sums of a^j for j = 1..4; the
    // sums stay unreduced and are only reduced when a query reads them
    let mut trees = vec![vec![0i64; n + 1]; MOST + 1];
    for i in 1..=n {
        values[i] = number(&mut words).rem_euclid(modulus);
        let mut p = 1;
        for tree in trees.iter_mut().skip(1) {
            p = p * values[i] % modulus;
            tree[i] += p;
        }
    }
    for tree in trees.iter_mut().skip(1) {
        for i in 1..=n {
            let up = i + (i & i.wrapping_neg());
            if up <= n {
                tree[up] += tree[i];
            }
        }
    }
    let inverse: Vec<i64> = (0..=MOST as i64)
        .map(|k| power(k, modulus - 2, modulus))
        .collect();
    let mut out = String::new();
    for _ in 0..m {
        if words.next().unwrap() == "I" {
            let (i, delta) = (number(&mut words) as usize, number(&mut words));
            let old = values[i];
            let now = (old + delta).rem_euclid(modulus);
            values[i] = now;
            let (mut po, mut pn) = (1, 1);
            for tree in trees.iter_mut().skip(1) {
                po = po * old % modulus;
                pn = pn * now % modulus;
                let mut k = i;
                while k <= n {
                    tree[k] += pn - po;
                    k += k & k.wrapping_neg();
                }
            }
            continue;
        }
        let left = number(&mut words) as usize;
        let right = number(&mut words) as usize;
        let top = number(&mut words) as usize;
        let mut sums = [0i64; MOST + 1];
        for j in 1..=top {
            let mut total = 0i64;
            let mut k = right;
            while k > 0 {
                total += trees[j][k];
                k -= k & k.wrapping_neg();
            }
            k = left - 1;
            while k > 0 {
                total -= trees[j][k];
                k -= k & k.wrapping_neg();
            }
            sums[j] = total.rem_euclid(modulus);
        }
        // Newton's identities: k e(k) is the alternating sum of e(k - i) p(i)
        let mut e = [0i64; MOST + 1];
        e[0] = 1;
        for k in 1..=top {
            let mut acc = 0i64;
            for i in 1..=k {
                let term = e[k - i] * sums[i] % modulus;
                acc += if i % 2 == 1 { term } else { modulus - term };
            }
            e[k] = acc % modulus * inverse[k] % modulus;
        }
        let line: Vec<String> = e[..=top].iter().map(|v| v.to_string()).collect();
        writeln!(out, "{}", line.join(" ")).unwrap();
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}
