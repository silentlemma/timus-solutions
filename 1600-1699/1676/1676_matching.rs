use std::io::{self, Read};

struct Board {
    m: usize,
    beats: Vec<Vec<bool>>, // beats[i][j] when fighter j beats monster i
    owner: Vec<Option<usize>>,
    matched: Vec<usize>,
    seen: Vec<bool>,
}

impl Board {
    /// Kuhn's augmenting search from monster u.
    fn augment(&mut self, u: usize) -> bool {
        for j in 0..self.m {
            if self.beats[u][j] && !self.seen[j] {
                self.seen[j] = true;
                let free = match self.owner[j] {
                    None => true,
                    Some(k) => self.augment(k),
                };
                if free {
                    self.owner[j] = Some(u);
                    self.matched[u] = j;
                    return true;
                }
            }
        }
        false
    }
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut words = text.split_ascii_whitespace();
    let n: usize = words.next().unwrap().parse().unwrap();
    let m: usize = words.next().unwrap().parse().unwrap();
    let cells: Vec<u8> = words.flat_map(|w| w.bytes()).collect();
    let beats: Vec<Vec<bool>> =
        (0..n).map(|i| cells[i * m..(i + 1) * m].iter().map(|&c| c == b'1').collect()).collect();
    let mut board = Board { m, beats, owner: vec![None; m], matched: vec![0; n], seen: vec![] };
    let mut out = String::new();
    for i in 0..n {
        board.seen = vec![false; m];
        if !board.augment(i) {
            // some monster cannot be beaten in any assignment
            let row = "1".repeat(m) + "\n";
            print!("{}", row.repeat(n));
            return;
        }
    }
    // i may take fighter j if j is free or its own, or if j's monster k moves on:
    // with k -> k2 when k can take k2's fighter, k reaches i (closing a cycle)
    // or reaches a monster (k included) that some free fighter beats
    let mut next = vec![Vec::new(); n];
    let mut loose = vec![false; n];
    for k in 0..n {
        for j in 0..m {
            if board.beats[k][j] {
                match board.owner[j] {
                    None => loose[k] = true,
                    Some(k2) if k2 != k => next[k].push(k2),
                    _ => {}
                }
            }
        }
    }
    let mut reach = vec![vec![false; n]; n];
    let mut helped = vec![false; n];
    for k in 0..n {
        let mut queue = vec![k];
        let mut h = 0;
        while h < queue.len() {
            for &k2 in &next[queue[h]] {
                if !reach[k][k2] {
                    reach[k][k2] = true;
                    queue.push(k2);
                }
            }
            h += 1;
        }
        helped[k] = loose[k] || (0..n).any(|x| reach[k][x] && loose[x]);
    }
    for i in 0..n {
        for j in 0..m {
            let ok = board.beats[i][j]
                && match board.owner[j] {
                    None => true,
                    Some(k) => board.matched[i] == j || helped[k] || reach[k][i],
                };
            out.push(if ok { '0' } else { '1' });
        }
        out.push('\n');
    }
    print!("{}", out);
}
