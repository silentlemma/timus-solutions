use std::io::{self, Read};

// Faces: 0 the base, 1..4 the sides clockwise from the one facing +y. On the
// base, side k rests on the edge (v[k - 1], v[k % 4]); on a side, v[0] and
// v[1] are its base corners and v[2] its apex.
const SIDES: usize = 4;
const FACES: usize = 5;
const MAX_ROLLS: usize = 32;
const EPS: f64 = 1e-12;
const NONE: f64 = -1e100;
const BEAM: usize = 4000; // states kept per depth by the first, greedy pass
const TRIANGLE: f64 = 3.0; // corners of a side: its centroid is a third of the way up
const START: usize = FACES * FACES; // the key of the starting state

#[derive(Clone, Copy, Default)]
struct Pt {
    x: f64,
    y: f64,
}

#[derive(Clone, Copy)]
struct State {
    face: usize,
    key: usize, // previous face * FACES + face, or START
    v: [Pt; SIDES],
    c: Pt, // the centre of the face on the table
}

fn can_roll(face: usize, next: usize) -> bool {
    // a neighbouring side, not the opposite one
    face != next && (face == 0 || next == 0 || (face + SIDES - next) % 2 == 1)
}

fn cross(a: Pt, b: Pt, p: Pt) -> f64 {
    (b.x - a.x) * (p.y - a.y) - (b.y - a.y) * (p.x - a.x)
}

fn reflect(p: Pt, a: Pt, b: Pt) -> Pt {
    let (dx, dy) = (b.x - a.x, b.y - a.y);
    let k = ((p.x - a.x) * dx + (p.y - a.y) * dy) / (dx * dx + dy * dy);
    Pt {
        x: 2.0 * (a.x + k * dx) - p.x,
        y: 2.0 * (a.y + k * dy) - p.y,
    }
}

// the unit normal of a -> b pointing away from q
fn away(a: Pt, b: Pt, q: Pt) -> (f64, f64) {
    let (dx, dy) = (b.x - a.x, b.y - a.y);
    let len = dx.hypot(dy);
    let (nx, ny) = (-dy / len, dx / len);
    if cross(
        a,
        b,
        Pt {
            x: a.x + nx,
            y: a.y + ny,
        },
    ) * cross(a, b, q)
        > 0.0
    {
        (-nx, -ny)
    } else {
        (nx, ny)
    }
}

struct Search {
    s: f64,
    t: f64, // the base edge and the height of a side
    x: f64,
    y: f64,
    n: usize,
    reach: Vec<[f64; MAX_ROLLS + 1]>, // the farthest the centre can go, ending on the base
    best: f64,
    best_rolls: usize,
    best_seq: [usize; MAX_ROLLS + 1],
    seq: [usize; MAX_ROLLS + 1],
}

impl Search {
    fn roll(&self, st: &State, next: usize) -> State {
        let v = &st.v;
        let mut ns = State {
            face: next,
            key: st.face * FACES + next,
            v: [Pt::default(); SIDES],
            c: Pt::default(),
        };
        if st.face == 0 {
            // onto side next: its apex beyond the edge
            let (a, b) = (v[next - 1], v[next % SIDES]);
            let (nx, ny) = away(a, b, st.c);
            ns.v[0] = a;
            ns.v[1] = b;
            ns.v[2] = Pt {
                x: (a.x + b.x) / 2.0 + nx * self.t,
                y: (a.y + b.y) / 2.0 + ny * self.t,
            };
        } else if next == 0 {
            // onto the base: the square beyond the edge
            let (a, b) = (v[0], v[1]);
            let (nx, ny) = away(a, b, v[2]);
            let s = self.s;
            let corner = [
                a,
                b,
                Pt {
                    x: b.x + nx * s,
                    y: b.y + ny * s,
                },
                Pt {
                    x: a.x + nx * s,
                    y: a.y + ny * s,
                },
            ];
            for (i, &p) in corner.iter().enumerate() {
                ns.v[(st.face - 1 + i) % SIDES] = p;
            }
        } else if next == st.face % SIDES + 1 {
            // clockwise over the edge (v[1], apex)
            ns.v[0] = v[1];
            ns.v[1] = reflect(v[0], v[1], v[2]);
            ns.v[2] = v[2];
        } else {
            // counterclockwise over the edge (v[0], apex)
            ns.v[0] = reflect(v[1], v[0], v[2]);
            ns.v[1] = v[0];
            ns.v[2] = v[2];
        }
        let n = if next == 0 { SIDES } else { SIDES - 1 };
        for p in &ns.v[..n] {
            ns.c.x += p.x / n as f64;
            ns.c.y += p.y / n as f64;
        }
        ns
    }

    fn dist2(&self, st: &State) -> f64 {
        let (dx, dy) = (st.c.x - self.x, st.c.y - self.y);
        dx * dx + dy * dy
    }

    fn dist(&self, st: &State) -> f64 {
        (st.c.x - self.x).hypot(st.c.y - self.y)
    }

