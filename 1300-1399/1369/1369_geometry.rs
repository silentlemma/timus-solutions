use std::io::{self, Read, Write};

// a coordinate times 10^SCALE, exact
type Fixed = i128;

const SCALE: i32 = 30; // decimal digits kept after the point
const LANDMARKS: usize = 1024; // evenly spread start points for the walks

// error bounds of the floating-point filters
const ORIENT_ERR: f64 = 3.3306690621773722e-16;
const IN_CIRCLE_ERR: f64 = 1.1102230246251565e-15;
const QUAD: usize = 4; // edges in a group: an edge and its rotations
const LAST_ROT: usize = 3; // the last rotation, also the mask of the rotations
const TEN: i128 = 10;
const LIMBS: usize = 16;
const LIMB_BITS: u32 = 32;
const KEY_BITS: u32 = 32;
const FIXED_LIMBS: usize = 4;
const EPS_BITS: usize = 24; // EPS = 2^-24 on squared distances

// A signed integer modulo 2^512 in 32-bit limbs; every value used here is far
// below 2^511, so the arithmetic is exact.
#[derive(Clone, Copy)]
struct Big([u32; LIMBS]);

impl Big {
    fn from_fixed(v: Fixed) -> Big {
        let mut r = [if v < 0 { u32::MAX } else { 0 }; LIMBS];
        let mut u = v as u128;
        for limb in r.iter_mut().take(FIXED_LIMBS) {
            *limb = u as u32;
            u >>= LIMB_BITS;
        }
        Big(r)
    }

    fn add(&self, y: &Big) -> Big {
        let mut r = [0; LIMBS];
        let mut carry = 0u64;
        for i in 0..LIMBS {
            carry += self.0[i] as u64 + y.0[i] as u64;
            r[i] = carry as u32;
            carry >>= LIMB_BITS;
        }
        Big(r)
    }

    fn sub(&self, y: &Big) -> Big {
        let mut r = [0; LIMBS];
        let mut borrow = 0i64;
        for i in 0..LIMBS {
            let z = self.0[i] as i64 - y.0[i] as i64 + borrow;
            r[i] = z as u32;
            borrow = if z < 0 { -1 } else { 0 };
        }
        Big(r)
    }

    fn mul(&self, y: &Big) -> Big {
        let mut acc = [0u64; LIMBS];
        for i in 0..LIMBS {
            if self.0[i] == 0 {
                continue;
            }
            let mut carry = 0u64;
            for j in 0..LIMBS - i {
                let z = self.0[i] as u64 * y.0[j] as u64 + acc[i + j] + carry;
                acc[i + j] = z & u32::MAX as u64;
                carry = z >> LIMB_BITS;
            }
        }
        let mut r = [0; LIMBS];
        for i in 0..LIMBS {
            r[i] = acc[i] as u32;
        }
        Big(r)
    }

    fn sign(&self) -> i32 {
        if self.0[LIMBS - 1] >> (LIMB_BITS - 1) != 0 {
            -1
        } else if self.0.iter().any(|&v| v != 0) {
            1
        } else {
            0
        }
    }

    fn less(&self, y: &Big) -> bool {
        self.sub(y).sign() < 0
    }
}

#[derive(Clone, Copy)]
struct Point {
    x: Fixed,
    y: Fixed,
    fx: f64,
    fy: f64,
    first: usize, // the cockroaches at this point: ids[first..last]
    last: usize,
}

struct Delaunay<'a> {
    pts: &'a [Point],
    orig: Vec<i32>,
    next: Vec<usize>,
    active: Vec<bool>,
    free: Vec<usize>,
}

fn rot(e: usize) -> usize {
    (e & !LAST_ROT) | ((e + 1) & LAST_ROT)
}

fn invrot(e: usize) -> usize {
    (e & !LAST_ROT) | ((e + LAST_ROT) & LAST_ROT)
}

fn rev(e: usize) -> usize {
    e ^ 2
}

