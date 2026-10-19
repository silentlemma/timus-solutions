use std::io::{self, Read};

// start of the lexicographically greatest suffix (the least one when flip
// is set), by the comparison loop of the Two-Way algorithm
fn suffix_start(w: &[u8], flip: bool) -> usize {
    let n = w.len() as i64;
    let (mut best, mut j, mut k, mut p) = (-1i64, 0i64, 1i64, 1i64);
    while j + k < n {
        let a = w[(j + k) as usize];
        let b = w[(best + k) as usize];
        if a != b && (a < b) != flip {
            j += k;
            k = 1;
            p = j - best;
        } else if a == b {
            if k != p {
                k += 1;
            } else {
                j += p;
                k = 1;
            }
        } else {
            best = j;
            j = best + 1;
            k = 1;
            p = 1;
        }
    }
    (best + 1) as usize
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let w = input.trim().as_bytes();
    let n = w.len();
    // the longest border gives the period of the word
    let mut border = vec![0usize; n];
    let mut k = 0;
    for i in 1..n {
        while k > 0 && w[k] != w[i] {
            k = border[k - 1];
        }
        if w[k] == w[i] {
            k += 1;
        }
        border[i] = k;
    }
    // the critical factorization theorem: the split before the later of the
    // two greatest suffixes has a local root as long as the period (both are
    // the whole word only for a power of one letter)
    let split = suffix_start(w, false).max(suffix_start(w, true)).max(1);
    println!("{} {}", split, n - border[n - 1]);
}
