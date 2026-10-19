use std::io::{self, Read};

const MOVE_COUNT: usize = 8;
const PIECE_COUNT: usize = 5;
const MOVES: [(i64, i64); MOVE_COUNT] = [
    (-2, -1),
    (-2, 1),
    (-1, -2),
    (-1, 2),
    (1, -2),
    (1, 2),
    (2, -1),
    (2, 1),
];

fn solve(n: i64, x: i64, y: i64) -> [i64; PIECE_COUNT] {
    let king = (1 + (x > 1) as i64 + (x < n) as i64) * (1 + (y > 1) as i64 + (y < n) as i64) - 1;
    let mut knight = 0;
    for (dx, dy) in MOVES {
        let (nx, ny) = (x + dx, y + dy);
        if 1 <= nx && nx <= n && 1 <= ny && ny <= n {
            knight += 1;
        }
    }
    let bishop = (x - 1).min(y - 1) + (x - 1).min(n - y) + (n - x).min(y - 1) + (n - x).min(n - y);
    let rook = 2 * (n - 1);
    [king, knight, bishop, rook, rook + bishop]
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut t = input.split_whitespace();
    let n = t.next().unwrap().parse().unwrap();
    let x = t.next().unwrap().parse().unwrap();
    let y = t.next().unwrap().parse().unwrap();
    let labels = ["King", "Knight", "Bishop", "Rook", "Queen"];
    for (label, value) in labels.iter().zip(solve(n, x, y)) {
        println!("{}: {}", label, value);
    }
}
