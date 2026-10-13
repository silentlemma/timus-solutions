use std::io::{self, Read};

/// Whether the black piece slides by (di, dj): no white cell may lie on
/// that side of a black one in the same column or row.
fn slides(grid: &[&[u8]], di: i32, dj: i32) -> bool {
    let n = grid.len();
    (0..n).all(|k| {
        let mut seen_white = false;
        for t in 0..n {
            // walk the line from the side the piece moves towards
            let step = if di + dj > 0 { n - 1 - t } else { t };
            let (i, j) = if di != 0 { (step, k) } else { (k, step) };
            if grid[i][j] == b'0' {
                seen_white = true;
            } else if seen_white {
                return false;
            }
        }
        true
    })
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let n: usize = it.next().unwrap().parse().unwrap();
    let grid: Vec<&[u8]> = (0..n).map(|_| it.next().unwrap().as_bytes()).collect();
    // a sliding direction for either piece is the opposite one for the
    // other; a diagonal slide works only if both of its axis slides do, so
    // trying the four axis directions for the black piece is enough
    let yes =
        slides(&grid, -1, 0) || slides(&grid, 1, 0) || slides(&grid, 0, -1) || slides(&grid, 0, 1);
    println!("{}", if yes { "Yes" } else { "No" });
}
