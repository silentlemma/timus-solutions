use std::fmt::Write as _;
use std::io::{self, Read};

const WIDTH: usize = 50;
const HEIGHT: usize = 20;
const MIN_SIDE: usize = 2;
const EMPTY: u8 = b'.';
const UPPER_LEFT: u8 = 218;
const UPPER_RIGHT: u8 = 191;
const LOWER_LEFT: u8 = 192;
const LOWER_RIGHT: u8 = 217;
const VERTICAL: u8 = 179;
const HORIZONTAL: u8 = 196;

struct Picture {
    screen: [[u8; WIDTH]; HEIGHT],
    // a peeled cell is covered by a frame drawn later, so it may hold anything
    peeled: [[bool; WIDTH]; HEIGHT],
    left: usize,
}

impl Picture {
    fn fits(&self, x: usize, y: usize, c: u8, fresh: &mut usize) -> bool {
        if self.peeled[y][x] {
            return true;
        }
        if self.screen[y][x] != c {
            return false;
        }
        *fresh += 1;
        true
    }

    // the frame matches the picture where it is visible and shows something new
    fn frame_fits(&self, x: usize, y: usize, side: usize) -> bool {
        let last = side - 1;
        let mut fresh = 0;
        let corners = [
            (x, y, UPPER_LEFT),
            (x + last, y, UPPER_RIGHT),
            (x, y + last, LOWER_LEFT),
            (x + last, y + last, LOWER_RIGHT),
        ];
        if !corners
            .iter()
            .all(|&(cx, cy, c)| self.fits(cx, cy, c, &mut fresh))
        {
            return false;
        }
        for i in 1..last {
            let edges = [
                (x + i, y, HORIZONTAL),
                (x + i, y + last, HORIZONTAL),
                (x, y + i, VERTICAL),
                (x + last, y + i, VERTICAL),
            ];
            if !edges
                .iter()
                .all(|&(cx, cy, c)| self.fits(cx, cy, c, &mut fresh))
            {
                return false;
            }
        }
        fresh > 0
    }

    fn peel(&mut self, x: usize, y: usize, side: usize) {
        let last = side - 1;
        for i in 0..side {
            for (cx, cy) in [(x + i, y), (x + i, y + last), (x, y + i), (x + last, y + i)] {
                if !self.peeled[cy][cx] {
                    self.peeled[cy][cx] = true;
                    self.left -= 1;
                }
            }
        }
    }
}

fn main() {
    let mut data = Vec::new();
    io::stdin().read_to_end(&mut data).unwrap();
    let mut p = Picture {
        screen: [[EMPTY; WIDTH]; HEIGHT],
        peeled: [[false; WIDTH]; HEIGHT],
        left: 0,
    };
    let mut pos = 0;
    for y in 0..HEIGHT {
        for x in 0..WIDTH {
            if pos < data.len() && data[pos] != b'\n' && data[pos] != b'\r' {
                p.screen[y][x] = data[pos];
                pos += 1;
            }
            if p.screen[y][x] != EMPTY {
                p.left += 1;
            }
        }
        while pos < data.len() && data[pos] != b'\n' {
            pos += 1;
        }
        pos += 1;
    }

    // Undo the drawing: a frame that fits can be the last one drawn among the
    // remaining ones; its cells then may hold anything.
    let mut frames = Vec::new();
    while p.left > 0 {
        let before = p.left;
        for y in 0..HEIGHT {
            for x in 0..WIDTH {
                for side in MIN_SIDE..=(WIDTH - x).min(HEIGHT - y) {
                    if p.frame_fits(x, y, side) {
                        frames.push((x, y, side));
                        p.peel(x, y, side);
                    }
                }
            }
        }
        if p.left == before {
            break;
        }
    }

    let mut out = String::new();
    writeln!(out, "{}", frames.len()).unwrap();
    for &(x, y, side) in frames.iter().rev() {
        writeln!(out, "{} {} {}", x, y, side).unwrap();
    }
    print!("{}", out);
}
