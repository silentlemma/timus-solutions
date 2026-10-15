use std::io::{self, Read};

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let nums: Vec<i64> = text.split_ascii_whitespace().map(|w| w.parse().unwrap()).collect();
    let n = nums[0] as usize;
    let mut heights = nums[1..=n * n].to_vec();
    heights.sort_unstable_by(|a, b| b.cmp(a));
    let mid = n as i64 / 2;
    // cells by (nearer, farther) distance from the centre row and column:
    // along any row or column this grows outwards on each side
    let mut cells = Vec::new();
    for r in 0..n as i64 {
        for c in 0..n as i64 {
            let (a, b) = ((r - mid).abs(), (c - mid).abs());
            cells.push((a.min(b), a.max(b), r as usize, c as usize));
        }
    }
    cells.sort();
    let mut grid = vec![vec![0; n]; n];
    for (&h, &(_, _, r, c)) in heights.iter().zip(cells.iter()) {
        grid[r][c] = h;
    }
    let lines: Vec<String> = grid
        .iter()
        .map(|row| row.iter().map(|h| h.to_string()).collect::<Vec<_>>().join(" "))
        .collect();
    println!("{}", lines.join("\n"));
}
