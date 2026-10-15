use std::io::{self, Read};

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut words = text.split_ascii_whitespace().map(|w| w.parse::<i64>().unwrap());
    let (n, s) = (words.next().unwrap(), words.next().unwrap());
    let yes = s - 2 * n; // YES takes 3 bytes, NO takes 2
    let no = n - yes;
    // the first test fails when its answer is NO, any later one when its
    // answer differs from the one before: no / n + (n - 1) * 2 yes no / (n (n - 1))
    println!("{:.7}", (no * (2 * yes + 1)) as f64 / n as f64);
}
