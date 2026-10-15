use std::io::{self, Read};

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut n: u64 = text.trim().parse().unwrap();
    // a fold of x cm needs x <= length - x, so a strip shrinks at best to
    // half its length, rounded up; folding exactly half each time reaches that
    let mut folds = Vec::new();
    while n > 1 {
        folds.push((n / 2).to_string());
        n -= n / 2;
    }
    println!("{}", folds.len());
    println!("{}", folds.join(" "));
}