// Each predicate is evaluated in floating point first; when the result is
// within the rounding error, it is recomputed exactly on the decimals.
fn orient(pts: &[Point], a: usize, b: usize, c: usize) -> i32 {
    let (pa, pb, pc) = (&pts[a], &pts[b], &pts[c]);
    let l = (pa.fx - pc.fx) * (pb.fy - pc.fy);
    let r = (pa.fy - pc.fy) * (pb.fx - pc.fx);
    let (det, err) = (l - r, ORIENT_ERR * (l + r).abs());
    if det > err {
        return 1;
    }
    if det < -err {
        return -1;
    }
    let ax = Big::from_fixed(pa.x - pc.x);
    let ay = Big::from_fixed(pa.y - pc.y);
    let bx = Big::from_fixed(pb.x - pc.x);
    let by = Big::from_fixed(pb.y - pc.y);
    ax.mul(&by).sub(&ay.mul(&bx)).sign()
}

fn exact_in_circle(pts: &[Point], a: usize, b: usize, c: usize, d: usize) -> bool {
    let pd = &pts[d];
    let diff = |i: usize| {
        (
            Big::from_fixed(pts[i].x - pd.x),
            Big::from_fixed(pts[i].y - pd.y),
        )
    };
    let ((adx, ady), (bdx, bdy), (cdx, cdy)) = (diff(a), diff(b), diff(c));
    let ab = adx.mul(&bdy).sub(&bdx.mul(&ady));
    let bc = bdx.mul(&cdy).sub(&cdx.mul(&bdy));
    let ca = cdx.mul(&ady).sub(&adx.mul(&cdy));
    let al = adx.mul(&adx).add(&ady.mul(&ady));
    let bl = bdx.mul(&bdx).add(&bdy.mul(&bdy));
    let cl = cdx.mul(&cdx).add(&cdy.mul(&cdy));
    al.mul(&bc).add(&bl.mul(&ca)).add(&cl.mul(&ab)).sign() > 0
}

// d lies strictly inside the circle through a, b, c (counterclockwise)
fn in_circle(pts: &[Point], a: usize, b: usize, c: usize, d: usize) -> bool {
    let pd = &pts[d];
    let (adx, ady) = (pts[a].fx - pd.fx, pts[a].fy - pd.fy);
    let (bdx, bdy) = (pts[b].fx - pd.fx, pts[b].fy - pd.fy);
    let (cdx, cdy) = (pts[c].fx - pd.fx, pts[c].fy - pd.fy);
    let (bdxcdy, cdxbdy) = (bdx * cdy, cdx * bdy);
    let (cdxady, adxcdy) = (cdx * ady, adx * cdy);
    let (adxbdy, bdxady) = (adx * bdy, bdx * ady);
    let al = adx * adx + ady * ady;
    let bl = bdx * bdx + bdy * bdy;
    let cl = cdx * cdx + cdy * cdy;
    let det = al * (bdxcdy - cdxbdy) + bl * (cdxady - adxcdy) + cl * (adxbdy - bdxady);
    let permanent = (bdxcdy.abs() + cdxbdy.abs()) * al
        + (cdxady.abs() + adxcdy.abs()) * bl
        + (adxbdy.abs() + bdxady.abs()) * cl;
    let err = IN_CIRCLE_ERR * permanent;
    if det > err {
        return true;
    }
    if det < -err {
        return false;
    }
    exact_in_circle(pts, a, b, c, d)
}

// Delaunay triangulation by divide and conquer on quad-edges: edge e, its
// rotations within one group of four, rev(e) the same edge reversed.
impl<'a> Delaunay<'a> {
    fn dest(&self, e: usize) -> usize {
        self.orig[rev(e)] as usize
    }

    fn org(&self, e: usize) -> usize {
        self.orig[e] as usize
    }

    fn lnext(&self, e: usize) -> usize {
        rot(self.next[invrot(e)])
    }

    fn oprev(&self, e: usize) -> usize {
        rot(self.next[rot(e)])
    }

    fn make_edge(&mut self, a: usize, b: usize) -> usize {
        let e = match self.free.pop() {
            Some(e) => e,
            None => {
                let e = self.orig.len();
                self.orig.extend_from_slice(&[0; QUAD]);
                self.next.extend_from_slice(&[0; QUAD]);
                self.active.push(false);
                e
            }
        };
        self.orig[e..e + QUAD].copy_from_slice(&[a as i32, -1, b as i32, -1]);
        self.next[e..e + QUAD].copy_from_slice(&[e, e + LAST_ROT, e + 2, e + 1]);
        self.active[e >> 2] = true;
        e
    }

