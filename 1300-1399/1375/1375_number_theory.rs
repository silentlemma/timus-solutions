use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<i64>().unwrap());
    let (k, p) = (it.next().unwrap(), it.next().unwrap());
    // root[v]: some y with y^2 = v (mod p), or -1 when v is not a square
    let mut root = vec![-1i64; p as usize];
    for y in 0..p {
        let v = (y * y % p) as usize;
        if root[v] < 0 {
            root[v] = y;
        }
    }
    // half the values are squares, so some x soon leaves a square k - x^2
    for x in 0..p {
        let y = root[((k - x * x) % p + p) as usize % p as usize];
        if y >= 0 {
            println!("{} {}", x, y);
            return;
        }
    }
    println!("NO SOLUTION");
}
