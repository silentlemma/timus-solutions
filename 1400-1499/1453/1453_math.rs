use std::io::{self, Read};

const BASE: u64 = 1_000_000_000; // a long number in decimal limbs of nine digits

/// number = number * factor + add, on limbs from the lowest.
fn mul_add(number: &mut Vec<u64>, factor: u64, add: u64) {
    let mut carry = add;
    for limb in number.iter_mut() {
        let v = *limb * factor + carry;
        *limb = v % BASE;
        carry = v / BASE;
    }
    while carry > 0 {
        number.push(carry % BASE);
        carry /= BASE;
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<usize> = input
        .split_ascii_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();
    let (n, s) = (v[0], v[1]);
    let c = &v[2..2 + n];
    let rook = (n * (s - 1)) as u64;
    if n == 1 {
        // in one dimension a bishop moves exactly like a rook
        println!("{}", rook);
        return;
    }
    // t bishop steps need room t on the chosen side of every coordinate
    let mut both = vec![0usize; s]; // both[m]: coordinates with room m on each side
    let mut reach = s; // beyond this some coordinate has no room
    for &x in c {
        both[(s - x).min(x - 1)] += 1;
        reach = reach.min((s - x).max(x - 1));
    }
    let mut count = vec![0u64; n + 1]; // count[k]: lengths t with 2^k directions
    let mut k = n - both[0];
    for t in 1..=reach {
        count[k] += 1;
        k -= both[t];
    }
    let mut ways = vec![0u64]; // the sum of count[k] 2^k, doubling from the top
    for j in (0..=n).rev() {
        mul_add(&mut ways, 2, count[j]);
    }
    mul_add(&mut ways, 1, rook);
    let mut text = ways.last().unwrap().to_string();
    for limb in ways.iter().rev().skip(1) {
        text.push_str(&format!("{:09}", limb));
    }
    println!("{}", text);
}
