use std::io::{self, Read};

fn main() {
    let mut data = Vec::new();
    io::stdin().read_to_end(&mut data).unwrap();
    // characters from 33 to 255 may come, so split on bytes up to the space
    let mut words = data.split(|&c| c <= b' ').filter(|w| !w.is_empty());
    let n: usize = std::str::from_utf8(words.next().unwrap())
        .unwrap()
        .parse()
        .unwrap();
    let s = words.next().unwrap();
    let t = words.next().unwrap();
    // t is s turned left by k, that is right by n - k: find it in s + s with KMP
    let mut fail = vec![0usize; n];
    let mut k = 0;
    for i in 1..n {
        while k > 0 && t[i] != t[k] {
            k = fail[k - 1];
        }
        if t[i] == t[k] {
            k += 1;
        }
        fail[i] = k;
    }
    k = 0;
    for i in 0..2 * n - 1 {
        let c = s[i % n];
        while k > 0 && c != t[k] {
            k = fail[k - 1];
        }
        if c == t[k] {
            k += 1;
        }
        if k == n {
            let start = i + 1 - n;
            println!("{}", (n - start) % n);
            return;
        }
    }
    println!("-1");
}
