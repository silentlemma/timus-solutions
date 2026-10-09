use std::cmp::Ordering;
use std::io::{self, Read};

// Signed arbitrary-precision integers, stored in little-endian limbs.
#[derive(Clone)]
struct Integer {
    digits: Vec<u64>,
    negative: bool,
}

impl Integer {
    const BASE: u64 = 1 << 30;

    fn new(v: i64) -> Self {
        let mut u = v.abs() as u64;
        let mut digits = Vec::new();
        while u != 0 {
            digits.push(u % Self::BASE);
            u /= Self::BASE;
        }
        Self { digits, negative: v < 0 }
    }

    fn normalize(&mut self) {
        while self.digits.last() == Some(&0) {
            self.digits.pop();
        }
        if self.digits.is_empty() {
            self.negative = false;
        }
    }

    fn magnitude(&self, b: &Self) -> Ordering {
        self.digits.len().cmp(&b.digits.len())
            .then_with(|| self.digits.iter().rev().cmp(b.digits.iter().rev()))
    }

    fn cmp(&self, b: &Self) -> Ordering {
        if self.negative != b.negative {
            return if self.negative { Ordering::Less } else { Ordering::Greater };
        }
        if self.negative { b.magnitude(self) } else { self.magnitude(b) }
    }

    fn add(&self, b: &Self) -> Self {
        let mut out = Self::new(0);
        if self.negative == b.negative {
            out.negative = self.negative;
            let mut carry = 0;
            let mut i = 0;
            while i < self.digits.len().max(b.digits.len()) || carry != 0 {
                let v = carry + self.digits.get(i).unwrap_or(&0)
                    + b.digits.get(i).unwrap_or(&0);
                out.digits.push(v % Self::BASE);
                carry = v / Self::BASE;
                i += 1;
            }
        } else {
            let (hi, lo) = if self.magnitude(b) != Ordering::Less { (self, b) } else { (b, self) };
            out.negative = hi.negative;
            let mut borrow = 0;
            for i in 0..hi.digits.len() {
                let v = hi.digits[i] as i64 - borrow - *lo.digits.get(i).unwrap_or(&0) as i64;
                borrow = if v < 0 { 1 } else { 0 };
                out.digits.push(if v < 0 { (v + Self::BASE as i64) as u64 } else { v as u64 });
            }
        }
        out.normalize();
        out
    }

    fn sub(&self, b: &Self) -> Self {
        let mut other = b.clone();
        if !other.digits.is_empty() {
            other.negative = !other.negative;
        }
        self.add(&other)
    }

    fn mul(&self, b: &Self) -> Self {
        let mut out = Self {
            digits: vec![0; self.digits.len() + b.digits.len()],
            negative: self.negative != b.negative,
        };
        for i in 0..self.digits.len() {
            let mut carry = 0;
            let mut j = 0;
            while j < b.digits.len() || carry != 0 {
                let v = out.digits[i + j] + carry
                    + self.digits[i] * b.digits.get(j).unwrap_or(&0);
                out.digits[i + j] = v % Self::BASE;
                carry = v / Self::BASE;
                j += 1;
            }
        }
        out.normalize();
        out
    }

    fn scale(&self, v: i64) -> Self {
        self.mul(&Self::new(v))
    }

    fn abs(mut self) -> Self {
        self.negative = false;
        self
    }

    fn max0(self) -> Self {
        if self.negative { Self::new(0) } else { self }
    }

    fn parse(text: &str) -> Self {
        let mut out = Self::new(0);
        for c in text.bytes().filter(|c| c.is_ascii_digit()) {
            out = out.scale(10).add(&Self::new((c - b'0') as i64));
        }
        out.negative = text.starts_with('-') && !out.digits.is_empty();
        out
    }
}

// squared distances carry these denominators: a point scaled by 2, a square
// by its projections
const POINT_DEN: i64 = 4;
const SQUARE_DEN: i64 = 8;

// squared distance from P to the square with diagonal (x1, y1)-(x2, y2), as a
// numerator and a denominator
fn distance(x1: i64, y1: i64, x2: i64, y2: i64, px: &Integer, py: &Integer) -> (Integer, i64) {
    // doubled coordinates of P relative to the centre, and the diagonal
    let qx = px.scale(2).sub(&Integer::new(x1 + x2));
    let qy = py.scale(2).sub(&Integer::new(y1 + y2));
    let (dx, dy) = (x2 - x1, y2 - y1);
    let h = dx * dx + dy * dy;
    if h == 0 {
        return (qx.mul(&qx).add(&qy.mul(&qy)), POINT_DEN);
    }
    // projections on the two side directions, the diagonal turned by +-45
    // degrees; inside the square both stay within h
    let s1 = qx.scale(dx - dy).add(&qy.scale(dy + dx)).abs();
    let s2 = qx.scale(dx + dy).add(&qy.scale(dy - dx)).abs();
    let a = s1.sub(&Integer::new(h)).max0();
    let b = s2.sub(&Integer::new(h)).max0();
    (a.mul(&a).add(&b.mul(&b)), SQUARE_DEN * h)
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tok = input.split_ascii_whitespace();
    let n: usize = tok.next().unwrap().parse().unwrap();
    let squares: Vec<(i64, i64, i64, i64)> = (0..n).map(|_| {
        (tok.next().unwrap().parse().unwrap(), tok.next().unwrap().parse().unwrap(),
         tok.next().unwrap().parse().unwrap(), tok.next().unwrap().parse().unwrap())
    }).collect();
    let (px, py) = (Integer::parse(tok.next().unwrap()), Integer::parse(tok.next().unwrap()));
    let dist: Vec<(Integer, i64)> = squares
        .iter()
        .map(|&(x1, y1, x2, y2)| distance(x1, y1, x2, y2, &px, &py))
        .collect();
    // exact cross products, with the input index breaking ties
    let mut order: Vec<usize> = (0..n).collect();
    order.sort_unstable_by(|&i, &j| {
        dist[i].0.scale(dist[j].1).cmp(&dist[j].0.scale(dist[i].1)).then_with(|| i.cmp(&j))
    });
    let out: Vec<String> = order.iter().map(|i| (i + 1).to_string()).collect();
    println!("{}", out.join(" "));
}
