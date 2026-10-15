use std::io::{self, Read};

// the sum of |a_i - a_j| over all pairs: in sorted order the i-th value
// is larger than the i values before it
fn pair_sum(a: &mut [i64]) -> i64 {
    a.sort_unstable();
    let (mut total, mut before) = (0i64, 0i64);
    for (i, &v) in a.iter().enumerate() {
        total += v * i as i64 - before;
        before += v;
    }
    total
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace().map(|w| w.parse::<i64>().unwrap());
    let n = it.next().unwrap();
    let mut x = Vec::with_capacity(n as usize);
    let mut y = Vec::with_capacity(n as usize);
    for _ in 0..n {
        x.push(it.next().unwrap());
        y.push(it.next().unwrap());
    }
    // walking along the streets, a visit covers |dx| + |dy|
    let pairs = n * (n - 1) / 2;
    println!("{}", (pair_sum(&mut x) + pair_sum(&mut y)) / pairs);
}
