use std::io::{self, Read};

const SIDE: usize = 8;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<i64> = input.split_ascii_whitespace().map(|w| w.parse().unwrap()).collect();
    let grid: Vec<&[i64]> = v.chunks(SIDE).collect();
    // moving from u to a neighbour v with weight w(v) / W(u), where W(u) sums
    // the weights around u, the walk is balanced by w(u) W(u) in every cell,
    // and after so many steps it has settled into that distribution
    let mut score = vec![vec![0i64; SIDE]; SIDE];
    for r in 0..SIDE {
        for c in 0..SIDE {
            let mut around = 0;
            for y in r.saturating_sub(1)..(r + 2).min(SIDE) {
                for x in c.saturating_sub(1)..(c + 2).min(SIDE) {
                    if y != r || x != c {
                        around += grid[y][x];
                    }
                }
            }
            score[r][c] = grid[r][c] * around;
        }
    }
    let total: i64 = score.iter().map(|row| row.iter().sum::<i64>()).sum();
    let mut out = String::new();
    for row in &score {
        let cells: Vec<String> =
            row.iter().map(|&s| format!("{:.15}", s as f64 / total as f64)).collect();
        out.push_str(&cells.join(" "));
        out.push('\n');
    }
    print!("{}", out);
}
