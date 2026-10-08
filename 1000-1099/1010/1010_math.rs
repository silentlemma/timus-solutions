use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_ascii_whitespace();
    let n: usize = tokens.next().unwrap().parse().unwrap();
    let f: Vec<i64> = tokens.take(n).map(|t| t.parse().unwrap()).collect();
    // the slope of a chord is the mean of the slopes of the steps under it, so
    // the steepest valid chord joins two neighbours; take the first steepest
    let mut a = 0;
    for i in 1..n - 1 {
        if (f[i + 1] - f[i]).abs() > (f[a + 1] - f[a]).abs() {
            a = i;
        }
    }
    println!("{} {}", a + 1, a + 2);
}
