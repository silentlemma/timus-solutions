use std::io::{self, Read};

struct Painting {
    n: usize,
    grid: Vec<Vec<u8>>,
    black: Vec<Vec<usize>>, // black[i][j]: black cells among the first j of row i
}

impl Painting {
    // Black cells of row i in the columns from lo up to end, end excluded.
    fn ones(&self, i: usize, lo: usize, end: usize) -> usize {
        self.black[i][end] - self.black[i][lo]
    }

    fn fits(&self, ci: usize, cj: usize, r: usize) -> bool {
        // row ci + d: |d| black cells, a white run of 2(r - |d|) + 1, |d| black
        for i in ci - r..=ci + r {
            let side = i.abs_diff(ci);
            let inner = r - side;
            let (lo, hi) = (cj - inner, cj + inner + 1);
            if self.ones(i, cj - r, lo) != side || self.ones(i, hi, cj + r + 1) != side {
                return false;
            }
            if self.ones(i, lo, hi) != 0 {
                return false;
            }
        }
        true
    }

    fn largest(&self) -> usize {
        let n = self.n;
        // the white square needs a cell on every side of the centre, so r >= 1
        for r in (1..=(n.max(1) - 1) / 2).rev() {
            for ci in r..n - r {
                for cj in r..n - r {
                    // quick tests first: a white centre and tip, a black corner
                    let g = &self.grid;
                    if g[ci][cj] == 1 || g[ci - r][cj] == 1 || g[ci - r][cj - r] == 0 {
                        continue;
                    }
                    if self.fits(ci, cj, r) {
                        return 2 * r + 1;
                    }
                }
            }
        }
        0
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_ascii_whitespace();
    let mut out = String::new();
    loop {
        let n: usize = tokens.next().unwrap().parse().unwrap();
        if n == 0 {
            break;
        }
        // the cells may come with or without spaces between them
        let mut cells = Vec::with_capacity(n * n);
        while cells.len() < n * n {
            cells.extend(tokens.next().unwrap().bytes().map(|c| c - b'0'));
        }
        let grid: Vec<Vec<u8>> = cells.chunks(n).map(|row| row.to_vec()).collect();
        let black = grid
            .iter()
            .map(|row| {
                let mut acc = vec![0];
                for &v in row {
                    acc.push(acc.last().unwrap() + v as usize);
                }
                acc
            })
            .collect();
        let best = Painting { n, grid, black }.largest();
        if best > 0 {
            out += &format!("{}\n", best);
        } else {
            out += "No solution\n";
        }
    }
    print!("{}", out);
}
