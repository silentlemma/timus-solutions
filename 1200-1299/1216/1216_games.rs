use std::collections::HashMap;
use std::io::{self, Read};

const NONE: i32 = 0;
const PAWN: i32 = 1;
const QUEEN: i32 = 2;
const ROOK: i32 = 3;
const BISHOP: i32 = 4;
const KNIGHT: i32 = 5;
const PROMOTIONS: [i32; 4] = [QUEEN, ROOK, BISHOP, KNIGHT];
const KING: [(i32, i32); 8] = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
    (1, 1),
    (1, -1),
    (-1, 1),
    (-1, -1),
];
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
// the double steps start from these rows, counted from 0
const WHITE_START: i32 = 1;
const EN_PASSANT_ROW: i32 = 3;
// a square is packed into 5 bits per coordinate in the memo keys
const SHIFT: u32 = 5;
// the king steps list the four straight directions before the diagonal ones
const FIRST_DIAGONAL: usize = 4;

// Black's pawn or piece and the king
#[derive(Clone, Copy)]
struct Black {
    kind: i32,
    bx: i32,
    by: i32,
    kx: i32,
    ky: i32,
}

struct Game {
    n: i32,
    memo: HashMap<i64, bool>,
}

impl Game {
    fn inside(&self, x: i32, y: i32) -> bool {
        x >= 0 && x < self.n && y >= 0 && y < self.n
    }

    // Squares the black piece can reach, ignoring the white pawn.
    fn piece_moves(&self, b: Black) -> Vec<(i32, i32)> {
        let mut out = Vec::new();
        let blocked = |x: i32, y: i32| !self.inside(x, y) || (x, y) == (b.kx, b.ky);
        if b.kind == KNIGHT {
            for (dx, dy) in JUMPS {
                if !blocked(b.bx + dx, b.by + dy) {
                    out.push((b.bx + dx, b.by + dy));
                }
            }
            return out;
        }
        // the queen uses all eight rays, the rook the first four, the bishop the last four
        let from = if b.kind == BISHOP { FIRST_DIAGONAL } else { 0 };
        let to = if b.kind == ROOK {
            FIRST_DIAGONAL
        } else {
            KING.len()
        };
        for &(dx, dy) in &KING[from..to] {
            let (mut x, mut y) = (b.bx + dx, b.by + dy);
            while !blocked(x, y) {
                out.push((x, y));
                x += dx;
                y += dy;
            }
        }
        out
    }

    // Whether White wins against every reply, Black to move.
    fn black_fails(&mut self, wx: i32, wy: i32, b: Black) -> bool {
        if (b.kx - wx).abs().max((b.ky - wy).abs()) == 1 {
            return false; // the king takes the pawn
        }
        if b.kind == PAWN && b.by - 1 == wy && (b.bx - wx).abs() == 1 {
            return false;
        }
        let mut squares = Vec::new();
        if b.kind != NONE && b.kind != PAWN {
            squares = self.piece_moves(b);
            if squares.contains(&(wx, wy)) {
                return false;
            }
        }
        let mut moves = Vec::new();
        for (dx, dy) in KING {
            let (x, y) = (b.kx + dx, b.ky + dy);
            // the pawn attacks the two squares diagonally in front of it
            let attacked = y == wy + 1 && (x - wx).abs() == 1;
            if self.inside(x, y) && !attacked && (b.kind == NONE || (x, y) != (b.bx, b.by)) {
                moves.push(Black { kx: x, ky: y, ..b });
            }
        }
        if b.kind == PAWN {
            let free = |y: i32| (b.bx, y) != (wx, wy) && (b.bx, y) != (b.kx, b.ky);
            let ahead = b.by - 1;
            if ahead >= 0 && free(ahead) {
                if ahead == 0 {
                    for kind in PROMOTIONS {
                        moves.push(Black {
                            kind,
                            by: ahead,
                            ..b
                        });
                    }
                } else {
                    moves.push(Black { by: ahead, ..b });
                    if b.by == self.n - 2 && free(b.by - 2) {
                        moves.push(Black { by: b.by - 2, ..b });
                    }
                }
            }
        } else if b.kind != NONE {
            for (x, y) in squares {
                moves.push(Black { bx: x, by: y, ..b });
            }
        }
        if moves.is_empty() {
            return false; // nothing to move: the pawn has not promoted
        }
        moves.into_iter().all(|m| self.white_wins(wx, wy, m))
    }

    fn white_wins(&mut self, wx: i32, wy: i32, b: Black) -> bool {
        let key = [wx, wy, b.bx + 1, b.by + 1, b.kx, b.ky]
            .iter()
            .fold(b.kind as i64, |k, &v| k << SHIFT | v as i64);
        if let Some(&r) = self.memo.get(&key) {
            return r;
        }
        self.memo.insert(key, false);
        let free =
            |x: i32, y: i32| (x, y) != (b.kx, b.ky) && (b.kind == NONE || (x, y) != (b.bx, b.by));
        // where the pawn lands and what is left of Black
        let mut options = Vec::new();
        if free(wx, wy + 1) {
            options.push((wx, wy + 1, b));
            if wy == WHITE_START && free(wx, wy + 2) {
                // a black pawn beside the landing square takes it en passant
                let beside = b.kind == PAWN && b.by == EN_PASSANT_ROW && (b.bx - wx).abs() == 1;
                if !beside {
                    options.push((wx, wy + 2, b));
                }
            }
        }
        for dx in [-1, 1] {
            if b.kind != NONE && (b.bx, b.by) == (wx + dx, wy + 1) {
                let left = Black {
                    kind: NONE,
                    bx: -1,
                    by: -1,
                    ..b
                };
                options.push((wx + dx, wy + 1, left));
            }
        }
        let n = self.n;
        let result = options
            .into_iter()
            .any(|(x, y, left)| y == n - 1 || self.black_fails(x, y, left));
        self.memo.insert(key, result);
        result
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut t = input.split_ascii_whitespace();
    let n: i32 = t.next().unwrap().parse().unwrap();
    let square = |s: &str| {
        let col = (s.as_bytes()[0] - b'a') as i32;
        (col, s[1..].parse::<i32>().unwrap() - 1)
    };
    let mut next = || square(t.next().unwrap());
    let (w, p, k) = (next(), next(), next());
    let mut game = Game {
        n,
        memo: HashMap::new(),
    };
    let start = Black {
        kind: PAWN,
        bx: p.0,
        by: p.1,
        kx: k.0,
        ky: k.1,
    };
    let win = game.white_wins(w.0, w.1, start);
    println!("{}", if win { "WHITE WINS" } else { "BLACK WINS" });
}
