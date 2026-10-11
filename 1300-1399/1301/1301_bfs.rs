use std::collections::VecDeque;
use std::io::{self, Read};

const TOP: usize = 0;
const BOTTOM: usize = 1;
const NORTH: usize = 2;
const SOUTH: usize = 3;
const EAST: usize = 4;
const WEST: usize = 5;
const SIDES: usize = 6;

const GO_EAST: usize = 0;
const GO_WEST: usize = 1;
const GO_NORTH: usize = 2;
const GO_SOUTH: usize = 3;
const MOVES: usize = 4;

const SIZE: usize = 12;
const DX: [i32; MOVES] = [1, -1, 0, 0];
const DY: [i32; MOVES] = [0, 0, 1, -1];

// a roll moves every face to a new side; only the side that holds the
// starting top face matters, so each roll (east, west, north, south)
// maps every side to the side it lands on
const ROLL: [[usize; SIDES]; MOVES] = [
    [EAST, WEST, NORTH, SOUTH, BOTTOM, TOP],
    [WEST, EAST, NORTH, SOUTH, TOP, BOTTOM],
    [NORTH, SOUTH, BOTTOM, TOP, EAST, WEST],
    [SOUTH, NORTH, TOP, BOTTOM, EAST, WEST],
];

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_ascii_whitespace();
    let mut number = || words.next().unwrap().parse::<usize>().unwrap();
    let (width, height) = (number(), number());
    let start = (number(), number());
    let goal = (number(), number());
    let mut blocked = [[[false; MOVES]; SIZE]; SIZE];
    let mut kind = "";
    let rest: Vec<&str> = words.collect();
    let mut i = 0;
    while i < rest.len() {
        if rest[i] == "v" || rest[i] == "h" {
            kind = rest[i];
            i += 1;
            continue;
        }
        let n: usize = rest[i].parse().unwrap();
        let m: usize = rest[i + 1].parse().unwrap();
        i += 2;
        // a v wall stands between (n, m) and (n + 1, m), an h wall between
        // (n, m) and (n, m + 1), and each blocks the move both ways
        if kind == "v" {
            blocked[n][m][GO_EAST] = true;
            blocked[n + 1][m][GO_WEST] = true;
        } else {
            blocked[n][m][GO_NORTH] = true;
            blocked[n][m + 1][GO_SOUTH] = true;
        }
    }
    let mut dist = vec![vec![vec![-1i32; SIDES]; SIZE]; SIZE];
    let mut queue = VecDeque::new();
    dist[start.0][start.1][TOP] = 0;
    queue.push_back((start.0, start.1, TOP));
    while let Some((x, y, side)) = queue.pop_front() {
        if (x, y) == goal && side == TOP {
            println!("{}", dist[x][y][side]);
            return;
        }
        for k in 0..MOVES {
            let (nx, ny) = (x as i32 + DX[k], y as i32 + DY[k]);
            if nx < 1 || nx > width as i32 || ny < 1 || ny > height as i32 || blocked[x][y][k] {
                continue;
            }
            let (nx, ny, ns) = (nx as usize, ny as usize, ROLL[k][side]);
            if dist[nx][ny][ns] < 0 {
                dist[nx][ny][ns] = dist[x][y][side] + 1;
                queue.push_back((nx, ny, ns));
            }
        }
    }
    println!("No solution");
}
