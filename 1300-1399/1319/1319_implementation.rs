use std::fmt::Write;
use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let n: i32 = input.trim().parse().unwrap();
    let size = n as usize;
    let mut grid = vec![vec![0; size]; size];
    let mut number = 1;
    // diagonals by column minus row, from the top right corner down
    for shift in (1 - n..n).rev() {
        for row in 0.max(-shift)..n.min(n - shift) {
            grid[row as usize][(row + shift) as usize] = number;
            number += 1;
        }
    }
    let mut out = String::new();
    for line in &grid {
        let cells: Vec<String> = line.iter().map(|v| v.to_string()).collect();
        writeln!(out, "{}", cells.join(" ")).unwrap();
    }
    print!("{}", out);
}
