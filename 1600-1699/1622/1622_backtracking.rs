use std::collections::HashSet;
use std::io::{self, Read};

const SIDE: i32 = 7;
const ARM: i32 = 2; // the corners cut from the 7 x 7 square are 2 x 2
const LETTERS: &[u8] = b"ABCDEFG";
const JUMPS: [(i32, i32); 4] = [(0, 1), (1, 0), (0, -1), (-1, 0)];
const CLASSES: i32 = 3; // the residues behind the invariant

struct Move {
    from: u64,
    over: u64,
    to: u64,
    i: usize,
    j: usize,
}

struct Search {
    moves: Vec<Move>,
    dead: HashSet<u64>,
    path: Vec<(usize, usize)>,
    goal: u64,
}

impl Search {
    fn solve(&mut self, board: u64) -> bool {
        if board == self.goal {
            return true;
        }
        if self.dead.contains(&board) {
            return false;
        }
        for k in 0..self.moves.len() {
            let m = &self.moves[k];
            if board & m.from != 0 && board & m.over != 0 && board & m.to == 0 {
                let (next, step) = (board ^ m.from ^ m.over ^ m.to, (m.i, m.j));
                self.path.push(step);
                if self.solve(next) {
                    return true;
                }
                self.path.pop();
            }
        }
        self.dead.insert(board);
        false
    }
}

fn on_board(r: i32, c: i32) -> bool {
    (0..SIDE).contains(&r)
        && (0..SIDE).contains(&c)
        && ((ARM..SIDE - ARM).contains(&r) || (ARM..SIDE - ARM).contains(&c))
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let target = text.trim().as_bytes();
    let mut tc = LETTERS.iter().position(|&l| l == target[0]).unwrap() as i32;
    let mut tr = (target[1] - b'1') as i32;
    let centre = SIDE / 2;
    // A jump changes the parity of the peg count in each class of r + c
    // (mod 3), and of r - c: so the last peg sits where r and c are both
    // congruent to the centre modulo 3.
    if (tr - centre) % CLASSES != 0 || (tc - centre) % CLASSES != 0 || !on_board(tr, tc) {
        println!("Impossible");
        return;
    }
    // The start is symmetric, so an edge target is a quarter turn of the top
    // one: search for the top cell, which the search finds fast, then turn.
    let mut turns = 0;
    while (tr, tc) != (centre, centre) && (tr, tc) != (SIDE - 1, centre) {
        let r = SIDE - 1 - tc; // a quarter turn back
        tc = tr;
        tr = r;
        turns += 1;
    }
    let mut cells = Vec::new();
    let mut index = [[0usize; SIDE as usize]; SIDE as usize];
    for r in 0..SIDE {
        for c in 0..SIDE {
            if on_board(r, c) {
                index[r as usize][c as usize] = cells.len();
                cells.push((r, c));
            }
        }
    }
    let at = |r: i32, c: i32| index[r as usize][c as usize];
    // every move as (from, over, to) bits
    let mut moves = Vec::new();
    for &(r, c) in &cells {
        for &(dr, dc) in &JUMPS {
            let (r1, c1, r2, c2) = (r + dr, c + dc, r + 2 * dr, c + 2 * dc);
            if on_board(r1, c1) && on_board(r2, c2) {
                moves.push(Move {
                    from: 1 << at(r, c),
                    over: 1 << at(r1, c1),
                    to: 1 << at(r2, c2),
                    i: at(r, c),
                    j: at(r2, c2),
                });
            }
        }
    }
    let full: u64 = (1 << cells.len()) - 1;
    let start = full & !(1 << at(centre, centre));
    let mut search = Search {
        moves,
        dead: HashSet::new(),
        path: Vec::new(),
        goal: 1 << at(tr, tc),
    };
    search.solve(start);
    let name = |i: usize| {
        let (mut r, mut c) = cells[i];
        for _ in 0..turns {
            let nr = c; // a quarter turn forward
            c = SIDE - 1 - r;
            r = nr;
        }
        format!("{}{}", LETTERS[c as usize] as char, r + 1)
    };
    let lines: Vec<String> =
        search.path.iter().map(|&(i, j)| format!("{}-{}", name(i), name(j))).collect();
    println!("{}", lines.join("\n"));
}
