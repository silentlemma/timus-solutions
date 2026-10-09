use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let n: i64 = it.next().unwrap().parse().unwrap();
    let k = it.next().unwrap().len() as i64;
    // multiply n, n - k, ... while the factor stays positive
    let mut product: i64 = 1;
    let mut factor = n;
    while factor > 0 {
        product *= factor;
        factor -= k;
    }
    println!("{}", product);
}
