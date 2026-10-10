use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tok = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<i32>().unwrap());
    let n = tok.next().unwrap() as usize;
    let grid: Vec<Vec<i32>> = (0..n).map(|_| tok.by_ref().take(n).collect()).collect();
    let mut best = grid[0][0];
    for top in 0..n {
        // column sums of the rows from top to bottom, then the best run of
        // neighbouring columns by Kadane's scan
        let mut cols = vec![0; n];
        for row in &grid[top..] {
            let mut run = 0;
            for c in 0..n {
                cols[c] += row[c];
                run = if run < 0 { cols[c] } else { run + cols[c] };
                best = best.max(run);
            }
        }
    }
    println!("{}", best);
}
