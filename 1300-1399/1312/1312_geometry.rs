use std::io::{self, Read};

const EPS: f64 = 1e-9; // relative to the size of the tray
const PLATES: usize = 3;

struct Tray {
    h: f64,
    w: f64,
    tol: f64,
    radii: [f64; PLATES],
    order: [usize; PLATES],
    pos: [(f64, f64); PLATES],
}

// centres of a circle touching circles (a, ra) and (b, rb) from outside,
// with ra and rb already increased by its radius
fn touching(a: (f64, f64), ra: f64, b: (f64, f64), rb: f64, out: &mut Vec<(f64, f64)>) {
    let (dx, dy) = (b.0 - a.0, b.1 - a.1);
    let d2 = dx * dx + dy * dy;
    if d2 == 0.0 {
        return;
    }
    let d = d2.sqrt();
    let x = (d2 + ra * ra - rb * rb) / (2.0 * d);
    let h2 = (ra - x) * (ra + x);
    if h2 < 0.0 {
        return;
    }
    let h = h2.sqrt();
    let (mx, my) = (a.0 + dx * x / d, a.1 + dy * x / d);
    out.push((mx - dy * h / d, my + dx * h / d));
    out.push((mx + dy * h / d, my - dx * h / d));
}

impl Tray {
    fn fits(&self, p: (f64, f64), r: f64) -> bool {
        p.0 >= r - self.tol
            && p.0 <= self.h - r + self.tol
            && p.1 >= r - self.tol
            && p.1 <= self.w - r + self.tol
    }

    fn place(&mut self, k: usize) -> bool {
        if k == PLATES {
            return true;
        }
        let r = self.radii[self.order[k]];
        let (xs, ys) = ([r, self.h - r], [r, self.w - r]);
        let mut cand: Vec<(f64, f64)> = Vec::new();
        for &x in &xs {
            for &y in &ys {
                cand.push((x, y)); // the four corners
            }
        }
        for i in 0..k {
            let q = self.pos[self.order[i]];
            let s = self.radii[self.order[i]] + r;
            for &x in &xs {
                // against a side wall and a placed plate
                let t = s * s - (x - q.0) * (x - q.0);
                if t >= 0.0 {
                    cand.push((x, q.1 - t.sqrt()));
                    cand.push((x, q.1 + t.sqrt()));
                }
            }
            for &y in &ys {
                let t = s * s - (y - q.1) * (y - q.1);
                if t >= 0.0 {
                    cand.push((q.0 - t.sqrt(), y));
                    cand.push((q.0 + t.sqrt(), y));
                }
            }
            for j in 0..i {
                // against two placed plates
                let other = self.order[j];
                touching(q, s, self.pos[other], self.radii[other] + r, &mut cand);
            }
        }
        for p in cand {
            if !self.fits(p, r) {
                continue;
            }
            let ok = (0..k).all(|i| {
                let q = self.pos[self.order[i]];
                (p.0 - q.0).hypot(p.1 - q.1) >= r + self.radii[self.order[i]] - self.tol
            });
            if !ok {
                continue;
            }
            self.pos[self.order[k]] = p;
            if self.place(k + 1) {
                return true;
            }
        }
        false
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<f64>().unwrap());
    let (h, w) = (it.next().unwrap(), it.next().unwrap());
    let mut radii = [0.0; PLATES];
    for r in radii.iter_mut() {
        *r = it.next().unwrap();
    }
    let mut tray = Tray {
        h,
        w,
        tol: EPS * (h + w),
        radii,
        order: [0; PLATES],
        pos: [(0.0, 0.0); PLATES],
    };
    // pushing every plate down and to the left as far as it goes leaves each
    // one held by two walls or plates placed before it, so some order of the
    // plates and some choice of two such supports finds a placement
    let orders = [
        [0, 1, 2],
        [0, 2, 1],
        [1, 0, 2],
        [1, 2, 0],
        [2, 0, 1],
        [2, 1, 0],
    ];
    for order in orders {
        tray.order = order;
        if tray.place(0) {
            let parts: Vec<String> = tray
                .pos
                .iter()
                .map(|p| format!("{:.4} {:.4}", p.0, p.1))
                .collect();
            println!("{}", parts.join(" "));
            return;
        }
    }
    println!("0");
}
