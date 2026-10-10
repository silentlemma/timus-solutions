use std::io::{self, Read};

struct Balconies {
    monsters: Vec<u32>,
    volleys: Vec<usize>,
    memo: Vec<Option<u32>>,
}

impl Balconies {
    fn alive(&self, mask: usize) -> u32 {
        (0..self.monsters.len())
            .filter(|&i| mask >> i & 1 == 1)
            .map(|i| self.monsters[i])
            .sum()
    }

    // the least damage still to come with these balconies occupied; the
    // monsters left after each volley fire once
    fn damage(&mut self, mask: usize) -> u32 {
        if mask == 0 {
            return 0;
        }
        if let Some(d) = self.memo[mask] {
            return d;
        }
        let mut best = u32::MAX;
        for k in 0..self.volleys.len() {
            let v = self.volleys[k];
            if mask & v != 0 {
                let rest = mask & !v;
                best = best.min(self.alive(rest) + self.damage(rest));
            }
        }
        self.memo[mask] = Some(best);
        best
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tok = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<u32>().unwrap());
    let n = tok.next().unwrap() as usize;
    let monsters: Vec<u32> = tok.take(n).collect();
    // a volley at i clears balconies i - 1, i and i + 1 around the circle
    let volleys = (0..n)
        .map(|i| 1 << ((i + n - 1) % n) | 1 << i | 1 << ((i + 1) % n))
        .collect();
    let mut b = Balconies {
        monsters,
        volleys,
        memo: vec![None; 1 << n],
    };
    println!("{}", b.damage((1 << n) - 1));
}
