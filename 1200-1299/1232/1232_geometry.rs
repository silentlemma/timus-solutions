use std::fmt::Write as _;
use std::io::{self, Read, Write};

const EPS: f64 = 1e-9;

struct Cone {
    h: f64,
    d: f64,
    tg: f64,
    sn: f64,
    cs: f64,
}

impl Cone {
    // the smallest drop of one move from a point on the cone wall at depth t
    // below the station: the move goes across to the opposite wall, or is
    // almost level once the cone there is at least d wide
    fn min_drop(&self, t: f64) -> f64 {
        let (d, tg) = (self.d, self.tg);
        let w = 2.0 * t * tg;
        if w >= d {
            return 0.0;
        }
        ((d * d * (1.0 + tg * tg) - w * w).sqrt() - w * tg) / (1.0 + tg * tg)
    }

    // n moves in the plane y = 0: first slides moves down the wall, then
    // crossings at full tilt, and as soon as one move can drop exactly the
    // extra height, that move and then straight down
    fn path(&self, n: usize, slides: usize) -> Option<Vec<(f64, f64)>> {
        let (h, d) = (self.h, self.d);
        let mut pts = Vec::with_capacity(n);
        let (mut t, mut x, mut side) = (0.0f64, 0.0f64, 1.0f64);
        for left in (1..=n).rev() {
            let extra = h - t - (left - 1) as f64 * d;
            let drop = self.min_drop(t);
            if extra >= drop - EPS {
                x += side * (d * d - extra * extra).max(0.0).sqrt();
                t += extra;
                pts.push((x, h - t));
                for k in (1..left).rev() {
                    pts.push((x, (k - 1) as f64 * d));
                }
                pts.last_mut().unwrap().1 = 0.0;
                return Some(pts);
            }
            if left == 1 {
                return None;
            }
            if n - left < slides {
                x -= side * d * self.sn;
                t += d * self.cs;
            } else {
                t += drop;
                x = side * t * self.tg;
                side = -side;
            }
            pts.push((x, h - t));
        }
        None
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<f64> = input
        .split_ascii_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();
    let (h, d, half) = (v[0], v[1], v[2] / 2.0);
    let cone = Cone {
        h,
        d,
        tg: half.tan(),
        sn: half.sin(),
        cs: half.cos(),
    };
    let n = (h / d - EPS).ceil() as usize;
    let mut out = String::new();
    match (0..=n).find_map(|slides| cone.path(n, slides)) {
        Some(pts) => {
            writeln!(out, "{}", n).unwrap();
            for (x, z) in pts {
                writeln!(out, "{:.6} 0 {:.6}", x, z).unwrap();
            }
        }
        None => out.push_str("-1\n"),
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}
