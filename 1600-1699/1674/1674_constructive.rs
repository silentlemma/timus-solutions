use std::io::{self, Read};

const BLOCK: usize = 4; // rows or columns added at a time
const SMALLEST: usize = 4; // boards with a shorter side have no tour, apart from 2 x 2
const BOTTOM: usize = SMALLEST - 1; // the last row of a strip

const NO_TOUR: (usize, usize) = (5, 5); // the one board with both sides at least 4 and no tour
const ODD_BASE: (usize, usize) = (5, 9); // the base when both sides are of the form 4k + 1

type Cell = (usize, usize);

/// Closed tours of small boards, as flat (row, column) lists ending at the start,
/// printed by 1674_constructive_table.py.
const BASES: [((usize, usize), &[usize]); 6] = [
    ((5, 6), &[0, 0, 0, 1, 1, 2, 2, 2, 2, 3, 1, 3, 0, 2, 0, 3, 1, 4, 0, 4, 0, 5, 1, 5, 2, 4, 2, 5,
        3, 5, 3, 4, 4, 5, 4, 4, 3, 3, 4, 3, 4, 2, 3, 2, 4, 1, 4, 0, 3, 0, 3, 1, 2, 0, 2, 1, 1, 0, 1,
        1, 0, 0]),
    ((5, 7), &[0, 0, 0, 1, 1, 2, 2, 2, 2, 3, 1, 3, 0, 2, 0, 3, 1, 4, 0, 4, 0, 5, 1, 5, 0, 6, 1, 6,
        2, 5, 2, 6, 3, 6, 3, 5, 4, 6, 4, 5, 3, 4, 2, 4, 3, 3, 4, 4, 4, 3, 3, 2, 4, 2, 3, 1, 4, 1, 4,
        0, 3, 0, 2, 1, 2, 0, 1, 0, 1, 1, 0, 0]),
    ((6, 6), &[0, 0, 0, 1, 1, 2, 1, 3, 0, 2, 0, 3, 1, 4, 0, 4, 0, 5, 1, 5, 2, 4, 2, 5, 3, 5, 3, 4,
        2, 3, 2, 2, 3, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 4, 4, 3, 5, 3, 5, 2, 4, 2, 5, 1, 5, 0, 4, 0, 4,
        1, 3, 0, 3, 1, 2, 0, 2, 1, 1, 0, 1, 1, 0, 0]),
    ((6, 7), &[0, 0, 0, 1, 1, 2, 1, 3, 0, 2, 0, 3, 1, 4, 0, 4, 0, 5, 1, 5, 0, 6, 1, 6, 2, 5, 2, 4,
        3, 5, 2, 6, 3, 6, 4, 5, 4, 6, 5, 6, 5, 5, 4, 4, 5, 4, 4, 3, 3, 4, 2, 3, 2, 2, 3, 3, 3, 2, 4,
        2, 5, 3, 5, 2, 4, 1, 5, 1, 5, 0, 4, 0, 3, 1, 3, 0, 2, 0, 2, 1, 1, 0, 1, 1, 0, 0]),
    ((7, 7), &[0, 0, 0, 1, 1, 2, 1, 3, 0, 2, 0, 3, 1, 4, 0, 4, 0, 5, 1, 5, 0, 6, 1, 6, 2, 5, 2, 4,
        3, 5, 2, 6, 3, 6, 4, 5, 4, 6, 5, 6, 5, 5, 6, 6, 6, 5, 5, 4, 6, 4, 5, 3, 4, 4, 3, 4, 2, 3, 2,
        2, 3, 3, 3, 2, 4, 3, 4, 2, 5, 2, 6, 3, 6, 2, 5, 1, 6, 1, 6, 0, 5, 0, 4, 1, 4, 0, 3, 0, 3, 1,
        2, 0, 2, 1, 1, 0, 1, 1, 0, 0]),
    ((5, 9), &[0, 0, 0, 1, 1, 2, 2, 2, 2, 3, 1, 3, 0, 2, 0, 3, 1, 4, 2, 4, 2, 5, 1, 5, 0, 4, 0, 5,
        1, 6, 0, 6, 0, 7, 1, 7, 0, 8, 1, 8, 2, 7, 2, 8, 3, 8, 3, 7, 4, 8, 4, 7, 3, 6, 2, 6, 3, 5, 4,
        6, 4, 5, 3, 4, 4, 4, 3, 3, 4, 3, 4, 2, 3, 2, 4, 1, 4, 0, 3, 0, 3, 1, 2, 0, 2, 1, 1, 0, 1, 1,
        0, 0]),
];

