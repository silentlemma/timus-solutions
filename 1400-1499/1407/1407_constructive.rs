use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let n: u32 = input.trim().parse().unwrap();
    // a number of k digits 1 and 2 divisible by 2^k: put 1 or 2 in front of the
    // one for k - 1, whichever keeps one more factor 2; only the lowest n + 1
    // bits matter, so the sums may wrap around in 128 bits
    let (mut value, mut power) = (0u128, 1u128);
    let mut digits = Vec::new();
    for k in 0..n {
        let mask = (2u128 << k) - 1;
        let d: u128 = if value.wrapping_add(power) & mask == 0 {
            1
        } else {
            2
        };
        value = value.wrapping_add(d.wrapping_mul(power));
        digits.push(b'0' + d as u8);
        power = power.wrapping_mul(10);
    }
    digits.reverse();
    println!("{}", String::from_utf8(digits).unwrap());
}
