use std::io::{self, Read};

// a cost is pegs * PEG + inches cut: fewer pegs first, then less cutting
const PEG: i64 = 1_000_000;

#[derive(Clone, Copy)]
struct Shelf {
    y: i64,
    left: i64,
    length: i64,
    a: i64,
    b: i64,
}

// cheapest way to get a shelf out of the open strip (lo, hi) of the tome,
// keeping its plank inside the niche [0, width]
fn clear(s: &Shelf, lo: i64, hi: i64, width: i64) -> i64 {
    if s.left + s.length <= lo || s.left >= hi {
        return 0;
    }
    let mut best = 2 * PEG + s.length;
    for (start, end) in [(0, lo), (hi, width)] {
        // pegs stay: a plank of length t in [start, end] over both pegs with
        // its middle between them exists for b - a <= t <= this bound
        if start <= s.a && s.b <= end {
            let longest = s
                .length
                .min(2 * (s.b - start))
                .min(end - start)
                .min(2 * (end - s.a));
            if longest >= s.b - s.a {
                best = best.min(s.length - longest);
            }
        }
        // one peg moves anywhere, so only the kept peg and the room matter
        let kept = (start <= s.a && s.a <= end) || (start <= s.b && s.b <= end);
        if end > start && kept {
            best = best.min(PEG + (s.length - (end - start)).max(0));
        }
    }
    best
}

// cost of making a shelf hold the tome over [x, x + tome], if possible
fn carry(s: &Shelf, x: i64, tome: i64, width: i64) -> Option<i64> {
    if s.length < tome {
        return None;
    }
    // pegs stay: limits on the new left end, doubled to stay in integers
    let low = 0
        .max(2 * (s.b - s.length))
        .max(2 * s.a - s.length)
        .max(2 * (x + tome - s.length));
    let high = (2 * s.a)
        .min(2 * x)
        .min(2 * s.b - s.length)
        .min(2 * (width - s.length));
    if low <= high {
        return Some(0);
    }
    // one peg moves: the plank only has to reach over the tome and the peg
    // that stays
    if [s.a, s.b]
        .iter()
        .any(|&p| (x + tome).max(p) - x.min(p) <= s.length)
    {
        return Some(PEG);
    }
    None
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<i64>().unwrap());
    let mut next = || it.next().unwrap();
    let (width, height, tome_w, tome_h) = (next(), next(), next(), next());
    let n = next() as usize;
    let mut shelves: Vec<Shelf> = (0..n)
        .map(|_| {
            let (y, left, length) = (next(), next(), next());
            let (x1, x2) = (next(), next());
            Shelf {
                y,
                left,
                length,
                a: left + x1,
                b: left + x2,
            }
        })
        .collect();
    shelves.sort_by_key(|s| s.y);
    let spots = (width - tome_w + 1) as usize;
    // prefix[k][x]: total cost of clearing the strip at x from the k lowest
    // shelves
    let mut prefix = vec![vec![0i64; spots]];
    for s in &shelves {
        let row: Vec<i64> = (0..spots)
            .map(|x| prefix.last().unwrap()[x] + clear(s, x as i64, x as i64 + tome_w, width))
            .collect();
        prefix.push(row);
    }
    let mut best: Option<i64> = None;
    for (i, s) in shelves.iter().enumerate() {
        if s.y + tome_h > height {
            continue;
        }
        // the shelves strictly between the tome bottom and top are in the way
        let mut top = i + 1;
        while top < n && shelves[top].y < s.y + tome_h {
            top += 1;
        }
        for x in 0..spots {
            if let Some(base) = carry(s, x as i64, tome_w, width) {
                let total = base + prefix[top][x] - prefix[i + 1][x];
                if best.map_or(true, |b| total < b) {
                    best = Some(total);
                }
            }
        }
    }
    let best = best.unwrap();
    println!("{} {}", best / PEG, best % PEG);
}
