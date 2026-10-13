use std::collections::HashMap;
use std::io::{self, Read};

const BLACK: u8 = 0; // results, better for white upwards
const DRAW: u8 = 1;
const WHITE: u8 = 2;
const SIZE: i32 = 8;
const SECOND: i32 = 6; // the black pawn may move two squares from rank 7
const DIAGONALS: [(i32, i32); 4] = [(1, 1), (1, -1), (-1, 1), (-1, -1)];

fn inside(f: i32, r: i32) -> bool {
    (0..SIZE).contains(&f) && (0..SIZE).contains(&r)
}

/// Can the bishop reach square (qf, qr) on an otherwise empty board?
fn sees(bf: i32, br: i32, qf: i32, qr: i32) -> bool {
    DIAGONALS.iter().any(|&(df, dr)| {
        let (mut f, mut r) = (bf + df, br + dr);
        while inside(f, r) {
            if (f, r) == (qf, qr) {
                return true;
            }
            f += df;
            r += dr;
        }
        false
    })
}

struct Game {
    memo: HashMap<(bool, i32, i32, i32, i32), u8>,
}

impl Game {
    fn white(&mut self, bf: i32, br: i32, pf: i32, pr: i32) -> u8 {
        if let Some(&v) = self.memo.get(&(true, bf, br, pf, pr)) {
            return v;
        }
        let mut best = BLACK;
        'search: for &(df, dr) in &DIAGONALS {
            let (mut f, mut r) = (bf + df, br + dr);
            while inside(f, r) {
                if (f, r) == (pf, pr) {
                    best = WHITE; // the bishop takes the pawn
                    break 'search;
                }
                best = best.max(self.black(f, r, pf, pr));
                f += df;
                r += dr;
            }
        }
        self.memo.insert((true, bf, br, pf, pr), best);
        best
    }

    fn black(&mut self, bf: i32, br: i32, pf: i32, pr: i32) -> u8 {
        if let Some(&v) = self.memo.get(&(false, bf, br, pf, pr)) {
            return v;
        }
        let mut options: Vec<u8> = Vec::new();
        if br == pr - 1 && (bf == pf - 1 || bf == pf + 1) {
            options.push(BLACK); // the pawn takes the bishop and cannot be stopped
        }
        if (bf, br) != (pf, pr - 1) {
            if pr - 1 == 0 {
                // a queen: white wins only by taking it at once
                options.push(if sees(bf, br, pf, 0) { WHITE } else { BLACK });
            } else {
                options.push(self.white(bf, br, pf, pr - 1));
                if pr == SECOND && (bf, br) != (pf, pr - 2) {
                    options.push(self.white(bf, br, pf, pr - 2));
                }
            }
        }
        let best = options.into_iter().min().unwrap_or(DRAW); // a blocked pawn is a draw
        self.memo.insert((false, bf, br, pf, pr), best);
        best
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let words: Vec<&[u8]> = input
        .split_ascii_whitespace()
        .map(|w| w.as_bytes())
        .collect();
    let square = |w: &[u8]| ((w[0] - b'a') as i32, (w[1] - b'1') as i32);
    let ((bf, br), (pf, pr)) = (square(words[0]), square(words[1]));
    let mut game = Game {
        memo: HashMap::new(),
    };
    let result = game.white(bf, br, pf, pr);
    println!("{}", ["BLACK", "DRAW", "WHITE"][result as usize]);
}
