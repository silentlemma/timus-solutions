use std::io;

fn main() {
    let mut line = String::new();
    io::stdin().read_line(&mut line).unwrap();
    let v: Vec<i64> = line
        .split_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let (n, k) = (v[0], v[1]);
    // every two hobbits shake hands exactly once, when their groups part,
    // except the married couples, who go home together and never part
    println!("{}", n * (n - 1) / 2 - k);
}
