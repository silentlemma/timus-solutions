use std::collections::HashSet;
use std::io::{self, Read};

const CORNERS: usize = 4; // a loop turns at least four times, by 90 degrees each
const FIRST_STAIR: usize = 12; // all-turn loops have 4 or at least 12 turns
const NOTCHED_HEIGHT: i64 = 3; // rows of the box when a corner is cut in

/// F, L or R for every cell of a closed loop of cells.
fn letters(cells: &[(i64, i64)]) -> String {
    let n = cells.len();
    (0..n)
        .map(|i| {
            let (a, b, c) = (cells[(i + n - 1) % n], cells[i], cells[(i + 1) % n]);
            let (dx1, dy1, dx2, dy2) = (b.0 - a.0, b.1 - a.1, c.0 - b.0, c.1 - b.1);
            if dx1 == dx2 && dy1 == dy2 {
                'F'
            } else if dx1 * dy2 - dy1 * dx2 > 0 {
                'L'
            } else {
                'R'
            }
        })
        .collect()
}

/// The border of a width x height box, counterclockwise from the lower left
/// corner, with bumps (2 cells wide, 1 high) on the top and bottom rows, and
/// with the lower left corner cut in if notch is set.
fn ring(width: i64, height: i64, bumps: usize, notch: bool) -> Vec<(i64, i64)> {
    let free_top: Vec<i64> = (2..=width - 2).rev().step_by(2).collect(); // pairs (x, x - 1)
    let first_bottom = 2 + notch as i64;
    let free_bottom: Vec<i64> = (first_bottom..width - 1).step_by(2).collect(); // pairs (x - 1, x)
    let up = bumps.min(free_top.len());
    let up_at: HashSet<i64> = free_top[..up].iter().copied().collect();
    let down_at: HashSet<i64> = free_bottom[..bumps - up].iter().copied().collect();
    let mut cells = if notch {
        vec![(1, 1), (1, 0)]
    } else {
        vec![(0, 0)]
    };
    for x in cells[cells.len() - 1].0 + 1..width {
        // the bottom row, going east
        if down_at.contains(&x) {
            cells.push((x - 1, -1));
            cells.push((x, -1));
        }
        cells.push((x, 0));
    }
    for y in 1..height {
        cells.push((width - 1, y));
    }
    let mut x = width - 2;
    while x >= 0 {
        // the top row, going west
        cells.push((x, height - 1));
        if up_at.contains(&x) {
            cells.extend([(x, height), (x - 1, height), (x - 1, height - 1)]);
            x -= 1;
        }
        x -= 1;
    }
    // the left column, going south; with a notch its last cell (0, 1) leads
    // into (1, 1) instead of the corner
    for y in (1..height - 1).rev() {
        cells.push((0, y));
    }
    cells
}

fn build(straights: usize, turns: usize) -> String {
    if straights == 0 && turns >= FIRST_STAIR {
        // a staircase loop: four corners and steps LR on the sides
        let half = format!("L{}LLR", "LR".repeat((turns - CORNERS) / CORNERS - 1));
        return half.repeat(2);
    }
    let notch = turns % CORNERS == 2;
    let bumps = (turns - CORNERS) / CORNERS; // a notch takes the other 2 turns
    let width = (2 + straights / 2 + bumps) as i64;
    letters(&ring(
        width,
        if notch { NOTCHED_HEIGHT } else { 2 },
        bumps,
        notch,
    ))
}

fn main() {
    let mut s = String::new();
    io::stdin().read_to_string(&mut s).unwrap();
    let v: Vec<usize> = s
        .split_ascii_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();
    // both counts even, at least 4 turns, and without straights the turns
    // must be 4 or a multiple of 4 from 12
    let (straights, mut turns) = (v[0] - v[0] % 2, v[1] - v[1] % 2);
    if turns < CORNERS {
        println!("Atawazu");
        return;
    }
    if straights == 0 {
        turns -= turns % CORNERS;
        if turns < FIRST_STAIR {
            turns = CORNERS;
        }
    }
    let path = build(straights, turns);
    println!("{}\n{}", path.len(), path);
}
