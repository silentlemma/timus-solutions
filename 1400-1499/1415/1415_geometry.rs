use std::io::{self, Read, Write};

const COLORS: [&str; 7] = [
    "VIOLET", "INDIGO", "BLUE", "GREEN", "YELLOW", "ORANGE", "RED",
];
const RED: usize = 6;
const PER_DECADE: f64 = 5.0; // a level per 2 dB: five levels per tenfold distance
const TEN: f64 = 10.0;
const EPS: f64 = 1e-9; // events closer than this in segment time happen together
const TIE: f64 = 1e-9; // powers closer than this relative gap are equal

struct Town {
    xs: Vec<f64>,
    ys: Vec<f64>,
    rs: Vec<f64>,
    names: Vec<Vec<u8>>,
    bounds: Vec<Vec<f64>>, // squared radii where the level steps up
}

struct Segment {
    sx: f64,
    sy: f64,
    dx: f64,
    dy: f64,
    len2: f64,
}

impl Town {
    fn level(&self, i: usize, px: f64, py: f64) -> usize {
        let d2 = (px - self.xs[i]).powi(2) + (py - self.ys[i]).powi(2);
        self.bounds[i].iter().filter(|&&b| d2 > b).count()
    }

    /// The strongest station at (px, py); equal powers go to the smaller name.
    fn best(&self, cands: &[usize], px: f64, py: f64) -> usize {
        let mut top = cands[0];
        for &i in &cands[1..] {
            // power is r / d: compare r_i * d_top with r_top * d_i
            let a = self.rs[i] * (px - self.xs[top]).hypot(py - self.ys[top]);
            let b = self.rs[top] * (px - self.xs[i]).hypot(py - self.ys[i]);
            if a > b * (1.0 + TIE)
                || ((a - b).abs() <= TIE * a.max(b) && self.names[i] < self.names[top])
            {
                top = i;
            }
        }
        top
    }

    /// Times in (0, 1) where the distance to station i squared is rad2.
    fn roots(&self, s: &Segment, i: usize, rad2: f64, out: &mut Vec<f64>) {
        let (px, py) = (s.sx - self.xs[i], s.sy - self.ys[i]);
        let (b, c) = (s.dx * px + s.dy * py, px * px + py * py - rad2);
        let disc = b * b - s.len2 * c;
        if disc <= 0.0 {
            return;
        }
        let q = -(b + disc.sqrt().copysign(b));
        for t in [q / s.len2, c / q] {
            if t > 0.0 && t < 1.0 {
                out.push(t);
            }
        }
    }

    /// The level of station i just after time t, before its own next change.
    fn level_after(&self, s: &Segment, i: usize, t: f64) -> usize {
        let mut ts = Vec::new();
        for &b in &self.bounds[i] {
            self.roots(s, i, b, &mut ts);
        }
        let next = ts
            .iter()
            .filter(|&&u| u > t + EPS)
            .fold(1.0f64, |m, &u| m.min(u));
        let u = (t + next) / 2.0;
        self.level(i, s.sx + s.dx * u, s.sy + s.dy * u)
    }

    /// Events as (time, station); None marks the current station's own circles.
    fn timeline(
        &self,
        s: &Segment,
        reds: &[(f64, Option<usize>)],
        cur: usize,
        after: f64,
    ) -> Vec<(f64, Option<usize>)> {
        let mut ts = Vec::new();
        for &b in &self.bounds[cur] {
            self.roots(s, cur, b, &mut ts);
        }
        let mut events: Vec<(f64, Option<usize>)> = ts.into_iter().map(|t| (t, None)).collect();
        events.extend(reds.iter().cloned());
        events.retain(|e| e.0 > after);
        events.sort_by(|a, b| a.partial_cmp(b).unwrap());
        events
    }
}

