use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let n: usize = it.next().unwrap().parse().unwrap();
    let grid: Vec<Vec<&str>> = (0..n).map(|_| it.by_ref().take(n).collect()).collect();
    // diagonal s holds the cells with row + column = s; each is read from
    // its lowest row up
    let mut out: Vec<&str> = Vec::with_capacity(n * n);
    for s in 0..2 * n - 1 {
        let lo = s.saturating_sub(n - 1);
        for i in (lo..=s.min(n - 1)).rev() {
            out.push(grid[i][s - i]);
        }
    }
    println!("{}", out.join(" "));
}