    // can this state, with r rolls left, still beat the best?
    fn hopeful(&self, st: &State, r: usize) -> bool {
        let u = self.reach[st.key][r];
        let lim = self.best + u + EPS;
        u > NONE && self.dist2(st) <= lim * lim
    }

    fn consider(&mut self, sequence: &[usize], rolls: usize, d: f64) {
        if d + EPS < self.best || ((d - self.best).abs() <= EPS && rolls < self.best_rolls) {
            self.best = d;
            self.best_rolls = rolls;
            self.best_seq[..=rolls].copy_from_slice(&sequence[..=rolls]);
        }
    }

    fn search(&mut self, st: &State, depth: usize) {
        if st.face == 0 {
            let seq = self.seq;
            self.consider(&seq, depth, self.dist(st));
        }
        if depth == self.n {
            return;
        }
        let mut next: Vec<(f64, State)> = Vec::with_capacity(SIDES);
        let prev = if st.key == START {
            FACES
        } else {
            st.key / FACES
        };
        for f in 0..FACES {
            if !can_roll(st.face, f) || f == prev {
                continue;
            }
            let ns = self.roll(st, f);
            if self.hopeful(&ns, self.n - depth - 1) {
                next.push((self.dist2(&ns), ns));
            }
        }
        next.sort_by(|a, b| a.0.partial_cmp(&b.0).unwrap()); // nearest first
        for (_, ns) in &next {
            self.seq[depth + 1] = ns.face;
            self.search(ns, depth + 1);
        }
    }

    // a first answer: a beam search keeping the states that may get closest
    fn beam(&mut self, start: State) {
        let mut states: Vec<(f64, State, [usize; MAX_ROLLS + 1])> =
            vec![(0.0, start, [0; MAX_ROLLS + 1])];
        for depth in 0..self.n {
            let mut next = Vec::new();
            for (_, st, seq) in &states {
                let prev = if st.key == START {
                    FACES
                } else {
                    st.key / FACES
                };
                for f in 0..FACES {
                    if !can_roll(st.face, f) || f == prev {
                        continue;
                    }
                    let ns = self.roll(st, f);
                    let r = self.reach[ns.key][self.n - depth - 1];
                    if r <= NONE {
                        continue;
                    }
                    let d = self.dist(&ns);
                    let mut nseq = *seq;
                    nseq[depth + 1] = f;
                    if f == 0 {
                        self.consider(&nseq, depth + 1, d);
                    }
                    next.push(((d - r).max(0.0), ns, nseq));
                }
            }
            next.sort_by(|a, b| a.0.partial_cmp(&b.0).unwrap());
            next.truncate(BEAM);
            states = next;
        }
    }
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut it = text.split_ascii_whitespace();
    let mut num = || it.next().unwrap().parse::<f64>().unwrap();
    let (s, l, x, y) = (num(), num(), num(), num());
    let n = num() as usize;
    let t = (l * l - (s / 2.0).powi(2)).sqrt();
    // how far one roll moves the centre: base <-> side, and side <-> side
    let (base_step, side_step) = (s / 2.0 + t / TRIANGLE, 2.0 * s * t / (TRIANGLE * l));
    let mut reach = vec![[NONE; MAX_ROLLS + 1]; START + 1];
    reach[START][0] = 0.0;
    for prev in 1..FACES {
        reach[prev * FACES][0] = 0.0;
    }
    for r in 1..=n {
        for face in 0..FACES {
            for prev in 0..=FACES {
                // prev == FACES: the start
                let k = if prev == FACES {
                    START
                } else {
                    prev * FACES + face
                };
                if (prev == FACES && face != 0) || (prev < FACES && !can_roll(prev, face)) {
                    continue;
                }
                let mut u = reach[k][r - 1];
                if face == 0 {
                    u = u.max(0.0);
                }
                for f in 0..FACES {
                    if can_roll(face, f) && f != prev && reach[face * FACES + f][r - 1] > NONE {
                        let step = if face == 0 || f == 0 {
                            base_step
                        } else {
                            side_step
                        };
                        u = u.max(step + reach[face * FACES + f][r - 1]);
                    }
                }
                reach[k][r] = u;
            }
        }
    }
    let h = s / 2.0;
    let start = State {
        face: 0,
        key: START,
        v: [
            Pt { x: -h, y: h },
            Pt { x: h, y: h },
            Pt { x: h, y: -h },
            Pt { x: -h, y: -h },
        ],
        c: Pt::default(),
    };
    let mut sr = Search {
        s,
        t,
        x,
        y,
        n,
        reach,
        best: x.hypot(y),
        best_rolls: 0,
        best_seq: [0; MAX_ROLLS + 1],
        seq: [0; MAX_ROLLS + 1],
    };
    sr.beam(start);
    sr.search(&start, 0);
    let faces: Vec<String> = sr.best_seq[..=sr.best_rolls]
        .iter()
        .map(|f| f.to_string())
        .collect();
    println!(
        "{:.3}\n{}\n{}",
        sr.best + EPS,
        sr.best_rolls,
        faces.join(" ")
    );
}
