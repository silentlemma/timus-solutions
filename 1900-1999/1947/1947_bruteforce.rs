use std::io::{self, Read};

const SIDE: i32 = 5;
const PORT_COUNT: usize = 4;
const CELLS: usize = (SIDE * SIDE) as usize;
const MIN_TILES: usize = 3;
const TOP: usize = 0;
const RIGHT: usize = 1;
const BOTTOM: usize = 2;
const LEFT: usize = 3;
const ROW_STEP: [i32; PORT_COUNT] = [-1, 0, 1, 0];
const COLUMN_STEP: [i32; PORT_COUNT] = [0, 1, 0, -1];
const OPPOSITE: [usize; PORT_COUNT] = [BOTTOM, LEFT, TOP, RIGHT];
const CONNECTIONS: [[usize; PORT_COUNT]; 2] =
    [[LEFT, BOTTOM, RIGHT, TOP], [RIGHT, TOP, LEFT, BOTTOM]];
const DIRECTIONS: [char; PORT_COUNT] = ['L', 'R', 'U', 'D'];
const HOLE_ROW: [i32; PORT_COUNT] = [0, 0, 1, -1];
const HOLE_COLUMN: [i32; PORT_COUNT] = [1, -1, 0, 0];

fn winning(board: &[u8]) -> bool {
    for side in 0..PORT_COUNT {
        for offset in 0..SIDE {
            let mut row = if side == TOP {
                0
            } else if side == BOTTOM {
                SIDE - 1
            } else {
                offset
            };
            let mut column = if side == LEFT {
                0
            } else if side == RIGHT {
                SIDE - 1
            } else {
                offset
            };
            let (mut incoming, mut count) = (side, 0);
            let mut visited = [false; CELLS * PORT_COUNT];
            let mut tiles = [false; CELLS];
            loop {
                let index = (row * SIDE + column) as usize;
                let state = index * PORT_COUNT + incoming;
                if board[index] == b'*' || visited[state] {
                    break;
                }
                visited[state] = true;
                if !tiles[index] {
                    tiles[index] = true;
                    count += 1;
                }
                let kind = usize::from(board[index] != b'/');
                let outgoing = CONNECTIONS[kind][incoming];
                row += ROW_STEP[outgoing];
                column += COLUMN_STEP[outgoing];
                if row < 0 || row >= SIDE || column < 0 || column >= SIDE {
                    if outgoing != side && count >= MIN_TILES {
                        return true;
                    }
                    break;
                }
                incoming = OPPOSITE[outgoing];
            }
        }
    }
    false
}

fn solve(board: &[u8]) -> String {
    if winning(board) {
        return "WIN".to_owned();
    }
    let empty = board.iter().position(|&tile| tile == b'*').unwrap();
    let (row, column) = (empty as i32 / SIDE, empty as i32 % SIDE);
    for motion in 0..PORT_COUNT {
        for amount in 1..SIDE {
            let end_row = row + HOLE_ROW[motion] * amount;
            let end_column = column + HOLE_COLUMN[motion] * amount;
            if end_row < 0 || end_row >= SIDE || end_column < 0 || end_column >= SIDE {
                continue;
            }
            let mut changed = board.to_vec();
            let mut hole = empty as i32;
            for _ in 0..amount {
                let following = hole + HOLE_ROW[motion] * SIDE + HOLE_COLUMN[motion];
                changed.swap(hole as usize, following as usize);
                hole = following;
            }
            if winning(&changed) {
                return format!("{}{}", DIRECTIONS[motion], amount);
            }
        }
    }
    "FAIL".to_owned()
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let board: Vec<u8> = input.split_whitespace().flat_map(str::bytes).collect();
    println!("{}", solve(&board));
}
