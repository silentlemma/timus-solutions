use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let n: u128 = input.trim().parse().unwrap();
    // ordered choices of k different drinks: n (n - 1) ... (n - k + 1), for k from 2,
    // the sum for n = 21 needs more than 64 bits
    let (mut total, mut ways) = (0u128, n);
    for k in 2..=n {
        ways *= n - k + 1;
        total += ways;
    }
    println!("{}", total);
}
