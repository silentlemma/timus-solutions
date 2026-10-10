use std::io::{self, Read};

const SIDE: i32 = 8;
const JUMPS: [(i32, i32); 8] = [
    (1, 2),
    (2, 1),
    (2, -1),
    (1, -2),
    (-1, -2),
    (-2, -1),
    (-2, 1),
    (-1, 2),
];

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let n: usize = it.next().unwrap().parse().unwrap();
    let mut out = String::new();
    for square in it.take(n) {
        let b = square.as_bytes();
        let (col, row) = ((b[0] - b'a') as i32, (b[1] - b'1') as i32);
        // the knight attacks every square one jump away that is on the board
        let count = JUMPS
            .iter()
            .filter(|(dc, dr)| (0..SIDE).contains(&(col + dc)) && (0..SIDE).contains(&(row + dr)))
            .count();
        out += &format!("{}\n", count);
    }
    print!("{}", out);
}
