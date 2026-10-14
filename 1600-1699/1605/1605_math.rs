use std::io::{self, Read};

fn main() {
    let mut s = String::new();
    io::stdin().read_to_string(&mut s).unwrap();
    let n: i64 = match s.trim().parse() {
        Ok(v) => v,
        Err(_) => return,
    };
    // x_n = 2/3 - (-1)^n (2/3) 2^-n: an even n leaves k sixes while
    // 10^k <= 2^n, an odd n while 2 10^k < 2^n, that is 10^k <= 2^(n-1)
    let m = if n % 2 == 0 { n } else { n - 1 };
    println!("{}", (m as f64 * 2f64.log10()).floor() as i64);
}
