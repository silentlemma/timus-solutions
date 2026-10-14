use std::collections::HashSet;
use std::io::{self, Read};
use std::ops::{Add, Div, Mul, Sub};

const MOST: usize = 6; // dots in one square
const FULL: usize = 4; // from four dots on, all corners of the inner square are used
const QUARTER: f64 = 0.25; // the inner square's corners are L / 4 from the centre

const SMALLEST: f64 = 1.0;
const LARGEST: f64 = 100.0;
const EPS: f64 = 2e-3; // the coordinates are given to 1e-4, and a fit spreads that error

#[derive(Clone, Copy, PartialEq)]
struct C(f64, f64);

impl Add for C {
    type Output = C;
    fn add(self, o: C) -> C {
        C(self.0 + o.0, self.1 + o.1)
    }
}

impl Sub for C {
    type Output = C;
    fn sub(self, o: C) -> C {
        C(self.0 - o.0, self.1 - o.1)
    }
}

impl Mul for C {
    type Output = C;
    fn mul(self, o: C) -> C {
        C(self.0 * o.0 - self.1 * o.1, self.0 * o.1 + self.1 * o.0)
    }
}

impl Div for C {
    type Output = C;
    fn div(self, o: C) -> C {
        let d = o.0 * o.0 + o.1 * o.1;
        C(
            (self.0 * o.0 + self.1 * o.1) / d,
            (self.1 * o.0 - self.0 * o.1) / d,
        )
    }
}

impl C {
    fn abs(self) -> f64 {
        self.0.hypot(self.1)
    }
}

// the dots of a square with k dots around (cx, 0), for L = 1, with the
// domino lying along the x axis
fn square(k: usize, cx: f64) -> Vec<C> {
    let q = QUARTER;
    let mut dots = Vec::new();
    if k >= 2 {
        dots.extend([C(-q, -q), C(q, q)]);
    }
    if k >= FULL {
        dots.extend([C(q, -q), C(-q, q)]);
    }
    if k == MOST {
        dots.push(C(0.0, -q)); // beside the long sides
        dots.push(C(0.0, q));
    }
    if k % 2 == 1 {
        dots.push(C(0.0, 0.0));
    }
    dots.iter().map(|&d| d + C(cx, 0.0)).collect()
}

// whether a similarity, maybe mirrored, with scale in the allowed range
// takes the template onto the given dots
fn fits(template: &[C], given: &[C]) -> bool {
    let g0 = given[0];
    let g1 = given.iter().copied().fold(g0, |f, g| {
        if (g - g0).abs() > (f - g0).abs() {
            g
        } else {
            f
        }
    });
    for mirror in [false, true] {
        let pts: Vec<C> = template
            .iter()
            .map(|&t| if mirror { C(t.0, -t.1) } else { t })
            .collect();
        for &a in &pts {
            for &b in &pts {
                if a == b {
                    continue;
                }
                let turn = (g1 - g0) / (b - a); // rotation times the scale L
                if turn.abs() < SMALLEST - EPS || turn.abs() > LARGEST + EPS {
                    continue;
                }
                let mut hit = HashSet::new();
                let ok = pts.iter().all(|&t| {
                    let image = g0 + (t - a) * turn;
                    let near = (0..given.len())
                        .min_by(|&i, &j| {
                            let (di, dj) = ((given[i] - image).abs(), (given[j] - image).abs());
                            di.partial_cmp(&dj).unwrap()
                        })
                        .unwrap();
                    hit.insert(near);
                    (given[near] - image).abs() <= EPS
                });
                if ok && hit.len() == given.len() {
                    return true;
                }
            }
        }
    }
    false
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<f64> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let n = v[0] as usize;
    let given: Vec<C> = (0..n).map(|i| C(v[1 + 2 * i], v[2 + 2 * i])).collect();
    let mut out = String::new();
    for a in 0..=MOST {
        if n < a || n - a < a || n - a > MOST {
            continue;
        }
        let b = n - a;
        let mut template = square(a, 0.0);
        template.extend(square(b, 1.0));
        if n == 1 || fits(&template, &given) {
            out += &format!("{} {}\n", a, b);
        }
    }
    print!("{}", out);
}
