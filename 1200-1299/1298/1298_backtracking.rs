use std::io::{self, Read};

const MOVES: [(i32, i32); 8] = [
    (1, 2),
    (2, 1),
    (2, -1),
    (1, -2),
    (-1, -2),
    (-2, -1),
    (-2, 1),
    (-1, 2),
];

struct Board {
    n: i32,
    seen: Vec<Vec<bool>>,
    path: Vec<(i32, i32)>,
}

impl Board {
    fn free(&self, c: i32, r: i32) -> Vec<(i32, i32)> {
        let n = self.n;
        MOVES
            .iter()
            .map(|&(dc, dr)| (c + dc, r + dr))
            .filter(|&(x, y)| x >= 0 && x < n && y >= 0 && y < n)
            .filter(|&(x, y)| !self.seen[x as usize][y as usize])
            .collect()
    }

    fn tour(&mut self, c: i32, r: i32) -> bool {
        self.seen[c as usize][r as usize] = true;
        self.path.push((c, r));
        if self.path.len() as i32 == self.n * self.n {
            return true;
        }
        // Warnsdorff's rule: try first the squares with the fewest onward
        // moves, and the search still backtracks, so it is exact
        let mut next = self.free(c, r);
        next.sort_by_key(|&(x, y)| self.free(x, y).len());
        for (x, y) in next {
            if self.tour(x, y) {
                return true;
            }
        }
        self.seen[c as usize][r as usize] = false;
        self.path.pop();
        false
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let n: i32 = input.trim().parse().unwrap();
    let mut board = Board {
        n,
        seen: vec![vec![false; n as usize]; n as usize],
        path: Vec::new(),
    };
    let found = (0..n).any(|c| (0..n).any(|r| board.tour(c, r)));
    if !found {
        println!("IMPOSSIBLE");
        return;
    }
    let mut out = String::new();
    for &(c, r) in &board.path {
        out.push((b'a' + c as u8) as char);
        out.push_str(&format!("{}\n", r + 1));
    }
    print!("{}", out);
}
