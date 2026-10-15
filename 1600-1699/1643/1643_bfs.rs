use std::collections::VecDeque;
use std::io::{self, Read};

const INF: usize = 1 << 29;
const LETTERS: usize = 26;
const MARKS: &[u8] = b"$!*"; // the two armies and the fortress

/// days to every district; teleports are free, so 0-1 BFS
fn bfs(
    grid: &[Vec<u8>],
    gates: &[Vec<(usize, usize)>],
    start: (usize, usize),
    avoid: Option<(usize, usize)>,
) -> Vec<Vec<usize>> {
    let (n, m) = (grid.len(), grid[0].len());
    let mut dist = vec![vec![INF; m]; n];
    let mut used = [false; LETTERS]; // teleport letters already spread
    let mut queue = VecDeque::from(vec![start]);
    dist[start.0][start.1] = 0;
    while let Some((r, c)) = queue.pop_front() {
        let d = dist[r][c];
        let ch = grid[r][c];
        if ch.is_ascii_uppercase() && !used[(ch - b'A') as usize] {
            used[(ch - b'A') as usize] = true;
            for &(gr, gc) in &gates[(ch - b'A') as usize] {
                if dist[gr][gc] > d {
                    dist[gr][gc] = d;
                    queue.push_front((gr, gc));
                }
            }
        }
        for nr in r.saturating_sub(1)..(r + 2).min(n) {
            for nc in c.saturating_sub(1)..(c + 2).min(m) {
                if grid[nr][nc] == b'#' || Some((nr, nc)) == avoid || dist[nr][nc] <= d + 1 {
                    continue;
                }
                dist[nr][nc] = d + 1;
                queue.push_back((nr, nc));
            }
        }
    }
    dist
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut words = text.split_ascii_whitespace();
    let n: usize = words.next().unwrap().parse().unwrap();
    let _m: usize = words.next().unwrap().parse().unwrap();
    let grid: Vec<Vec<u8>> = (0..n).map(|_| words.next().unwrap().bytes().collect()).collect();
    let mut gates = vec![Vec::new(); LETTERS];
    let mut marks = vec![(0, 0); MARKS.len()];
    for (r, row) in grid.iter().enumerate() {
        for (c, &ch) in row.iter().enumerate() {
            if ch.is_ascii_uppercase() {
                gates[(ch - b'A') as usize].push((r, c));
            }
            if let Some(k) = MARKS.iter().position(|&x| x == ch) {
                marks[k] = (r, c);
            }
        }
    }
    let fortress = marks[2];
    let first = bfs(&grid, &gates, marks[0], Some(fortress));
    let second = bfs(&grid, &gates, marks[1], Some(fortress));
    let attack = bfs(&grid, &gates, fortress, None); // moves are symmetric: the way back
    // the earlier army waits at the meeting place, then both march together
    let mut best = INF;
    for r in 0..n {
        for c in 0..grid[r].len() {
            if (r, c) != fortress {
                best = best.min(first[r][c].max(second[r][c]) + attack[r][c]);
            }
        }
    }
    if best >= INF {
        println!("Impossible");
    } else {
        println!("{}", best);
    }
}
