use std::collections::hash_map::RandomState;
use std::hash::{BuildHasher, Hasher};
use std::io::{self, Read};

// independence is tested modulo a prime drawn at random from [2^30, 2^31): a set
// independent modulo a prime is independent over the rationals, and an input can
// beat a fixed prime that divides one of its minors, but not a random one
const LOW: i64 = 1 << 30;
const HIGH: i64 = 1 << 31;

fn is_prime(x: i64) -> bool {
    let mut d = 2;
    while d * d <= x {
        if x % d == 0 {
            return false;
        }
        d += 1;
    }
    true
}

// the standard library seeds every RandomState with fresh random keys
fn random_prime() -> i64 {
    let state = RandomState::new();
    let mut salt = 0;
    loop {
        let mut hasher = state.build_hasher();
        hasher.write_u64(salt);
        salt += 1;
        let x = LOW + (hasher.finish() % (HIGH - LOW) as u64) as i64;
        if is_prime(x) {
            return x;
        }
    }
}

fn power(mut b: i64, mut e: i64, p: i64) -> i64 {
    let mut r = 1;
    b %= p;
    while e > 0 {
        if e % 2 == 1 {
            r = r * b % p;
        }
        b = b * b % p;
        e /= 2;
    }
    r
}

fn main() {
    let p = random_prime();
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<i64>().unwrap());
    let m = it.next().unwrap() as usize;
    let n = it.next().unwrap() as usize;
    let vec: Vec<Vec<i64>> = (0..m)
        .map(|_| (0..n).map(|_| it.next().unwrap().rem_euclid(p)).collect())
        .collect();
    let cost: Vec<i64> = (0..m).map(|_| it.next().unwrap()).collect();
    // the greedy algorithm of a matroid: the cheapest vectors first, and among
    // equal prices the smaller numbers first, which gives the smallest list too
    let mut order: Vec<usize> = (0..m).collect();
    order.sort_by_key(|&i| (cost[i], i));
    // rows of the basis, each with a pivot coordinate equal to 1 and zero in
    // the pivots of the rows before it
    let mut rows: Vec<(usize, Vec<i64>)> = Vec::new();
    let mut chosen: Vec<usize> = Vec::new();
    for &i in &order {
        if chosen.len() == n {
            break;
        }
        let mut v = vec[i].clone();
        for (piv, row) in &rows {
            let f = v[*piv];
            if f == 0 {
                continue;
            }
            for k in 0..n {
                v[k] = (v[k] - f * row[k]).rem_euclid(p);
            }
        }
        let piv = match v.iter().position(|&x| x != 0) {
            Some(k) => k,
            None => continue,
        };
        let inv = power(v[piv], p - 2, p);
        for x in v.iter_mut() {
            *x = *x * inv % p;
        }
        rows.push((piv, v));
        chosen.push(i);
    }
    if chosen.len() < n {
        println!("0");
        return;
    }
    let total: i64 = chosen.iter().map(|&i| cost[i]).sum();
    chosen.sort();
    let mut out = total.to_string();
    for i in chosen {
        out.push_str(&format!("\n{}", i + 1));
    }
    println!("{}", out);
}
