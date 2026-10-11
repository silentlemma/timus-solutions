use std::io;

fn main() {
    let mut line = String::new();
    io::stdin().read_line(&mut line).unwrap();
    let v: Vec<i64> = line
        .split_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let (n, m) = (v[0], v[1]);
    // every full lap turns four times and peels two rows and two columns; the
    // spiral ends in the middle of the shorter side, so only that side counts
    println!("{}", if n <= m { 2 * (n - 1) } else { 2 * m - 1 });
}
