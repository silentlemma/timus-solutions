use std::io::{self, Read};

// linear independence is tested modulo a large prime: exact, and a set that is
// independent modulo the prime is independent over the rationals
const P: i64 = 2147483647;

fn power(mut b: i64, mut e: i64) -> i64 {
    let mut r = 1;
    b %= P;
    while e > 0 {
        if e % 2 == 1 {
            r = r * b % P;
        }
        b = b * b % P;
        e /= 2;
    }
    r
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<i64>().unwrap());
    let m = it.next().unwrap() as usize;
    let n = it.next().unwrap() as usize;
    let vec: Vec<Vec<i64>> = (0..m)
        .map(|_| (0..n).map(|_| it.next().unwrap().rem_euclid(P)).collect())
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
                v[k] = (v[k] - f * row[k]).rem_euclid(P);
            }
        }
        let piv = match v.iter().position(|&x| x != 0) {
            Some(k) => k,
            None => continue,
        };
        let inv = power(v[piv], P - 2);
        for x in v.iter_mut() {
            *x = *x * inv % P;
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
