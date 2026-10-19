use std::io::{self, Read};
const WORD_BITS: usize = 64;
type Matrix = Vec<Vec<u64>>;
fn matrix(n: usize, m: usize) -> Matrix {
    vec![vec![0; (m + WORD_BITS - 1) / WORD_BITS]; n]
}
fn maximum_matching(rows: &Matrix, m: usize) -> (Vec<isize>, Vec<isize>) {
    let n = rows.len();
    let words = (m + WORD_BITS - 1) / WORD_BITS;
    let (mut left, mut right) = (vec![-1isize; n], vec![-1isize; m]);
    let mut free = vec![u64::MAX; words];
    let mut remaining = m;
    if m % WORD_BITS != 0 {
        free[words - 1] = (1u64 << (m % WORD_BITS)) - 1;
    }
    for start in 0..n {
        if remaining == 0 {
            break;
        }
        let mut direct = None;
        for w in 0..words {
            let mask = rows[start][w] & free[w];
            if mask != 0 {
                direct = Some(w * WORD_BITS + mask.trailing_zeros() as usize);
                break;
            }
        }
        if let Some(v) = direct {
            left[start] = v as isize;
            right[v] = start as isize;
            free[v / WORD_BITS] &= !(1u64 << (v % WORD_BITS));
            remaining -= 1;
            continue;
        }
        let mut queue = vec![start];
        let mut parent = vec![0usize; m];
        let mut seen = vec![0u64; words];
        let mut finish = -1isize;
        let mut at = 0;
        while at < queue.len() && finish < 0 {
            let u = queue[at];
            at += 1;
            for w in 0..words {
                if finish >= 0 {
                    break;
                }
                let mut mask = rows[u][w] & !seen[w];
                while mask != 0 {
                    let offset = mask.trailing_zeros() as usize;
                    let bit = 1u64 << offset;
                    mask &= mask - 1;
                    seen[w] |= bit;
                    let v = w * WORD_BITS + offset;
                    parent[v] = u;
                    if right[v] < 0 {
                        finish = v as isize;
                        break;
                    }
                    queue.push(right[v] as usize);
                }
            }
        }
        if finish >= 0 {
            let v = finish as usize;
            free[v / WORD_BITS] &= !(1u64 << (v % WORD_BITS));
            remaining -= 1;
            while finish >= 0 {
                let v = finish as usize;
                let u = parent[v];
                let old = left[u];
                left[u] = finish;
                right[v] = u as isize;
                finish = old;
            }
        }
    }
    (left, right)
}
fn reach(rows: &Matrix, opposite: &[isize], own_match: &[isize]) -> (Vec<bool>, Vec<bool>) {
    let (mut own, mut other) = (vec![false; rows.len()], vec![false; opposite.len()]);
    let mut queue = Vec::new();
    for (u, &matched) in own_match.iter().enumerate() {
        if matched < 0 {
            own[u] = true;
            queue.push(u);
        }
    }
    let words = (opposite.len() + WORD_BITS - 1) / WORD_BITS;
    let mut seen = vec![0u64; words];
    let mut at = 0;
    while at < queue.len() {
        let u = queue[at];
        at += 1;
        for w in 0..words {
            let mut mask = rows[u][w] & !seen[w];
            while mask != 0 {
                let offset = mask.trailing_zeros() as usize;
                let bit = 1u64 << offset;
                mask &= mask - 1;
                seen[w] |= bit;
                let v = w * WORD_BITS + offset;
                let partner = opposite[v];
                other[v] = true;
                if partner >= 0 && !own[partner as usize] {
                    own[partner as usize] = true;
                    queue.push(partner as usize);
                }
            }
        }
    }
    (own, other)
}
fn solve(rows: &Matrix, reverse: &Matrix) -> (String, String) {
    let (left, right) = maximum_matching(rows, reverse.len());
    let (never_left, always_right) = reach(rows, &right, &left);
    let (never_right, always_left) = reach(reverse, &left, &right);
    let a = (0..rows.len())
        .map(|u| {
            if never_left[u] {
                'N'
            } else if always_left[u] {
                'A'
            } else {
                'E'
            }
        })
        .collect();
    let b = (0..reverse.len())
        .map(|v| {
            if never_right[v] {
                'N'
            } else if always_right[v] {
                'A'
            } else {
                'E'
            }
        })
        .collect();
    (a, b)
}
fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input
        .split_whitespace()
        .map(|v| v.parse::<usize>().unwrap());
    let (n, m, k) = (
        words.next().unwrap(),
        words.next().unwrap(),
        words.next().unwrap(),
    );
    let (mut rows, mut reverse) = (matrix(n, m), matrix(m, n));
    for _ in 0..k {
        let (u, v) = (words.next().unwrap() - 1, words.next().unwrap() - 1);
        rows[u][v / WORD_BITS] |= 1u64 << (v % WORD_BITS);
        reverse[v][u / WORD_BITS] |= 1u64 << (u % WORD_BITS);
    }
    let (a, b) = solve(&rows, &reverse);
    println!("{}\n{}", a, b);
}
