use std::io::{self, Read};

const SIZE: i32 = 8;
const PAWN: i32 = 1;
const KNIGHT: i32 = 2;
const BISHOP: i32 = 3;
const ROOK: i32 = 4;
const QUEEN: i32 = 5;
const KING: i32 = 6;
const TO_FILE: usize = 3; // a move reads like e2-e4
const TO_RANK: usize = 4;

/// board[r][f]: row r is rank r + 1, column f is file a + f.
struct Board {
    cells: [[i32; SIZE as usize]; SIZE as usize],
}

fn inside(f: i32, r: i32) -> bool {
    (0..SIZE).contains(&f) && (0..SIZE).contains(&r)
}

impl Board {
    fn at(&self, f: i32, r: i32) -> i32 {
        self.cells[r as usize][f as usize]
    }

    fn put(&mut self, f: i32, r: i32, v: i32) {
        self.cells[r as usize][f as usize] = v;
    }

    /// Can the piece on (f, r) move to (tf, tr), ignoring checks?
    fn reaches(&self, f: i32, r: i32, tf: i32, tr: i32) -> bool {
        let (piece, target) = (self.at(f, r), self.at(tf, tr));
        let (side, kind) = (piece.signum(), piece.abs());
        let (df, dr) = (tf - f, tr - r);
        if (df == 0 && dr == 0) || target * side > 0 {
            return false;
        }
        if kind == PAWN {
            // a pawn may step two squares from its second rank
            let home = if side > 0 { 1 } else { SIZE - 2 };
            if df == 0 && target == 0 {
                return dr == side || (dr == 2 * side && r == home && self.at(f, r + side) == 0);
            }
            return df.abs() == 1 && dr == side && target * side < 0;
        }
        if kind == KNIGHT {
            return (df * dr).abs() == 2;
        }
        if kind == KING {
            return df.abs() <= 1 && dr.abs() <= 1;
        }
        let straight = df == 0 || dr == 0;
        let diagonal = df.abs() == dr.abs();
        if !((kind == BISHOP && diagonal)
            || (kind == ROOK && straight)
            || (kind == QUEEN && (straight || diagonal)))
        {
            return false;
        }
        let (sf, sr) = (df.signum(), dr.signum());
        let (mut f, mut r) = (f + sf, r + sr);
        while f != tf || r != tr {
            if self.at(f, r) != 0 {
                return false;
            }
            f += sf;
            r += sr;
        }
        true
    }

    /// Is any king of this side attacked?
    fn in_check(&self, side: i32) -> bool {
        for kr in 0..SIZE {
            for kf in 0..SIZE {
                if self.at(kf, kr) != KING * side {
                    continue;
                }
                for r in 0..SIZE {
                    for f in 0..SIZE {
                        if self.at(f, r) * side < 0 && self.reaches(f, r, kf, kr) {
                            return true;
                        }
                    }
                }
            }
        }
        false
    }

    /// Makes the move if it is legal and returns the piece it took.
    fn legal(&mut self, side: i32, f: i32, r: i32, tf: i32, tr: i32) -> Option<i32> {
        if !inside(f, r)
            || !inside(tf, tr)
            || self.at(f, r) * side <= 0
            || !self.reaches(f, r, tf, tr)
        {
            return None;
        }
        let taken = self.at(tf, tr);
        self.put(tf, tr, self.at(f, r));
        self.put(f, r, 0);
        if self.in_check(side) {
            self.put(f, r, self.at(tf, tr));
            self.put(tf, tr, taken);
            return None;
        }
        Some(taken)
    }

    fn has_move(&mut self, side: i32) -> bool {
        for r in 0..SIZE {
            for f in 0..SIZE {
                if self.at(f, r) * side <= 0 {
                    continue;
                }
                for tr in 0..SIZE {
                    for tf in 0..SIZE {
                        if let Some(taken) = self.legal(side, f, r, tf, tr) {
                            self.put(f, r, self.at(tf, tr));
                            self.put(tf, tr, taken);
                            return true;
                        }
                    }
                }
            }
        }
        false
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_ascii_whitespace();
    let mut board = Board {
        cells: [[0; SIZE as usize]; SIZE as usize],
    };
    for r in (0..SIZE).rev() {
        for f in 0..SIZE {
            let v = words.next().unwrap().parse().unwrap();
            board.put(f, r, v);
        }
    }
    let count: usize = words.next().unwrap().parse().unwrap();
    let mut side = if words.next().unwrap() == "White" {
        1
    } else {
        -1
    };
    let mut out = Vec::new();
    for move_text in words.take(count) {
        let m = move_text.as_bytes();
        let (f, r) = ((m[0] - b'a') as i32, (m[1] - b'1') as i32);
        let (tf, tr) = ((m[TO_FILE] - b'a') as i32, (m[TO_RANK] - b'1') as i32);
        if board.legal(side, f, r, tf, tr).is_none() {
            out.push("Incorrect".to_string());
            break;
        }
        side = -side;
        let (check, free) = (board.in_check(side), board.has_move(side));
        let word = match (free, check) {
            (false, true) => "Mate",
            (false, false) => "Draw",
            (true, true) => "Check",
            (true, false) => "Correct",
        };
        out.push(word.to_string());
        if !free {
            break;
        }
    }
    out.push(String::new());
    for r in (0..SIZE).rev() {
        let row: Vec<String> = (0..SIZE).map(|f| board.at(f, r).to_string()).collect();
        out.push(row.join(" "));
    }
    println!("{}", out.join("\n"));
}
