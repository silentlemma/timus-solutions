use std::io::{self, Read};

const LINES: [[usize; 3]; 8] = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
];
// outcomes for the side to move: win, draw, loss
const WIN: i32 = 1;
const DRAW: i32 = 0;
const LOSS: i32 = -1;

fn won(board: &[u8], mark: u8) -> bool {
    LINES.iter().any(|l| l.iter().all(|&i| board[i] == mark))
}

// the best outcome for the side about to move with mark
fn play(board: &mut Vec<u8>, mark: u8, other: u8) -> i32 {
    let mut best = LOSS;
    let mut moved = false;
    for i in 0..board.len() {
        if board[i] == b'#' {
            moved = true;
            board[i] = mark;
            let result = if won(board, mark) {
                WIN
            } else {
                -play(board, other, mark)
            };
            best = best.max(result);
            board[i] = b'#';
        }
    }
    if moved {
        best
    } else {
        DRAW
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut board: Vec<u8> = input.split_whitespace().flat_map(|r| r.bytes()).collect();
    // three moves each have been made, so crosses move now
    let text = match play(&mut board, b'X', b'O') {
        WIN => "Crosses win",
        DRAW => "Draw",
        _ => "Ouths win",
    };
    println!("{}", text);
}