    fn splice(&mut self, a: usize, b: usize) {
        let (alpha, beta) = (rot(self.next[a]), rot(self.next[b]));
        self.next.swap(alpha, beta);
        self.next.swap(a, b);
    }

    fn delete_edge(&mut self, e: usize) {
        let p = self.oprev(e);
        self.splice(e, p);
        let p = self.oprev(rev(e));
        self.splice(rev(e), p);
        self.active[e >> 2] = false;
        self.free.push(e & !LAST_ROT);
    }

    fn connect(&mut self, a: usize, b: usize) -> usize {
        let e = self.make_edge(self.dest(a), self.org(b));
        let l = self.lnext(a);
        self.splice(e, l);
        self.splice(rev(e), b);
        e
    }

    fn turn(&self, p: usize, e: usize) -> i32 {
        orient(self.pts, self.org(e), self.dest(e), p)
    }

    fn in_circle(&self, a: usize, b: usize, c: usize, d: usize) -> bool {
        in_circle(self.pts, a, b, c, d)
    }

    // points l..=r (sorted by x, then y); returns the counterclockwise hull
    // edge out of the leftmost point and the clockwise one out of the rightmost
    fn build(&mut self, l: usize, r: usize) -> (usize, usize) {
        if r - l == 1 {
            let e = self.make_edge(l, r);
            return (e, rev(e));
        }
        if r - l == 2 {
            let a = self.make_edge(l, l + 1);
            let b = self.make_edge(l + 1, r);
            self.splice(rev(a), b);
            let turn = orient(self.pts, l, l + 1, r);
            if turn == 0 {
                return (a, rev(b));
            }
            let c = self.connect(b, a);
            return if turn > 0 { (a, rev(b)) } else { (rev(c), c) };
        }
        let mid = (l + r) / 2;
        let (mut ldo, mut ldi) = self.build(l, mid);
        let (mut rdi, mut rdo) = self.build(mid + 1, r);
        loop {
            // the lower common tangent
            if self.turn(self.org(rdi), ldi) > 0 {
                ldi = self.lnext(ldi);
            } else if self.turn(self.org(ldi), rdi) < 0 {
                rdi = self.next[rev(rdi)];
            } else {
                break;
            }
        }
        let mut basel = self.connect(rev(rdi), ldi);
        if self.org(ldi) == self.org(ldo) {
            ldo = rev(basel);
        }
        if self.org(rdi) == self.org(rdo) {
            rdo = basel;
        }
        loop {
            // zip the halves upward
            let valid = |s: &Self, e: usize, basel: usize| s.turn(s.dest(e), basel) < 0;
            let mut lc = self.next[rev(basel)];
            if valid(self, lc, basel) {
                while self.in_circle(
                    self.dest(basel),
                    self.org(basel),
                    self.dest(lc),
                    self.dest(self.next[lc]),
                ) {
                    let t = self.next[lc];
                    self.delete_edge(lc);
                    lc = t;
                }
            }
            let mut rc = self.oprev(basel);
            if valid(self, rc, basel) {
                while self.in_circle(
                    self.dest(basel),
                    self.org(basel),
                    self.dest(rc),
                    self.dest(self.oprev(rc)),
                ) {
                    let t = self.oprev(rc);
                    self.delete_edge(rc);
                    rc = t;
                }
            }
            let (lv, rv) = (valid(self, lc, basel), valid(self, rc, basel));
            if !lv && !rv {
                break;
            }
            if !lv
                || (rv && self.in_circle(self.dest(lc), self.org(lc), self.org(rc), self.dest(rc)))
            {
                basel = self.connect(rc, rev(basel));
            } else {
                basel = self.connect(rev(basel), rev(lc));
            }
        }
        (ldo, rdo)
    }
}

