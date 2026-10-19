use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let n: usize = match input.trim().parse() {
        Ok(v) => v,
        Err(_) => return,
    };
    // m, the least number not dividing n, divides no proper divisor either,
    // so colouring by x mod m separates every two artists d apart; m <= 13
    // since lcm(1, ..., 13) exceeds 300000
    let m = (2..).find(|m| n % m != 0).unwrap();
    let p = (2..).find(|p| n % p == 0).unwrap();
    // the wrap-around neighbours are n - d apart, at least n - n/p; the
    // last n/p artists get a second palette, so no gap inside either part
    // is that long and the parts never share a colour
    let front = n - n / p;
    let out: String =
        (0..n).map(|x| (b'a' + (x % m + if x >= front { m } else { 0 }) as u8) as char).collect();
    println!("{}", out);
}
