use std::io::{self, Read};

const NINE: i64 = 9;
const CLASSES: usize = 4; // positions grouped by the signs of the two rules
const BOTH_UP: usize = 0;
const X_UP: usize = 1;
const Y_UP: usize = 2;
const BOTH_DOWN: usize = 3;

struct Combo<'a> {
    s: &'a [i64],
    wx: Vec<i64>,
    wy: Vec<i64>,
    cls: Vec<usize>,
    tail: Vec<i64>, // tail[k]: sum of wx from k on
    cnt: Vec<Vec<i64>>,
    px: Vec<i64>,
    py: Vec<i64>,
}

impl<'a> Combo<'a> {
    fn new(s: &'a [i64], wx: Vec<i64>, wy: Vec<i64>) -> Self {
        let n = s.len();
        let cls: Vec<usize> = (0..n)
            .map(|k| (if wx[k] > 0 { 0 } else { 2 }) + (if wy[k] > 0 { 0 } else { 1 }))
            .collect();
        let mut cnt = vec![vec![0i64; n + 1]; CLASSES];
        let (mut px, mut py) = (vec![0i64; n + 1], vec![0i64; n + 1]);
        for k in 0..n {
            for c in 0..CLASSES {
                cnt[c][k + 1] = cnt[c][k] + i64::from(cls[k] == c);
            }
            px[k + 1] = px[k] + wx[k] * s[k];
            py[k + 1] = py[k] + wy[k] * s[k];
        }
        let mut tail = vec![0i64; n + 1];
        for k in (0..n).rev() {
            tail[k] = tail[k + 1] + wx[k];
        }
        Combo {
            s,
            wx,
            wy,
            cls,
            tail,
            cnt,
            px,
            py,
        }
    }

    /// Digits before j give sums sx, sy; j in [lo_j, hi_j], free up to p,
    /// p at most 8, nines after p; t must balance wx, t + 1 must balance wy.
    fn feasible(&self, sx: i64, sy: i64, j: usize, p: usize, lo_j: i64, hi_j: i64) -> bool {
        let (a, b) = (-sx - NINE * self.tail[p + 1], -sy - self.wy[p]);
        let mut lo = [0i64; CLASSES];
        let mut hi = [0i64; CLASSES];
        for c in 0..CLASSES {
            hi[c] = NINE * (self.cnt[c][p + 1] - self.cnt[c][j]);
        }
        hi[self.cls[j]] += hi_j - NINE;
        lo[self.cls[j]] += lo_j;
        if p > j {
            hi[self.cls[p]] -= 1;
        }
        if (a + b) % 2 != 0 {
            return false;
        }
        let (u, v) = ((a + b) / 2, (a - b) / 2);
        lo[BOTH_UP] - hi[BOTH_DOWN] <= u
            && u <= hi[BOTH_UP] - lo[BOTH_DOWN]
            && lo[X_UP] - hi[Y_UP] <= v
            && v <= hi[X_UP] - lo[Y_UP]
    }

    /// t from s up to j, then d, then the smallest digits that still fit, then nines after p.
    fn build(&self, p: usize, j: usize, d: i64) -> Vec<i64> {
        let n = self.s.len();
        let mut t = vec![NINE; n];
        if j > p {
            // t keeps s up to p and has nines after it
            t[..=p].copy_from_slice(&self.s[..=p]);
            return t;
        }
        t[..j].copy_from_slice(&self.s[..j]);
        t[j] = d;
        let (mut sx, mut sy) = (self.px[j] + self.wx[j] * d, self.py[j] + self.wy[j] * d);
        for k in j + 1..=p {
            let mut x = 0;
            while !self.feasible(sx, sy, k, p, x, x) {
                x += 1;
            }
            t[k] = x;
            sx += self.wx[k] * x;
            sy += self.wy[k] * x;
        }
        t
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let s: Vec<i64> = input.trim().bytes().map(|c| (c - b'0') as i64).collect();
    let n = s.len();
    let half = n / 2;
    let rule_a: Vec<i64> = (0..n).map(|k| if k < half { 1 } else { -1 }).collect();
    let rule_b: Vec<i64> = (0..n).map(|k| if k % 2 == 0 { 1 } else { -1 }).collect();
    let rules = [rule_a, rule_b];
    // best: the first position where t leaves s (later is better), then the digit there
    let mut best: Option<(i64, i64, Vec<i64>)> = None;
    for x in &rules {
        for y in &rules {
            // the rule for t, then the rule for t + 1
            let c = Combo::new(&s, x.clone(), y.clone());
            for p in 0..n {
                let mut found: Option<(i64, i64, usize, i64)> = None;
                if s[p] < NINE
                    && c.px[p + 1] + NINE * c.tail[p + 1] == 0
                    && c.py[p + 1] + c.wy[p] == 0
                {
                    let dev = (p + 1..n).find(|&k| s[k] < NINE).unwrap_or(n);
                    found = Some((dev as i64, NINE, p + 1, 0));
                } else {
                    for q in (0..=p).rev() {
                        let top = if q == p { NINE - 1 } else { NINE };
                        if s[q] + 1 > top || !c.feasible(c.px[q], c.py[q], q, p, s[q] + 1, top) {
                            continue;
                        }
                        let mut d = s[q] + 1;
                        while !c.feasible(c.px[q], c.py[q], q, p, d, d) {
                            d += 1;
                        }
                        found = Some((q as i64, d, q, d));
                        break;
                    }
                }
                let Some((dev, digit, j, d)) = found else {
                    continue;
                };
                if let Some((bd, bg, _)) = &best {
                    if dev < *bd || (dev == *bd && digit > *bg) {
                        continue;
                    }
                }
                let t = c.build(p, j, d);
                let better = match &best {
                    None => true,
                    Some((bd, bg, bt)) => dev > *bd || digit < *bg || t < *bt,
                };
                if better {
                    best = Some((dev, digit, t));
                }
            }
        }
    }
    match best {
        None => println!("No solution"),
        Some((_, _, t)) => {
            let mut next = t.clone();
            let mut k = n - 1;
            while next[k] == NINE {
                next[k] = 0;
                k -= 1;
            }
            next[k] += 1;
            let a: String = t.iter().map(|&x| (b'0' + x as u8) as char).collect();
            let b: String = next.iter().map(|&x| (b'0' + x as u8) as char).collect();
            println!("{} {}", a, b);
        }
    }
}
