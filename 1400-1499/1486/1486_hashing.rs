use std::io::{self, Read};

// two hashes modulo two primes, packed into one 64-bit key
const MOD1: u64 = 1_000_000_007;
const MOD2: u64 = 998_244_353;
const ROW1: u64 = 131;
const ROW2: u64 = 137;
const COL1: u64 = 1009;
const COL2: u64 = 1013;
const HALF: u32 = 32;
const LOW: u64 = (1 << HALF) - 1;

fn power(b: u64, e: usize, modulus: u64) -> u64 {
    (0..e).fold(1, |r, _| r * b % modulus)
}

/// Two different equal k x k squares as top-left corners.
fn find(grid: &[&[u8]], k: usize) -> Option<[(usize, usize); 2]> {
    let (n, m) = (grid.len(), grid[0].len());
    let width = m - k + 1;
    let mut rows = vec![vec![0u64; width]; n];
    let (p1, p2) = (power(ROW1, k, MOD1), power(ROW2, k, MOD2));
    for i in 0..n {
        let (mut h1, mut h2) = (0u64, 0u64);
        for j in 0..m {
            let c = grid[i][j] as u64;
            h1 = (h1 * ROW1 + c) % MOD1;
            h2 = (h2 * ROW2 + c) % MOD2;
            if j >= k {
                let old = grid[i][j - k] as u64;
                h1 = (h1 + MOD1 - old * p1 % MOD1) % MOD1;
                h2 = (h2 + MOD2 - old * p2 % MOD2) % MOD2;
            }
            if j + 1 >= k {
                rows[i][j + 1 - k] = h1 << HALF | h2;
            }
        }
    }
    let (p1, p2) = (power(COL1, k, MOD1), power(COL2, k, MOD2));
    let (mut c1, mut c2) = (vec![0u64; width], vec![0u64; width]);
    let mut keys: Vec<(u64, usize)> = Vec::with_capacity((n - k + 1) * width);
    for i in 0..n {
        for j in 0..width {
            c1[j] = (c1[j] * COL1 + (rows[i][j] >> HALF)) % MOD1;
            c2[j] = (c2[j] * COL2 + (rows[i][j] & LOW)) % MOD2;
            if i >= k {
                c1[j] = (c1[j] + MOD1 - (rows[i - k][j] >> HALF) * p1 % MOD1) % MOD1;
                c2[j] = (c2[j] + MOD2 - (rows[i - k][j] & LOW) * p2 % MOD2) % MOD2;
            }
            if i + 1 >= k {
                keys.push((c1[j] << HALF | c2[j], (i + 1 - k) * width + j));
            }
        }
    }
    keys.sort_unstable();
    for w in keys.windows(2) {
        if w[0].0 == w[1].0 {
            let (a, b) = (w[0].1, w[1].1);
            let (r1, s1, r2, s2) = (a / width, a % width, b / width, b % width);
            if (0..k).all(|t| grid[r1 + t][s1..s1 + k] == grid[r2 + t][s2..s2 + k]) {
                return Some([(r1, s1), (r2, s2)]);
            }
        }
    }
    None
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let n: usize = it.next().unwrap().parse().unwrap();
    let m: usize = it.next().unwrap().parse().unwrap();
    let grid: Vec<&[u8]> = (0..n).map(|_| it.next().unwrap().as_bytes()).collect();
    // equal k x k squares contain equal (k - 1) x (k - 1) ones, so the
    // largest size can be found by binary search
    let (mut lo, mut hi) = (1, n.min(m));
    let mut best: Option<(usize, [(usize, usize); 2])> = None;
    while lo <= hi {
        let k = (lo + hi) / 2;
        match find(&grid, k) {
            Some(corners) => {
                best = Some((k, corners));
                lo = k + 1;
            }
            None => hi = k - 1,
        }
    }
    match best {
        None => println!("0"),
        Some((k, [(r1, c1), (r2, c2)])) => {
            println!("{}\n{} {}\n{} {}", k, r1 + 1, c1 + 1, r2 + 1, c2 + 1)
        }
    }
}