/// A closed tour of the 4 x m board: along the top two rows in a zigzag, down
/// the right end, back along the bottom two rows, up the left end.
fn strip(m: usize) -> Vec<Cell> {
    let mut path = vec![(0, 0), (0, 1), (1, 1)];
    for c in 2..m - 1 {
        path.push((0, c));
        if c < m - 2 {
            path.push((1, c));
        }
    }
    path.extend([(0, m - 1), (1, m - 1), (1, m - 2), (2, m - 1), (BOTTOM, m - 1)]);
    for c in (2..m - 1).rev() {
        path.extend([(BOTTOM, c), (2, c)]);
    }
    path.extend([(BOTTOM, 1), (BOTTOM, 0), (2, 0), (2, 1), (1, 0), (0, 0)]);
    path
}

fn flip(path: Vec<Cell>) -> Vec<Cell> {
    path.into_iter().map(|(r, c)| (c, r)).collect()
}

fn base(n: usize, m: usize) -> Vec<Cell> {
    if n == SMALLEST {
        return strip(m);
    }
    if m == SMALLEST {
        return flip(strip(n));
    }
    let swapped = !BASES.iter().any(|(key, _)| *key == (n, m));
    let key = if swapped { (m, n) } else { (n, m) };
    let flat = BASES.iter().find(|(k, _)| *k == key).unwrap().1;
    let path: Vec<Cell> = flat.chunks(2).map(|p| (p[0], p[1])).collect();
    if swapped {
        flip(path)
    } else {
        path
    }
}

struct Picture {
    grid: Vec<Vec<u8>>,
}

impl Picture {
    /// Draw the move between cells a and b, or with ch = b' ' erase it.
    fn mark(&mut self, a: Cell, b: Cell, ch: u8) {
        let ch = if ch != 0 {
            ch
        } else if a.0 == b.0 {
            b'-'
        } else if a.1 == b.1 {
            b'|'
        } else if (b.0 > a.0) == (b.1 > a.1) {
            b'\\'
        } else {
            b'/'
        };
        self.grid[a.0 + b.0][a.1 + b.1] = ch;
    }

    fn draw(&mut self, path: &[Cell], dr: usize, dc: usize, swap: bool) {
        for w in path.windows(2) {
            let (a, b) = if swap { ((w[0].1, w[0].0), (w[1].1, w[1].0)) } else { (w[0], w[1]) };
            self.mark((a.0 + dr, a.1 + dc), (b.0 + dr, b.1 + dc), 0);
        }
    }
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let v: Vec<usize> = text.split_ascii_whitespace().map(|w| w.parse().unwrap()).collect();
    let (n, m) = (v[0], v[1]);
    let mut pic = Picture { grid: vec![vec![b' '; 2 * m - 1]; 2 * n - 1] };
    for r in 0..n {
        for c in 0..m {
            pic.grid[2 * r][2 * c] = b'o';
        }
    }
    if (n, m) == (2, 2) {
        pic.draw(&[(0, 0), (0, 1), (1, 1), (1, 0), (0, 0)], 0, 0, false);
    } else if n < SMALLEST || m < SMALLEST || (n, m) == NO_TOUR {
        println!("No");
        return;
    } else {
        // a base board whose sides leave multiples of 4; two sides of the
        // form 4k + 1 start from 5 x 9 instead, as 5 x 5 has no tour
        let mut bn = SMALLEST + (n - SMALLEST) % BLOCK;
        let mut bm = SMALLEST + (m - SMALLEST) % BLOCK;
        if n % BLOCK == 1 && m % BLOCK == 1 {
            (bn, bm) = if m >= ODD_BASE.1 { ODD_BASE } else { (ODD_BASE.1, ODD_BASE.0) };
        }
        pic.draw(&base(bn, bm), 0, 0, false);
        // each new 4-wide block has its own strip tour; three edges at the
        // seam are swapped for three others, which joins the two cycles
        let mut cur = bm;
        while cur < m {
            pic.draw(&strip(bn), 0, cur, true);
            pic.mark((0, cur - 1), (1, cur - 1), b' ');
            pic.mark((0, cur), (1, cur), b' ');
            pic.mark((2, cur), (1, cur + 1), b' ');
            pic.mark((0, cur - 1), (1, cur), 0);
            pic.mark((1, cur - 1), (2, cur), 0);
            pic.mark((0, cur), (1, cur + 1), 0);
            cur += BLOCK;
        }
        let mut cur = bn;
        while cur < n {
            pic.draw(&strip(m), cur, 0, false);
            pic.mark((cur - 1, 0), (cur - 1, 1), b' ');
            pic.mark((cur, 0), (cur, 1), b' ');
            pic.mark((cur, 2), (cur + 1, 1), b' ');
            pic.mark((cur - 1, 0), (cur, 1), 0);
            pic.mark((cur - 1, 1), (cur, 2), 0);
            pic.mark((cur, 0), (cur + 1, 1), 0);
            cur += BLOCK;
        }
    }
    let mut out = String::from("Yes\n");
    for row in &pic.grid {
        out.push_str(std::str::from_utf8(row).unwrap());
        out.push('\n');
    }
    print!("{}", out);
}
