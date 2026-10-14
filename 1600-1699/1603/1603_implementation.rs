use std::collections::HashSet;
use std::fmt::Write as _;
use std::io::{self, Read};

const SIDE: usize = 4;
const CELLS: usize = SIDE * SIDE;
const LETTERS: usize = 26;

struct Search<'a> {
    grid: &'a [u8],
    word: &'a [u8],
    near: &'a [Vec<usize>],
    dead: HashSet<usize>, // (visited cells, last cell) that cannot finish the word
}

impl Search<'_> {
    /// Continues from cell, which holds word[i - 1]; mask is every cell used so far.
    fn walk(&mut self, cell: usize, mask: usize, i: usize) -> bool {
        if i == self.word.len() {
            return true;
        }
        let key = mask * CELLS + cell;
        if self.dead.contains(&key) {
            return false;
        }
        for k in 0..self.near[cell].len() {
            let next = self.near[cell][k];
            if mask >> next & 1 == 0
                && self.grid[next] == self.word[i]
                && self.walk(next, mask | 1 << next, i + 1)
            {
                return true;
            }
        }
        self.dead.insert(key);
        false
    }
}

fn found(grid: &[u8], word: &[u8], near: &[Vec<usize>]) -> bool {
    let (mut have, mut need) = ([0; LETTERS], [0; LETTERS]);
    for &c in grid {
        have[(c - b'a') as usize] += 1;
    }
    for &c in word {
        let i = (c - b'a') as usize;
        need[i] += 1;
        if need[i] > have[i] {
            return false;
        }
    }
    let mut search = Search {
        grid,
        word,
        near,
        dead: HashSet::new(),
    };
    (0..CELLS).any(|c| grid[c] == word[0] && search.walk(c, 1 << c, 1))
}

fn main() {
    let mut s = String::new();
    io::stdin().read_to_string(&mut s).unwrap();
    let mut it = s.split_ascii_whitespace();
    let grid: Vec<u8> = (0..SIDE)
        .flat_map(|_| it.next().unwrap().bytes().collect::<Vec<_>>())
        .collect();
    let near: Vec<Vec<usize>> = (0..CELLS)
        .map(|c| {
            let (r, col) = (c / SIDE, c % SIDE);
            let mut list = Vec::new();
            if r > 0 {
                list.push(c - SIDE);
            }
            if r + 1 < SIDE {
                list.push(c + SIDE);
            }
            if col > 0 {
                list.push(c - 1);
            }
            if col + 1 < SIDE {
                list.push(c + 1);
            }
            list
        })
        .collect();
    let n: usize = it.next().unwrap().parse().unwrap();
    let mut out = String::new();
    for _ in 0..n {
        let word = it.next().unwrap();
        let answer = if found(&grid, word.as_bytes(), &near) {
            "YES"
        } else {
            "NO"
        };
        writeln!(out, "{}: {}", word, answer).unwrap();
    }
    print!("{}", out);
}
