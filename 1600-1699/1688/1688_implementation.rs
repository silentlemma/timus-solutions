use std::io::{self, Read};

const SHARES: i64 = 3; // a bill is split three ways

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let data: Vec<i64> = text.split_ascii_whitespace().map(|w| w.parse().unwrap()).collect();
    let (n, m) = (data[0], data[1] as usize);
    let mut total = 0;
    for i in 0..m {
        total += data[2 + i];
        // Vanya's share total / 3 exceeds n exactly when total > 3n
        if total > SHARES * n {
            println!("Free after {} times.", i + 1);
            return;
        }
    }
    println!("Team.GOV!");
}
