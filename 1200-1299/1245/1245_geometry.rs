use std::io::{self, Read};

const SIDE: i64 = 100;
const SPOT: usize = 3;

#[derive(Clone, Copy)]
struct Box {
    lo: i64,
    hi: i64,
    lo2: i64,
    hi2: i64,
}

impl Box {
    fn grow(self, b: Box) -> Box {
        Box {
            lo: self.lo.min(b.lo),
            hi: self.hi.max(b.hi),
            lo2: self.lo2.min(b.lo2),
            hi2: self.hi2.max(b.hi2),
        }
    }

    // area of the smallest picture holding the box, at least 100 by 100
    fn area(self) -> i64 {
        (self.hi - self.lo).max(SIDE) * (self.hi2 - self.lo2).max(SIDE)
    }
}

// sorted by their low edge on the first axis, a prefix and the rest can
// hang apart exactly when the prefix ends no later than the rest begins
fn best(mut spots: Vec<Box>) -> i64 {
    spots.sort_by_key(|b| b.lo);
    let n = spots.len();
    let mut suffix = spots.clone();
    for i in (0..n - 1).rev() {
        suffix[i] = spots[i].grow(suffix[i + 1]);
    }
    let mut result = suffix[0].area();
    let mut prefix = spots[0];
    for k in 1..n {
        if prefix.hi <= spots[k].lo {
            result = result.min(prefix.area() + suffix[k].area());
        }
        prefix = prefix.grow(spots[k]);
    }
    result
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<i64> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let n = v[0] as usize;
    // a picture must hold each spot whole, so it must hold its bounding square
    let (mut across, mut down) = (Vec::with_capacity(n), Vec::with_capacity(n));
    for s in v[1..].chunks(SPOT) {
        let (r, x, y) = (s[0], s[1], s[2]);
        across.push(Box {
            lo: x - r,
            hi: x + r,
            lo2: y - r,
            hi2: y + r,
        });
        down.push(Box {
            lo: y - r,
            hi: y + r,
            lo2: x - r,
            hi2: x + r,
        });
    }
    // two pictures that do not overlap are split by a vertical or a
    // horizontal line, and each can grow to 100 mm away from that line
    println!("{}", best(across).min(best(down)));
}
