use std::io::{self, BufWriter, Read, Write};

const SIDE: usize = 4;
const CELLS: usize = SIDE * SIDE;
const LETTERS: usize = 26;
const COLORS: usize = 2;
const STATE_BITS: usize = CELLS - 1;
const BYTE_BITS: usize = u8::BITS as usize;
const MEMO_BYTES: usize = CELLS * (1 << STATE_BITS) / BYTE_BITS;

struct Search {
    positions: [u32; LETTERS],
    colors: [u32; COLORS],
    near: [u32; CELLS],
    allowed: [u32; CELLS],
    capacity: [[u8; LETTERS]; COLORS],
    failed: Vec<u8>,
    word: Vec<u8>,
}

impl Search {
    fn walk(&mut self, cell: usize, used: u32, index: usize) -> bool {
        if index + 1 == self.word.len() {
            return true;
        }
        let compressed = (used & ((1u32 << cell) - 1)) | ((used >> (cell + 1)) << cell);
        let key = (cell << STATE_BITS) | compressed as usize;
        let slot = key / BYTE_BITS;
        let flag = 1u8 << (key % BYTE_BITS);
        if self.failed[slot] & flag != 0 {
            return false;
        }
        let mut options = self.near[cell] & self.allowed[index + 1] & !used;
        while options != 0 {
            let bit = options & options.wrapping_neg();
            if self.walk(bit.trailing_zeros() as usize, used | bit, index + 1) {
                return true;
            }
            options -= bit;
        }
        self.failed[slot] |= flag;
        false
    }

    fn found(&mut self, original: &str) -> bool {
        self.word.clear();
        self.word.extend_from_slice(original.as_bytes());
        let length = self.word.len();
        if self.positions[(self.word[0] - b'a') as usize].count_ones()
            > self.positions[(self.word[length - 1] - b'a') as usize].count_ones()
        {
            self.word.reverse();
        }
        let mut needed = [[0u8; LETTERS]; COLORS];
        for (i, &letter) in self.word.iter().enumerate() {
            needed[i % COLORS][(letter - b'a') as usize] += 1;
        }
        let mut starts = 0;
        for color in 0..COLORS {
            if (0..LETTERS).all(|letter| {
                needed[0][letter] <= self.capacity[color][letter]
                    && needed[1][letter] <= self.capacity[color ^ 1][letter]
            }) {
                starts |= self.colors[color];
            }
        }
        if starts == 0 {
            return false;
        }
        self.allowed[length - 1] = self.positions[(self.word[length - 1] - b'a') as usize];
        for i in (0..length - 1).rev() {
            self.allowed[i] = 0;
            let mut cells = self.positions[(self.word[i] - b'a') as usize];
            while cells != 0 {
                let bit = cells & cells.wrapping_neg();
                let cell = bit.trailing_zeros() as usize;
                if self.near[cell] & self.allowed[i + 1] != 0 {
                    self.allowed[i] |= bit;
                }
                cells -= bit;
            }
        }
        starts &= self.allowed[0];
        if starts == 0 {
            return false;
        }
        self.failed.fill(0);
        while starts != 0 {
            let bit = starts & starts.wrapping_neg();
            if self.walk(bit.trailing_zeros() as usize, bit, 0) {
                return true;
            }
            starts -= bit;
        }
        false
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let grid: Vec<u8> = (0..SIDE).flat_map(|_| it.next().unwrap().bytes()).collect();
    let mut search = Search {
        positions: [0; LETTERS],
        colors: [0; COLORS],
        near: [0; CELLS],
        allowed: [0; CELLS],
        capacity: [[0; LETTERS]; COLORS],
        failed: vec![0; MEMO_BYTES],
        word: Vec::with_capacity(CELLS),
    };
    for (cell, &letter) in grid.iter().enumerate() {
        let bit = 1u32 << cell;
        search.positions[(letter - b'a') as usize] |= bit;
        let (row, column) = (cell / SIDE, cell % SIDE);
        search.colors[(row + column) % COLORS] |= bit;
        if row > 0 {
            search.near[cell] |= 1u32 << (cell - SIDE);
        }
        if row + 1 < SIDE {
            search.near[cell] |= 1u32 << (cell + SIDE);
        }
        if column > 0 {
            search.near[cell] |= 1u32 << (cell - 1);
        }
        if column + 1 < SIDE {
            search.near[cell] |= 1u32 << (cell + 1);
        }
    }
    for color in 0..COLORS {
        for letter in 0..LETTERS {
            search.capacity[color][letter] =
                (search.positions[letter] & search.colors[color]).count_ones() as u8;
        }
    }
    let n: usize = it.next().unwrap().parse().unwrap();
    let mut cache: Vec<(&str, bool)> = Vec::with_capacity(n);
    let stdout = io::stdout();
    let mut out = BufWriter::new(stdout.lock());
    for _ in 0..n {
        let original = it.next().unwrap();
        let answer = if let Some((_, answer)) = cache.iter().find(|(word, _)| *word == original) {
            *answer
        } else {
            search.found(original)
        };
        cache.push((original, answer));
        writeln!(out, "{}: {}", original, if answer { "YES" } else { "NO" }).unwrap();
    }
}
