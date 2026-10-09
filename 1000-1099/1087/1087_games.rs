use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<usize> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let (n, m) = (v[0], v[1]);
    let moves = &v[2..2 + m];
    // win[x]: the player to move with x stones left wins; with none left the
    // other player has just taken the last stone and lost
    let mut win = vec![false; n + 1];
    win[0] = true;
    for x in 1..=n {
        win[x] = moves.iter().any(|&k| k <= x && !win[x - k]);
    }
    println!("{}", if win[n] { 1 } else { 2 });
}
