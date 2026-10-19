use std::cmp::Ordering;
use std::io::{self, Read, Write};
use std::ops::{Add, Mul, Neg, Sub};

const LIMB_BITS: u32 = 32; // magnitudes are kept in 32-bit limbs
const SCALE: i64 = 4; // N is the distance of Q from the vertex times 4 |A|^3

// a small signed big integer: values here reach about 10^164
#[derive(Clone)]
struct Big {
    negative: bool,
    limbs: Vec<u32>, // least significant first, no leading zeros
}

impl Big {
    fn from(v: i64) -> Big {
        let mut m = v.unsigned_abs();
        let mut limbs = Vec::new();
        while m > 0 {
            limbs.push(m as u32);
            m >>= LIMB_BITS;
        }
        Big { negative: v < 0, limbs }
    }

    fn zero(&self) -> bool {
        self.limbs.is_empty()
    }

    fn trimmed(mut self) -> Big {
        while self.limbs.last() == Some(&0) {
            self.limbs.pop();
        }
        if self.zero() {
            self.negative = false;
        }
        self
    }

    fn parse(s: &str) -> Big {
        let digits = s.trim_start_matches('-');
        let mut r = Big::from(0);
        for c in digits.bytes() {
            r = &(&r * &Big::from(10)) + &Big::from((c - b'0') as i64);
        }
        if s.starts_with('-') {
            -&r
        } else {
            r
        }
    }
}

fn compare_magnitude(a: &Big, b: &Big) -> Ordering {
    a.limbs.len().cmp(&b.limbs.len()).then_with(|| a.limbs.iter().rev().cmp(b.limbs.iter().rev()))
}

fn add_magnitude(a: &Big, b: &Big) -> Vec<u32> {
    let mut r = Vec::new();
    let mut carry = 0u64;
    let mut i = 0;
    while i < a.limbs.len().max(b.limbs.len()) || carry > 0 {
        let s = carry
            + *a.limbs.get(i).unwrap_or(&0) as u64
            + *b.limbs.get(i).unwrap_or(&0) as u64;
        r.push(s as u32);
        carry = s >> LIMB_BITS;
        i += 1;
    }
    r
}

fn sub_magnitude(a: &Big, b: &Big) -> Vec<u32> {
    // |a| >= |b|
    let mut r = Vec::new();
    let mut borrow = 0i64;
    for i in 0..a.limbs.len() {
        let mut s = a.limbs[i] as i64 - borrow - *b.limbs.get(i).unwrap_or(&0) as i64;
        borrow = 0;
        if s < 0 {
            s += 1i64 << LIMB_BITS;
            borrow = 1;
        }
        r.push(s as u32);
    }
    r
}

impl<'a> Neg for &'a Big {
    type Output = Big;
    fn neg(self) -> Big {
        Big { negative: !self.negative && !self.zero(), limbs: self.limbs.clone() }
    }
}

impl<'a> Add for &'a Big {
    type Output = Big;
    fn add(self, b: &Big) -> Big {
        if self.negative == b.negative {
            return Big { negative: self.negative, limbs: add_magnitude(self, b) }.trimmed();
        }
        if compare_magnitude(self, b) != Ordering::Less {
            Big { negative: self.negative, limbs: sub_magnitude(self, b) }.trimmed()
        } else {
            Big { negative: b.negative, limbs: sub_magnitude(b, self) }.trimmed()
        }
    }
}

impl<'a> Sub for &'a Big {
    type Output = Big;
    fn sub(self, b: &Big) -> Big {
        self + &(-b)
    }
}

impl<'a> Mul for &'a Big {
    type Output = Big;
    fn mul(self, b: &Big) -> Big {
        let mut r = vec![0u32; self.limbs.len() + b.limbs.len()];
        for (i, &x) in self.limbs.iter().enumerate() {
            let mut carry = 0u64;
            let mut j = 0;
            while j < b.limbs.len() || carry > 0 {
                let mut cur = r[i + j] as u64 + carry;
                if j < b.limbs.len() {
                    cur += x as u64 * b.limbs[j] as u64;
                }
                r[i + j] = cur as u32;
                carry = cur >> LIMB_BITS;
                j += 1;
            }
        }
        Big { negative: self.negative != b.negative, limbs: r }.trimmed()
    }
}

fn le(a: &Big, b: &Big) -> bool {
    if a.negative != b.negative {
        return a.negative;
    }
    let c = compare_magnitude(a, b);
    if a.negative {
        c != Ordering::Less
    } else {
        c != Ordering::Greater
    }
}

fn cross(ux: &Big, uy: &Big, vx: &Big, vy: &Big) -> Big {
    &(ux * vy) - &(uy * vx)
}

type Coefficients<'a> = (&'a Big, &'a Big, &'a Big, &'a Big, &'a Big, &'a Big);

fn answer(curve: Coefficients, px: &Big, py: &Big, r: &Big) -> &'static str {
    // the curve is C + B t + A t^2 with A = (a, d), B = (b, e), C = (c, f)
    let (a, b, c, d, e, f) = curve;
    let (wx, wy) = (px - c, py - f); // P relative to C
    let r2 = r * r;
    if a.zero() && d.zero() {
        if b.zero() && e.zero() {
            // a single point: every line through it is an axis, and Q runs over the
            // circle with diameter CP, from C itself to P
            return if le(&(&(&wx * &wx) + &(&wy * &wy)), &r2) { "YES" } else { "MAYBE" };
        }
        // a line: the line itself is an axis (Q lies on it), and so is every
        // perpendicular, with Q at the distance of P from the line
        let dist = cross(&wx, &wy, b, e);
        let limit = &r2 * &(&(b * b) + &(e * e));
        return if le(&(&dist * &dist), &limit) { "YES" } else { "MAYBE" };
    }
    // one axis along A; along it, P lies at N / (4 |A|^3) from the vertex
    let scale = Big::from(SCALE);
    let a2 = &(a * a) + &(d * d);
    let ab = &(a * b) + &(d * e);
    let n = &(&(&scale * &a2) * &(&(&wx * a) + &(&wy * d))) + &(&ab * &ab);
    let k = cross(a, d, b, e);
    let k2 = &k * &k; // zero for a ray, otherwise the parabola width
    let a6 = &(&a2 * &a2) * &a2;
    let inside = if le(&n, &(&Big::from(2) * &k2)) {
        // the nearest point of the curve is its vertex (the end of a ray)
        le(&(&n * &n), &(&(&(&scale * &scale) * &r2) * &a6))
    } else {
        // Q far enough inside: squared distance k2 (N - k2) / (4 |A|^6), zero on a ray
        le(&(&k2 * &(&n - &k2)), &(&(&scale * &r2) * &a6))
    };
    if inside {
        "YES"
    } else {
        "NO"
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let t: usize = it.next().unwrap().parse().unwrap();
    let mut out = String::new();
    for _ in 0..t {
        let mut read = || Big::parse(it.next().unwrap());
        // tuple fields are read from left to right
        let (a, b, c, d, e, f) = (read(), read(), read(), read(), read(), read());
        let (px, py, r) = (read(), read(), read());
        out.push_str(answer((&a, &b, &c, &d, &e, &f), &px, &py, &r));
        out.push('\n');
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}
