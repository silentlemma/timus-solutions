use std::io::{self, Read};

struct Wall {
    n: i64,
    h: i64,
    d: i64,
    lefts: Vec<i64>,
}

impl Wall {
    // the place of a left end on the line from start, if it has one
    fn spot(&self, value: i64, start: i64) -> Option<usize> {
        let diff = value - start;
        if diff % self.d != 0 {
            return None;
        }
        let step = diff / self.d;
        if step >= 0 && step < self.n {
            Some(step as usize)
        } else {
            None
        }
    }

    // the places of strip k unturned and turned
    fn choices(&self, k: usize, start: i64) -> (Option<usize>, Option<usize>) {
        let x = self.lefts[k];
        let (a, b) = if self.d != 0 {
            (self.spot(x, start), self.spot(self.h - self.d - x, start))
        } else {
            // with a flat line every strip keeps its own place in the order
            ((x == start).then(|| k), (self.h - x == start).then(|| k))
        };
        (a, if b == a { None } else { b })
    }

    // the strips in order, signed when turned over, if their left ends can be
    // start, start + d, ..., start + (n - 1) d
    fn arrange(&self, start: i64) -> Option<Vec<i64>> {
        let mut place = vec![0i64; self.lefts.len()];
        let mut flexible = Vec::new();
        for k in 0..self.lefts.len() {
            let label = k as i64 + 1;
            match self.choices(k, start) {
                (None, None) => return None,
                (Some(_), Some(_)) => flexible.push(k),
                (Some(step), None) | (None, Some(step)) => {
                    if place[step] != 0 {
                        return None;
                    }
                    let unturned = self.choices(k, start).0.is_some();
                    place[step] = if unturned { label } else { -label };
                }
            }
        }
        // a strip that fits two places pairs place i with place K - i, so only
        // strips of the same pair compete once the strips with one choice are in
        for k in flexible {
            let label = k as i64 + 1;
            if let (Some(a), Some(b)) = self.choices(k, start) {
                if place[a] == 0 {
                    place[a] = label;
                } else if place[b] == 0 {
                    place[b] = -label;
                } else {
                    return None;
                }
            }
        }
        Some(place)
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_ascii_whitespace().map(|w| w.parse::<i64>().unwrap());
    let mut next = || words.next().unwrap();
    let (h, n) = (next(), next());
    let mut lefts = Vec::new();
    let mut rights = Vec::new();
    for _ in 0..n {
        lefts.push(next());
        rights.push(next());
    }
    // turning a strip over keeps its slope, so all slopes must be equal; the
    // left end x of a strip turns into h - d - x
    let d = rights[0] - lefts[0];
    if lefts.iter().zip(&rights).any(|(l, r)| r - l != d) {
        println!("0");
        return;
    }
    let mut starts = vec![lefts[0], h - lefts[0]];
    if d != 0 {
        let ends: Vec<i64> = lefts.iter().flat_map(|&x| [x, h - d - x]).collect();
        let (low, high) = (*ends.iter().min().unwrap(), *ends.iter().max().unwrap());
        // the strip with the extreme end either starts the line or, turned,
        // ends it
        let (first, last) = if d > 0 { (low, high) } else { (high, low) };
        starts = vec![first, last - (n - 1) * d];
    }
    let wall = Wall { n, h, d, lefts };
    for start in starts {
        if let Some(place) = wall.arrange(start) {
            let names: Vec<String> = place.iter().map(|v| v.to_string()).collect();
            println!("{}", names.join(" "));
            return;
        }
    }
    println!("0");
}
