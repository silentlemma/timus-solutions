use std::io::{self, Read};

const PIECE_SIDE: usize = 4;
const GRID_SIDE: usize = 3;
const PIECE_COUNT: usize = GRID_SIDE * GRID_SIDE;
const TURN_COUNT: usize = 4;
const STATE_COUNT: usize = PIECE_COUNT * TURN_COUNT;
const PIXELS: usize = PIECE_SIDE * PIECE_SIDE;
const STRIDE: usize = PIECE_SIDE - 1;
const BOARD_SIDE: usize = GRID_SIDE * STRIDE + 1;
type Piece = [i32; PIXELS];

struct Solver {
    states: [Piece; STATE_COUNT],
    masks: [u64; PIECE_COUNT],
    compatible: [[u64; STATE_COUNT]; TURN_COUNT],
    neighbors: Vec<Vec<(usize, usize)>>,
    placement: [Option<usize>; PIECE_COUNT],
}

impl Solver {
    fn search(&mut self, domains: [u64; PIECE_COUNT], remaining: usize) -> bool {
        if remaining == 0 {
            return true;
        }
        let slot = (0..PIECE_COUNT)
            .filter(|&i| self.placement[i].is_none())
            .min_by_key(|&i| {
                (
                    domains[i].count_ones(),
                    TURN_COUNT - self.neighbors[i].len(),
                )
            })
            .unwrap();
        let mut choices = domains[slot];
        while choices != 0 {
            let state = choices.trailing_zeros() as usize;
            choices &= choices - 1;
            self.placement[slot] = Some(state);
            let unused = !self.masks[state / TURN_COUNT];
            let mut following = domains;
            for domain in &mut following {
                *domain &= unused;
            }
            for &(direction, adjacent) in &self.neighbors[slot] {
                if self.placement[adjacent].is_none() {
                    following[adjacent] &= self.compatible[direction][state];
                }
            }
            let possible =
                (0..PIECE_COUNT).all(|i| self.placement[i].is_some() || following[i] != 0);
            if possible && self.search(following, remaining - 1) {
                return true;
            }
            self.placement[slot] = None;
        }
        false
    }
}

fn assemble(pieces: &[Piece; PIECE_COUNT]) -> [[i32; BOARD_SIDE]; BOARD_SIDE] {
    let mut solver = Solver {
        states: [[0; PIXELS]; STATE_COUNT],
        masks: [0; PIECE_COUNT],
        compatible: [[0; STATE_COUNT]; TURN_COUNT],
        neighbors: vec![Vec::new(); PIECE_COUNT],
        placement: [None; PIECE_COUNT],
    };
    let mut initial = 0_u64;
    for (index, original) in pieces.iter().enumerate() {
        let mut current = *original;
        for turn in 0..TURN_COUNT {
            let state = index * TURN_COUNT + turn;
            solver.states[state] = current;
            solver.masks[index] |= 1_u64 << state;
            let duplicate = (index * TURN_COUNT..state).any(|i| solver.states[i] == current);
            if !duplicate && (index != 0 || turn == 0) {
                initial |= 1_u64 << state;
            }
            let mut rotated = [0; PIXELS];
            for r in 0..PIECE_SIDE {
                for c in 0..PIECE_SIDE {
                    rotated[r * PIECE_SIDE + c] = current[(PIECE_SIDE - 1 - c) * PIECE_SIDE + r];
                }
            }
            current = rotated;
        }
    }
    let mut edges = [[[0; PIECE_SIDE]; TURN_COUNT]; STATE_COUNT];
    for (state, piece) in solver.states.iter().enumerate() {
        for i in 0..PIECE_SIDE {
            edges[state][0][i] = piece[i];
            edges[state][1][i] = piece[i * PIECE_SIDE + PIECE_SIDE - 1];
            edges[state][2][i] = piece[(PIECE_SIDE - 1) * PIECE_SIDE + i];
            edges[state][TURN_COUNT - 1][i] = piece[i * PIECE_SIDE];
        }
    }
    for direction in 0..TURN_COUNT {
        for first in 0..STATE_COUNT {
            for second in 0..STATE_COUNT {
                if first / TURN_COUNT != second / TURN_COUNT
                    && edges[first][direction] == edges[second][(direction + 2) % TURN_COUNT]
                {
                    solver.compatible[direction][first] |= 1_u64 << second;
                }
            }
        }
    }
    let directions: [(isize, isize); TURN_COUNT] = [(-1, 0), (0, 1), (1, 0), (0, -1)];
    for slot in 0..PIECE_COUNT {
        for (direction, &(dr, dc)) in directions.iter().enumerate() {
            let r = (slot / GRID_SIDE) as isize + dr;
            let c = (slot % GRID_SIDE) as isize + dc;
            if r >= 0 && r < GRID_SIDE as isize && c >= 0 && c < GRID_SIDE as isize {
                solver.neighbors[slot].push((direction, r as usize * GRID_SIDE + c as usize));
            }
        }
    }
    assert!(solver.search([initial; PIECE_COUNT], PIECE_COUNT));
    let mut board = [[0; BOARD_SIDE]; BOARD_SIDE];
    for slot in 0..PIECE_COUNT {
        let state = solver.placement[slot].unwrap();
        for r in 0..PIECE_SIDE {
            for c in 0..PIECE_SIDE {
                board[slot / GRID_SIDE * STRIDE + r][slot % GRID_SIDE * STRIDE + c] =
                    solver.states[state][r * PIECE_SIDE + c];
            }
        }
    }
    board
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let mut pieces = [[0; PIXELS]; PIECE_COUNT];
    for piece in &mut pieces {
        for value in piece {
            *value = tokens.next().unwrap().parse().unwrap();
        }
    }
    let mut out = String::new();
    for row in assemble(&pieces) {
        for (c, value) in row.iter().enumerate() {
            if c != 0 {
                out.push(' ');
            }
            out.push_str(&value.to_string());
        }
        out.push('\n');
    }
    print!("{out}");
}
