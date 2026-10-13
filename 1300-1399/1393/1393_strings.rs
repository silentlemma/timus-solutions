use std::io::{self, Read};

const ALPHABET: usize = 256;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let n: usize = it.next().unwrap().parse().unwrap();
    let text = &it.next().unwrap().as_bytes()[..n];
    // the shortest period p of the cyclic string: T is u repeated n / p times
    let mut pi = vec![0u32; n];
    for i in 1..n {
        let mut k = pi[i - 1] as usize;
        while k > 0 && text[i] != text[k] {
            k = pi[k - 1] as usize;
        }
        if text[i] == text[k] {
            k += 1;
        }
        pi[i] = k as u32;
    }
    let mut p = n - pi[n - 1] as usize;
    if n % p != 0 {
        p = n;
    }
    drop(pi);
    // sort the rotations of u by doubling, all of them distinct
    let mut order = vec![0u32; p];
    let mut cls = vec![0u32; p];
    let mut tmp = vec![0u32; p];
    let mut tmp_cls = vec![0u32; p];
    let mut cnt = vec![0u32; p.max(ALPHABET)];
    for &c in &text[..p] {
        cnt[c as usize] += 1;
    }
    for i in 1..ALPHABET {
        cnt[i] += cnt[i - 1];
    }
    for i in (0..p).rev() {
        let c = text[i] as usize;
        cnt[c] -= 1;
        order[cnt[c] as usize] = i as u32;
    }
    let mut classes = 1;
    for i in 1..p {
        if text[order[i] as usize] != text[order[i - 1] as usize] {
            classes += 1;
        }
        cls[order[i] as usize] = classes as u32 - 1;
    }
    let mut length = 1;
    while length < p && classes < p {
        // sorted by the second half already: shift each start back by length
        for i in 0..p {
            tmp[i] = ((order[i] as usize + p - length) % p) as u32;
        }
        cnt[..classes].fill(0);
        for &t in &tmp {
            cnt[cls[t as usize] as usize] += 1;
        }
        for i in 1..classes {
            cnt[i] += cnt[i - 1];
        }
        for &t in tmp.iter().rev() {
            let c = cls[t as usize] as usize;
            cnt[c] -= 1;
            order[cnt[c] as usize] = t;
        }
        tmp_cls[order[0] as usize] = 0;
        classes = 1;
        for i in 1..p {
            let (a, b) = (order[i] as usize, order[i - 1] as usize);
            if cls[a] != cls[b] || cls[(a + length) % p] != cls[(b + length) % p] {
                classes += 1;
            }
            tmp_cls[a] = classes as u32 - 1;
        }
        std::mem::swap(&mut cls, &mut tmp_cls);
        length *= 2;
    }
    // Kasai: the common prefix with the previous rotation drops by at most one per step
    let mut total: u64 = 0;
    let mut h = 0usize;
    for i in 0..p {
        if cls[i] == 0 {
            h = 0;
            continue;
        }
        let j = order[cls[i] as usize - 1] as usize;
        while h < p && text[(i + h) % p] == text[(j + h) % p] {
            h += 1;
        }
        total += h as u64;
        h = h.saturating_sub(1);
    }
    // each rotation of u appears n / p times in a row, with common prefixes of n
    total += (p * (n / p - 1) * n) as u64;
    println!("{:.3}", total as f64 / (n - 1) as f64);
}
