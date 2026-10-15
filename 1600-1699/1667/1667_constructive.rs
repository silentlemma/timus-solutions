use std::collections::{HashMap, HashSet};
use std::io::{self, Read};

const ROOT_LIMIT: i64 = 316227766; // the largest integer whose square is at most 10^17
const LEGS: i64 = 40; // Pythagorean pairs from m^2 - n^2 and 2mn with n < m < LEGS

const STARTS: i64 = 30; // first terms of the arithmetic sequences
const STEPS: i64 = 6; // their differences
const OFFSETS: usize = 30; // where the runs of consecutive primes start
const PRIMES: usize = 80;
const HALF: u32 = 32; // a reduced fraction x / y is stored as x << HALF | y

struct List {
    nums: Vec<i64>,
    ratios: Vec<i64>, // sorted reduced fractions x / y < 1
    top: i64,
}

fn gcd(a: i64, b: i64) -> i64 {
    if b == 0 {
        a
    } else {
        gcd(b, a % b)
    }
}

/// For u_1..u_k with S = sum of u^2, the numbers 2u_1, ..., 2u_k and S - 1
/// have squares adding up to (S + 1)^2; None if they repeat.
fn from_us(us: &[i64]) -> Option<Vec<i64>> {
    let total: i64 = us.iter().map(|u| u * u).sum();
    let mut nums: Vec<i64> = us.iter().map(|u| 2 * u).collect();
    nums.push(total - 1);
    let seen: HashSet<i64> = nums.iter().copied().collect();
    if seen.len() == nums.len() {
        Some(nums)
    } else {
        None
    }
}

fn make_list(nums: Vec<i64>) -> List {
    let mut ratios = Vec::new();
    for &x in &nums {
        for &y in &nums {
            if x < y {
                let g = gcd(x, y);
                ratios.push((x / g) << HALF | (y / g));
            }
        }
    }
    ratios.sort_unstable();
    let top = *nums.iter().max().unwrap();
    List { nums, ratios, top }
}

/// Lists of distinct positive integers whose squares add up to a square,
/// smallest maximum first.
fn lists(size: usize, primes: &[i64]) -> Vec<List> {
    let mut found: Vec<Option<Vec<i64>>> = Vec::new();
    if size == 1 {
        found.push(Some(vec![1]));
    } else if size == 2 {
        for m in 2..LEGS {
            for n in 1..m {
                if gcd(m, n) == 1 && (m - n) % 2 == 1 {
                    found.push(Some(vec![m * m - n * n, 2 * m * n]));
                }
            }
        }
    } else {
        let k = size - 1;
        for s in 1..STARTS {
            for d in 1..=STEPS {
                let us: Vec<i64> = (0..k as i64).map(|i| s + d * i).collect();
                found.push(from_us(&us));
            }
        }
        for off in 0..OFFSETS {
            found.push(from_us(&primes[off..off + k]));
        }
    }
    let mut out: Vec<List> = found.into_iter().flatten().map(make_list).collect();
    out.sort_by_key(|l| l.top);
    out
}

fn disjoint(x: &[i64], y: &[i64]) -> bool {
    let (mut i, mut j) = (0, 0);
    while i < x.len() && j < y.len() {
        if x[i] == y[j] {
            return false;
        }
        if x[i] < y[j] {
            i += 1;
        } else {
            j += 1;
        }
    }
    true
}

fn main() {
    let mut primes: Vec<i64> = Vec::new();
    let mut n = 2;
    while primes.len() < PRIMES {
        if primes.iter().take_while(|&&p| p * p <= n).all(|&p| n % p != 0) {
            primes.push(n);
        }
        n += 1;
    }
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let v: Vec<usize> = text.split_ascii_whitespace().map(|w| w.parse().unwrap()).collect();
    let mut pool: HashMap<usize, Vec<List>> = HashMap::new();
    let mut out = String::new();
    for k in 0..v[0] {
        let (rows, cols) = (v[1 + 2 * k], v[2 + 2 * k]);
        for size in [rows, cols] {
            pool.entry(size).or_insert_with(|| lists(size, &primes));
        }
        // entry (i, j) is (a_i b_j)^2; two products a_i b_j and a_k b_l are
        // equal exactly when a_i / a_k = b_l / b_j, so no ratio may be shared
        let smallest = pool[&cols][0].top;
        let mut chosen: Option<(&List, &List)> = None;
        for a in &pool[&rows] {
            if a.top * smallest > ROOT_LIMIT || chosen.is_some() {
                break;
            }
            for b in &pool[&cols] {
                if a.top * b.top > ROOT_LIMIT {
                    break;
                }
                if disjoint(&a.ratios, &b.ratios) {
                    chosen = Some((a, b));
                    break;
                }
            }
        }
        if k > 0 {
            out.push('\n');
        }
        match chosen {
            None => out.push_str("-1\n"),
            Some((a, b)) => {
                for &x in &a.nums {
                    let row: Vec<String> =
                        b.nums.iter().map(|&y| (x * y * x * y).to_string()).collect();
                    out.push_str(&row.join(" "));
                    out.push('\n');
                }
            }
        }
    }
    print!("{}", out);
}