// a decimal number times 10^SCALE, digits beyond that dropped
fn parse_fixed(s: &[u8]) -> Fixed {
    let negative = s.first() == Some(&b'-');
    let s = if matches!(s.first(), Some(b'-') | Some(b'+')) {
        &s[1..]
    } else {
        s
    };
    let mut digits = Vec::new();
    let (mut fraction, mut exponent, mut dot) = (0i32, 0i32, false);
    let mut i = 0;
    while i < s.len() && s[i] != b'e' && s[i] != b'E' {
        if s[i] == b'.' {
            dot = true;
        } else {
            digits.push((s[i] - b'0') as i128);
            fraction += dot as i32;
        }
        i += 1;
    }
    if i < s.len() {
        exponent = std::str::from_utf8(&s[i + 1..]).unwrap().parse().unwrap();
    }
    let shift = SCALE - fraction + exponent;
    let keep = if shift < 0 {
        (digits.len() as i32 + shift).max(0) as usize
    } else {
        digits.len()
    };
    let mut v: Fixed = 0;
    for &d in &digits[..keep] {
        v = v * TEN + d;
    }
    for _ in 0..shift.max(0) {
        v *= TEN;
    }
    if negative {
        -v
    } else {
        v
    }
}

fn edge_key(a: usize, b: usize) -> u64 {
    let (a, b) = if a < b { (a, b) } else { (b, a) };
    (a as u64) << KEY_BITS | b as u64
}

struct Query<'a> {
    pts: &'a [Point],
    offset: &'a [usize],
    adj: &'a [usize],
    qx: Fixed,
    qy: Fixed,
    x: f64,
    y: f64,
}

impl<'a> Query<'a> {
    // the squared distance from point i, exact: SCALE * 2 digits
    fn dist2(&self, i: usize) -> Big {
        let bx = Big::from_fixed((self.pts[i].x - self.qx).abs());
        let by = Big::from_fixed((self.pts[i].y - self.qy).abs());
        bx.mul(&bx).add(&by.mul(&by))
    }

    fn dist2f(&self, i: usize) -> f64 {
        let (dx, dy) = (self.pts[i].fx - self.x, self.pts[i].fy - self.y);
        dx * dx + dy * dy
    }

    fn around(&self, v: usize) -> &'a [usize] {
        &self.adj[self.offset[v]..self.offset[v + 1]]
    }

    // the point nearest to the sweet: a walk on floating point, then an exact one
    fn nearest(&self, seed: usize) -> usize {
        let mut cur = seed;
        loop {
            let (mut best, mut bd) = (cur, self.dist2f(cur));
            for &v in self.around(cur) {
                let z = self.dist2f(v);
                if z < bd {
                    bd = z;
                    best = v;
                }
            }
            if best == cur {
                break;
            }
            cur = best;
        }
        loop {
            let (mut best, mut bd) = (cur, self.dist2(cur));
            for &v in self.around(cur) {
                let z = self.dist2(v);
                if z.less(&bd) {
                    bd = z;
                    best = v;
                }
            }
            if best == cur {
                return cur;
            }
            cur = best;
        }
    }
}

