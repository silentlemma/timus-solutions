use std::io::{self, Read};

const SIZE: i32 = 8;
const SIDE: usize = SIZE as usize;
const DIAGONALS: [(i32, i32); 4] = [(1, 1), (1, -1), (-1, 1), (-1, -1)];

fn inside(c: i32, r: i32) -> bool {
    (0..SIZE).contains(&c) && (0..SIZE).contains(&r)
}

// some checker has a checker of the other color next to it on a diagonal
// and a free square right behind that one; 0 marks an empty square
fn can_capture(board: &[[u8; SIDE]; SIDE]) -> bool {
    let at = |c: i32, r: i32| board[c as usize][r as usize];
    for c in 0..SIZE {
        for r in 0..SIZE {
            if at(c, r) == 0 {
                continue;
            }
            for &(dc, dr) in &DIAGONALS {
                let (lc, lr) = (c + 2 * dc, r + 2 * dr);
                if inside(lc, lr) {
                    let over = at(c + dc, r + dr);
                    if over != 0 && over != at(c, r) && at(lc, lr) == 0 {
                        return true;
                    }
                }
            }
        }
    }
    false
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut board = [[0u8; SIDE]; SIDE];
    for (number, mv) in input.split_ascii_whitespace().enumerate() {
        let mv = mv.to_ascii_lowercase();
        let c = (mv.as_bytes()[0] - b'a') as usize;
        let r: usize = mv[1..].parse::<usize>().unwrap() - 1;
        board[c][r] = if number % 2 == 0 { 1 } else { 2 }; // white moves first
        if can_capture(&board) {
            println!("{}", number + 1);
            return;
        }
    }
    println!("Draw");
}
