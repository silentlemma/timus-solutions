use std::io::{self, Read};

const ROWS: usize = 7;
const COLUMNS: usize = 9;
const CONNECT: usize = 4;
const DIRECTION_COUNT: usize = 4;
const MAX_MOVES: usize = ROWS * COLUMNS;
const FIRST_WIN: usize = 2 * (CONNECT - 1);

fn make_masks() -> ([usize; DIRECTION_COUNT], [u64; DIRECTION_COUNT]) {
    let row_steps: [isize; DIRECTION_COUNT] = [1, 0, 1, -1];
    let column_steps: [isize; DIRECTION_COUNT] = [0, 1, 1, 1];
    let mut shifts = [0; DIRECTION_COUNT];
    let mut masks = [0; DIRECTION_COUNT];
    for direction in 0..DIRECTION_COUNT {
        let dr = row_steps[direction];
        let dc = column_steps[direction];
        shifts[direction] = (dc * ROWS as isize + dr) as usize;
        for column in 0..COLUMNS {
            for row in 0..ROWS {
                let end_row = row as isize + (CONNECT - 1) as isize * dr;
                let end_column = column as isize + (CONNECT - 1) as isize * dc;
                if end_row >= 0 && end_row < ROWS as isize && end_column < COLUMNS as isize {
                    masks[direction] |= 1 << (column * ROWS + row);
                }
            }
        }
    }
    (shifts, masks)
}

fn has_won(board: u64, shifts: &[usize; DIRECTION_COUNT], masks: &[u64; DIRECTION_COUNT]) -> bool {
    for direction in 0..DIRECTION_COUNT {
        let shift = shifts[direction];
        let pair = board & (board >> shift);
        // The mask excludes lines that wrap across column boundaries.
        if pair & (pair >> (2 * shift)) & masks[direction] != 0 {
            return true;
        }
    }
    false
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let moves = input.trim().as_bytes();
    let (shifts, masks) = make_masks();
    let mut wins = 0;
    let mut draws = 0;
    for start in 0..moves.len() {
        let mut heights = [0; COLUMNS];
        let mut boards = [0_u64; 2];
        let mut placed = 0;
        let limit = MAX_MOVES.min(moves.len() - start);
        for turn in 0..limit {
            let column = (moves[start + turn] - b'1') as usize;
            if heights[column] < ROWS {
                let player = turn & 1;
                boards[player] |= 1 << (column * ROWS + heights[column]);
                heights[column] += 1;
                placed += 1;
                if turn >= FIRST_WIN && has_won(boards[player], &shifts, &masks) {
                    wins += 1;
                    break;
                }
            }
            if turn + 1 == MAX_MOVES && placed == MAX_MOVES {
                draws += 1;
            }
        }
    }
    println!("{} {}", wins, draws);
}
