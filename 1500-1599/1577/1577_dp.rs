use std::io::{self, Read};

const MOD: u64 = 1_000_000_007;

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut words = text.split_ascii_whitespace();
    let a = words.next().unwrap().as_bytes();
    let b = words.next().unwrap().as_bytes();
    let (n, m) = (a.len(), b.len());
    // length[j] and count[j]: the shortest common supersequences of a[i..] and
    // b[j..], their length and number; row i needs only row i + 1
    let mut length: Vec<usize> = (0..=m).map(|j| m - j).collect(); // i = n: only b[j..]
    let mut count = vec![1u64; m + 1];
    let (mut below_len, mut below_cnt) = (vec![0usize; m + 1], vec![0u64; m + 1]);
    for i in (0..n).rev() {
        std::mem::swap(&mut length, &mut below_len);
        std::mem::swap(&mut count, &mut below_cnt);
        length[m] = n - i; // only a[i..] itself
        count[m] = 1;
        for j in (0..m).rev() {
            if a[i] == b[j] {
                // the first letter is the common one and covers both
                length[j] = below_len[j + 1] + 1;
                count[j] = below_cnt[j + 1];
                continue;
            }
            // the first letter is a[i] or b[j]; the two kinds of strings differ
            // in their first letter, so their numbers add up
            let (take_a, take_b) = (below_len[j], length[j + 1]);
            let best = take_a.min(take_b);
            length[j] = best + 1;
            let mut ways = 0;
            if take_a == best {
                ways += below_cnt[j];
            }
            if take_b == best {
                ways += count[j + 1];
            }
            count[j] = ways % MOD;
        }
    }
    println!("{}", count[0]);
}
