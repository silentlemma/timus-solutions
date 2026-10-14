use std::io::{self, Read};

const SIZE: usize = 8;

struct Board {
    jumps: Vec<Vec<(usize, usize)>>, // the jumped and the landing squares, square by square
    total: u32,
    best: u32,
}

impl Board {
    // black and white hold the pieces still on the board, the mover excluded,
    // removed counts the whites taken away so far and taken the captured blacks
    fn dfs(&mut self, square: usize, black: u64, white: u64, removed: u32, taken: u32) {
        // every black not captured is taken away
        self.best = self.best.min(removed + self.total - taken);
        for k in 0..self.jumps[square].len() {
            let (mid, to) = self.jumps[square][k];
            if black >> mid & 1 == 0 {
                continue;
            }
            // a black in the way is taken away, uncaptured
            let nb = black & !(1u64 << mid) & !(1u64 << to);
            let (mut nw, mut cost) = (white, removed);
            if nw >> to & 1 == 1 {
                nw &= !(1u64 << to); // a white in the way costs one more
                cost += 1;
            }
            self.dfs(to, nb, nw, cost, taken + 1);
        }
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    // square (x, y), both from 0, is bit x * SIZE + y; the first input line is y = 7
    let (mut whites, mut blacks) = (0u64, 0u64);
    for (r, line) in input.split_ascii_whitespace().take(SIZE).enumerate() {
        for (x, ch) in line.bytes().enumerate() {
            let bit = 1u64 << (x * SIZE + SIZE - 1 - r);
            match ch {
                b'W' => whites |= bit,
                b'B' => blacks |= bit,
                _ => {}
            }
        }
    }
    // only squares off the edge can be jumped, so the landing stays on the board
    let mut jumps = vec![Vec::new(); SIZE * SIZE];
    for x in 0..SIZE as i32 {
        for y in 0..SIZE as i32 {
            for (dx, dy) in [(-1, -1), (-1, 1), (1, -1), (1, 1)] {
                let (tx, ty) = (x + 2 * dx, y + 2 * dy);
                if (0..SIZE as i32).contains(&tx) && (0..SIZE as i32).contains(&ty) {
                    let mid = ((x + dx) * SIZE as i32 + y + dy) as usize;
                    jumps[(x * SIZE as i32 + y) as usize]
                        .push((mid, (tx * SIZE as i32 + ty) as usize));
                }
            }
        }
    }
    let total = blacks.count_ones();
    // removing every black always wins
    let mut board = Board {
        jumps,
        total,
        best: total,
    };
    for s in 0..SIZE * SIZE {
        if whites >> s & 1 == 1 {
            board.dfs(s, blacks, whites & !(1u64 << s), 0, 0);
        }
    }
    println!("{}", board.best);
}
