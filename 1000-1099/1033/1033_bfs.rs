use std::collections::VecDeque;
use std::io::{self, Read};

const SIDE_AREA: usize = 9;
const ENTRANCE_SIDES: usize = 4;
const STEPS: [(isize, isize); 4] = [(-1, 0), (1, 0), (0, -1), (0, 1)];

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_ascii_whitespace();
    let n: usize = tokens.next().unwrap().parse().unwrap();
    let grid: Vec<&[u8]> = tokens.take(n).map(|row| row.as_bytes()).collect();
    // visit every empty cell reachable from either entrance; each side of
    // such a cell that faces a block or the outer wall is a visible wall
    let mut seen = vec![vec![false; n]; n];
    let mut queue = VecDeque::from([(0, 0), (n - 1, n - 1)]);
    seen[0][0] = true;
    seen[n - 1][n - 1] = true;
    let mut sides = 0;
    while let Some((i, j)) = queue.pop_front() {
        for &(di, dj) in &STEPS {
            let (a, b) = (i as isize + di, j as isize + dj);
            if a < 0 || b < 0 || a >= n as isize || b >= n as isize {
                sides += 1;
                continue;
            }
            let (a, b) = (a as usize, b as usize);
            if grid[a][b] == b'#' {
                sides += 1;
            } else if !seen[a][b] {
                seen[a][b] = true;
                queue.push_back((a, b));
            }
        }
    }
    // the outer sides of the two entrance cells are openings, not walls
    println!("{}", (sides - ENTRANCE_SIDES) * SIDE_AREA);
}
