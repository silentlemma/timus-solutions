use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let n: usize = input.trim().parse().unwrap();
    // a[k]: rooted trees with k vertices; s[k]: the sum of d a[d] over divisors d of k
    let mut a = vec![0u128; n + 1];
    let mut s = vec![0u128; n + 1];
    a[1] = 1;
    s[1] = 1;
    for m in 1..n {
        // a(m + 1) = (s(1) a(m) + s(2) a(m - 1) + ... + s(m) a(1)) / m
        let total: u128 = (1..=m).map(|k| s[k] * a[m - k + 1]).sum();
        a[m + 1] = total / m as u128;
        s[m + 1] = (1..=m + 1)
            .filter(|d| (m + 1) % d == 0)
            .map(|d| d as u128 * a[d])
            .sum();
    }
    println!("{}", a[n]);
}
