use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<f64> = input.split_ascii_whitespace().map(|w| w.parse().unwrap()).collect();
    let (rim, book) = (v[0], v[1]);
    // with the foot at distance x from the rim and r = hypot(x, rim), the book
    // leans on the rim top and its middle lies x * (book / 2r - 1) to the left,
    // which is largest where r cubed is book * rim * rim / 2
    let r = (book * rim * rim / 2.0).cbrt();
    let mut shift = 0.0;
    if r > rim {
        let x = (r * r - rim * rim).sqrt();
        shift = x * (book / (2.0 * r) - 1.0);
    }
    println!("{:.6}", shift);
}