fn main() {
    let mut data = Vec::new();
    io::stdin().read_to_end(&mut data).unwrap();
    let mut tokens = data
        .split(|c| c.is_ascii_whitespace())
        .filter(|t| !t.is_empty());
    let mut token = || tokens.next().unwrap();
    let number = |t: &[u8]| -> f64 { std::str::from_utf8(t).unwrap().parse().unwrap() };
    let m: usize = std::str::from_utf8(token()).unwrap().parse().unwrap();
    let mut raw: Vec<Point> = (0..m)
        .map(|i| {
            let (tx, ty) = (token(), token());
            Point {
                x: parse_fixed(tx),
                y: parse_fixed(ty),
                fx: number(tx),
                fy: number(ty),
                first: i,
                last: i + 1,
            }
        })
        .collect();
    let n: usize = std::str::from_utf8(token()).unwrap().parse().unwrap();
    if n == 0 {
        return;
    }
    // equal points become one, keeping all their cockroaches
    raw.sort_by(|a, b| (a.x, a.y, a.first).cmp(&(b.x, b.y, b.first)));
    let mut ids = Vec::with_capacity(m);
    let mut pts: Vec<Point> = Vec::new();
    let mut i = 0;
    while i < m {
        let (mut j, start) = (i, ids.len());
        while j < m && raw[j].x == raw[i].x && raw[j].y == raw[i].y {
            ids.push(raw[j].first + 1);
            j += 1;
        }
        pts.push(Point {
            first: start,
            last: ids.len(),
            ..raw[i]
        });
        i = j;
    }
    let k = pts.len();
    let mut keys: Vec<u64> = Vec::new();
    let collinear = (2..k).all(|i| orient(&pts, 0, 1, i) == 0);
    if k > 2 && !collinear {
        let mut d = Delaunay {
            pts: &pts,
            orig: Vec::new(),
            next: Vec::new(),
            active: Vec::new(),
            free: Vec::new(),
        };
        d.build(0, k - 1);
        for (q, &on) in d.active.iter().enumerate() {
            if on {
                keys.push(edge_key(
                    d.orig[q * QUAD] as usize,
                    d.orig[q * QUAD + 2] as usize,
                ));
            }
        }
        let mut by_y: Vec<usize> = (0..k).collect();
        by_y.sort_by(|&a, &b| (pts[a].y, pts[a].x).cmp(&(pts[b].y, pts[b].x)));
        for w in by_y.windows(2) {
            keys.push(edge_key(w[0], w[1]));
        }
    }
    for i in 1..k {
        // neighbours by x; on a line, all edges
        keys.push(edge_key(i - 1, i));
    }
    // the graph: the triangulation plus the neighbours in the order by x and
    // by y, as adjacency lists adj[offset[v]..offset[v + 1]]
    keys.sort_unstable();
    keys.dedup();
    let mut offset = vec![0usize; k + 1];
    for &key in &keys {
        offset[(key >> KEY_BITS) as usize + 1] += 1;
        offset[(key as u32) as usize + 1] += 1;
    }
    for i in 0..k {
        offset[i + 1] += offset[i];
    }
    let mut at = offset[..k].to_vec();
    let mut adj = vec![0usize; offset[k]];
    for &key in &keys {
        let (a, b) = ((key >> KEY_BITS) as usize, (key as u32) as usize);
        adj[at[a]] = b;
        at[a] += 1;
        adj[at[b]] = a;
        at[b] += 1;
    }

    // the answer: the nearest point and every point closer than it plus EPS,
    // found by a search through the graph from it
    let ten = Big::from_fixed(TEN);
    let mut eps = Big::from_fixed(1);
    for _ in 0..2 * SCALE {
        eps = eps.mul(&ten);
    }
    for _ in 0..EPS_BITS {
        // EPS times 10^(2 * SCALE), an integer
        let mut carry = 0u32;
        for j in (0..LIMBS).rev() {
            let low = eps.0[j] & 1;
            eps.0[j] = eps.0[j] >> 1 | carry << (LIMB_BITS - 1);
            carry = low;
        }
    }
    let marks = LANDMARKS.min(k);
    let landmark: Vec<usize> = (0..marks)
        .map(|i| {
            if marks > 1 {
                i * (k - 1) / (marks - 1)
            } else {
                0
            }
        })
        .collect();
    let mut seen = vec![0usize; k];
    let (mut queue, mut answer): (Vec<usize>, Vec<usize>) = (Vec::new(), Vec::new());
    let mut prev = 0;
    let mut out = String::new();
    for stamp in 1..=n {
        let (tx, ty) = (token(), token());
        let q = Query {
            pts: &pts,
            offset: &offset,
            adj: &adj,
            qx: parse_fixed(tx),
            qy: parse_fixed(ty),
            x: number(tx),
            y: number(ty),
        };
        let (mut seed, mut bd) = (prev, q.dist2f(prev));
        for &v in &landmark {
            let z = q.dist2f(v);
            if z < bd {
                bd = z;
                seed = v;
            }
        }
        let best = q.nearest(seed);
        prev = best;
        let limit = q.dist2(best).add(&eps);
        queue.clear();
        queue.push(best);
        answer.clear();
        seen[best] = stamp;
        let mut h = 0;
        while h < queue.len() {
            let v = queue[h];
            h += 1;
            if !q.dist2(v).less(&limit) {
                continue;
            }
            answer.extend_from_slice(&ids[pts[v].first..pts[v].last]);
            for &u in q.around(v) {
                if seen[u] != stamp {
                    seen[u] = stamp;
                    queue.push(u);
                }
            }
        }
        answer.sort_unstable();
        let line: Vec<String> = answer.iter().map(|v| v.to_string()).collect();
        out.push_str(&line.join(" "));
        out.push('\n');
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}
