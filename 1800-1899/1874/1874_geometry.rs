use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<f64> = input.split_ascii_whitespace().map(|t| t.parse().unwrap()).collect();
    let (a, b) = (v[0], v[1]);
    // the right triangle on the birch and the ground holds at most a quarter
    // of the squared diagonal; with the triangle of the sticks added, the
    // total is largest when the sticks meet at 135 degrees
    let (x, y) = (a / 2.0, b / 2.0);
    println!("{:.9}", x * x + y * y + 2.0 * 2f64.sqrt() * x * y);
}
