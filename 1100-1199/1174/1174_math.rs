use std::io::{self, Read};

const BASE: u64 = 1_000_000_000;

// rank = rank * m + add, on little-endian digits in base 10^9
fn mul_add(rank: &mut Vec<u64>, m: u64, add: u64) {
    let mut carry = add;
    for d in rank.iter_mut() {
        carry += *d * m;
        *d = carry % BASE;
        carry /= BASE;
    }
    while carry > 0 {
        rank.push(carry % BASE);
        carry /= BASE;
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<usize> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let n = v[0];
    let mut place = vec![0; n + 1];
    for (i, &x) in v[1..=n].iter().enumerate() {
        place[x] = i;
    }
    // rank of the order of 1..k among themselves: element k sweeps once
    // across the order of 1..k-1, to the left in even sweeps and to the
    // right in odd ones, and that order's rank counts the sweeps before
    let mut rank = vec![0u64];
    for k in 2..=n {
        let smaller_left = (1..k).filter(|&x| place[x] < place[k]).count();
        let step = if rank[0] % 2 == 1 {
            smaller_left
        } else {
            k - 1 - smaller_left
        };
        mul_add(&mut rank, k as u64, step as u64);
    }
    mul_add(&mut rank, 1, 1);
    let mut out = rank.last().unwrap().to_string();
    for d in rank.iter().rev().skip(1) {
        out += &format!("{:09}", d);
    }
    println!("{}", out);
}