fn main() {
    let mut data = Vec::new();
    io::stdin().read_to_end(&mut data).unwrap();
    let words: Vec<&[u8]> = data
        .split(|c| c.is_ascii_whitespace())
        .filter(|w| !w.is_empty())
        .collect();
    let mut pos = 0;
    let mut next = || {
        pos += 1;
        words[pos - 1]
    };
    let num = |w: &[u8]| -> f64 { std::str::from_utf8(w).unwrap().parse().unwrap() };
    let n = num(next()) as usize;
    let mut town = Town {
        xs: vec![],
        ys: vec![],
        rs: vec![],
        names: vec![],
        bounds: vec![],
    };
    for _ in 0..n {
        town.xs.push(num(next()));
        town.ys.push(num(next()));
        let r = num(next());
        town.rs.push(r);
        town.names.push(next().to_vec());
        town.bounds.push(
            (0..RED)
                .map(|k| (r * TEN.powf(k as f64 / PER_DECADE)).powi(2))
                .collect(),
        );
    }
    let m = num(next()) as usize;
    // each segment as its start and its end
    let segments: Vec<((f64, f64), (f64, f64))> = (0..m)
        .map(|_| ((num(next()), num(next())), (num(next()), num(next()))))
        .collect();
    let mut out: Vec<u8> = Vec::new();
    let all: Vec<usize> = (0..n).collect();
    let (x0, y0) = segments[0].0;
    let mut cur = town.best(&all, x0, y0);
    let mut lev = town.level(cur, x0, y0);
    let cell = |out: &mut Vec<u8>, head: &str, name: &[u8], lev: usize| {
        out.extend_from_slice(head.as_bytes());
        out.extend_from_slice(name);
        out.extend_from_slice(format!(", SIGNAL_LEVEL:{}\n", COLORS[lev]).as_bytes());
    };
    cell(&mut out, "Power on. CELL_ID:", &town.names[cur], lev);

    for &((sx, sy), (ex, ey)) in &segments {
        let (dx, dy) = (ex - sx, ey - sy);
        let s = Segment {
            sx,
            sy,
            dx,
            dy,
            len2: dx * dx + dy * dy,
        };
        if s.len2 == 0.0 {
            continue;
        }
        // red and not red switch only on the outer circles
        let mut reds = Vec::new();
        for i in 0..n {
            let mut ts = Vec::new();
            town.roots(&s, i, town.bounds[i][RED - 1], &mut ts);
            reds.extend(ts.into_iter().map(|t| (t, Some(i))));
        }
        let mut events = town.timeline(&s, &reds, cur, -1.0);
        let mut k = 0;
        while k < events.len() {
            let t0 = events[k].0;
            let mut group = Vec::new();
            while k < events.len() && events[k].0 - t0 <= EPS {
                group.push(events[k].1);
                k += 1;
            }
            // the state right after the group holds until the next event
            let tend = events[k - 1].0;
            let t1 = if k < events.len() { events[k].0 } else { 1.0 };
            let (mx, my) = (s.sx + s.dx * (t0 + t1) / 2.0, s.sy + s.dy * (t0 + t1) / 2.0);
            let (px, py) = (s.sx + s.dx * t0, s.sy + s.dy * t0);
            let mut searching = false;
            let mut cands = Vec::new();
            if lev != RED {
                let now = town.level(cur, mx, my);
                if now != lev {
                    lev = now;
                    out.extend_from_slice(
                        format!("Signal changed. SIGNAL_LEVEL:{}\n", COLORS[lev]).as_bytes(),
                    );
                    if lev == RED {
                        searching = true;
                        cands = (0..n).filter(|&i| town.level(i, mx, my) < RED).collect();
                    }
                }
            } else {
                searching = true;
                cands = group
                    .iter()
                    .flatten()
                    .cloned()
                    .filter(|&i| town.level(i, mx, my) < RED)
                    .collect();
            }
            if !searching || cands.is_empty() {
                continue;
            }
            let pick = town.best(&cands, px, py);
            lev = town.level_after(&s, pick, tend);
            if pick == cur {
                out.extend_from_slice(
                    format!("Signal changed. SIGNAL_LEVEL:{}\n", COLORS[lev]).as_bytes(),
                );
            } else {
                cur = pick;
                cell(&mut out, "Cell changed. CELL_ID:", &town.names[cur], lev);
                events = town.timeline(&s, &reds, cur, tend + EPS);
                k = 0;
            }
        }
    }
    io::stdout().write_all(&out).unwrap();
}
