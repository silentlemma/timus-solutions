use std::io::{self, Read};

// no row is longer than all the ships together: 99 * 100
const MAX_SUM: usize = 10000;
const BITS: usize = 64;
const WORDS: usize = (MAX_SUM + BITS - 1) / BITS;

type Sums = Vec<u64>;

fn has(s: &Sums, v: usize) -> bool {
    s[v / BITS] >> (v % BITS) & 1 == 1
}

// s | s << by
fn shift_or(s: &Sums, by: usize) -> Sums {
    let mut out = s.clone();
    let (w, b) = (by / BITS, by % BITS);
    for i in (w..WORDS).rev() {
        let mut v = s[i - w] << b;
        if b > 0 && i > w {
            v |= s[i - w - 1] >> (BITS - b);
        }
        out[i] |= v;
    }
    out
}

struct Fleet {
    ships: Vec<usize>,
    rows: Vec<usize>,
    order: Vec<usize>,
    owner: Vec<Option<usize>>,
}

impl Fleet {
    fn fill(&mut self, pos: usize) -> bool {
        let free: Vec<usize> = (0..self.ships.len())
            .filter(|&i| self.owner[i].is_none())
            .collect();
        let row = self.order[pos];
        if pos == self.rows.len() - 1 {
            // the last row takes every ship that is left
            if free.iter().map(|&i| self.ships[i]).sum::<usize>() != self.rows[row] {
                return false;
            }
            for &i in &free {
                self.owner[i] = Some(row);
            }
            return true;
        }
        // reach[k]: the sums that the free ships from k on can make
        let mut reach = vec![vec![0u64; WORDS]; free.len() + 1];
        reach[free.len()][0] = 1;
        for k in (0..free.len()).rev() {
            reach[k] = shift_or(&reach[k + 1], self.ships[free[k]]);
        }
        self.pick(pos, &free, &reach, 0, self.rows[row])
    }

    fn pick(&mut self, pos: usize, free: &[usize], reach: &[Sums], k: usize, need: usize) -> bool {
        if need == 0 {
            return self.fill(pos + 1);
        }
        if !has(&reach[k], need) {
            return false;
        }
        let mut last = None;
        for j in k..free.len() {
            let length = self.ships[free[j]];
            // equal ships are interchangeable: try each length once per place
            if last == Some(length) || length > need || !has(&reach[j + 1], need - length) {
                continue;
            }
            last = Some(length);
            self.owner[free[j]] = Some(self.order[pos]);
            if self.pick(pos, free, reach, j + 1, need - length) {
                return true;
            }
            self.owner[free[j]] = None;
        }
        false
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tok = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<usize>().unwrap());
    let (n, m) = (tok.next().unwrap(), tok.next().unwrap());
    let mut ships: Vec<usize> = tok.by_ref().take(n).collect();
    ships.sort_unstable_by(|a, b| b.cmp(a));
    let rows: Vec<usize> = tok.take(m).collect();
    // the shortest rows first: they have the fewest ways to be filled
    let mut order: Vec<usize> = (0..m).collect();
    order.sort_by_key(|&r| rows[r]);
    let mut fleet = Fleet {
        ships,
        rows,
        order,
        owner: vec![None; n],
    };
    fleet.fill(0);
    let mut out = String::new();
    for r in 0..m {
        let row: Vec<String> = (0..n)
            .filter(|&i| fleet.owner[i] == Some(r))
            .map(|i| fleet.ships[i].to_string())
            .collect();
        out.push_str(&format!("{}\n{}\n", row.len(), row.join(" ")));
    }
    print!("{}", out);
}
