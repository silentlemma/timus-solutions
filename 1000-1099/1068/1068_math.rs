use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let n: i64 = input.trim().parse().unwrap();
    // the numbers between 1 and N form one interval whichever side N is on,
    // and its sum is the count times the average of the ends
    let count = (n - 1).abs() + 1;
    println!("{}", (1 + n) * count / 2);
}
