use std::cmp::Ordering;
use std::io::{self, Read};

const DIM: usize = 3;
const COMPONENTS: usize = 2 * DIM;
const LIMB_DIGITS: usize = 9;
const BASE: i64 = 1_000_000_000;
const RATIO_LIMBS: usize = 3;
const OUTPUT_PRECISION: usize = 3;
// Coordinate differences are at most 10^9. The quadratic coefficients
// have magnitude at most 3 * 10^18, so the discriminant fits in i128.
const FIXED_LIMIT: i64 = 500_000_000;

#[derive(Clone, Default)]
struct Integer {
    // Little-endian magnitude. Zero has no limbs and is always nonnegative.
    limbs: Vec<i64>,
    negative: bool,
}

impl Integer {
    fn new(mut limbs: Vec<i64>, negative: bool) -> Self {
        while limbs.last() == Some(&0) {
            limbs.pop();
        }
        let negative = !limbs.is_empty() && negative;
        Self { limbs, negative }
    }

    fn is_zero(&self) -> bool {
        self.limbs.is_empty()
    }

    fn add(&self, other: &Self) -> Self {
        self.add_with_sign(other, other.negative)
    }

    fn sub(&self, other: &Self) -> Self {
        self.add_with_sign(other, !other.negative)
    }

    fn add_with_sign(&self, other: &Self, negative: bool) -> Self {
        if self.negative == negative {
            let count = self.limbs.len().max(other.limbs.len());
            let mut result = Vec::with_capacity(count + 1);
            let mut carry = 0;
            for i in 0..count {
                let sum =
                    self.limbs.get(i).unwrap_or(&0) + other.limbs.get(i).unwrap_or(&0) + carry;
                result.push(sum % BASE);
                carry = sum / BASE;
            }
            result.push(carry);
            return Self::new(result, negative);
        }
        let order = self
            .limbs
            .len()
            .cmp(&other.limbs.len())
            .then_with(|| self.limbs.iter().rev().cmp(other.limbs.iter().rev()));
        let (large, small, negative) = match order {
            Ordering::Equal => return Self::default(),
            Ordering::Greater => (&self.limbs, &other.limbs, self.negative),
            Ordering::Less => (&other.limbs, &self.limbs, negative),
        };
        let mut result = Vec::with_capacity(large.len());
        let mut borrow = 0;
        for (i, digit) in large.iter().enumerate() {
            let difference = digit - small.get(i).unwrap_or(&0) - borrow;
            borrow = i64::from(difference < 0);
            result.push(difference + BASE * borrow);
        }
        Self::new(result, negative)
    }

    fn mul(&self, other: &Self) -> Self {
        if self.is_zero() || other.is_zero() {
            return Self::default();
        }
        let mut result = vec![0; self.limbs.len() + other.limbs.len()];
        for (i, a) in self.limbs.iter().enumerate() {
            let mut carry = 0;
            for (j, b) in other.limbs.iter().enumerate() {
                let sum = a * b + result[i + j] + carry;
                result[i + j] = sum % BASE;
                carry = sum / BASE;
            }
            result[i + other.limbs.len()] = carry;
        }
        Self::new(result, self.negative != other.negative)
    }

    fn leading(&self) -> (f64, i32) {
        let start = self.limbs.len().saturating_sub(RATIO_LIMBS);
        let value = self.limbs[start..]
            .iter()
            .rev()
            .fold(0.0, |acc, digit| acc * BASE as f64 + *digit as f64);
        (value, start as i32)
    }

    fn absolute_ratio(&self, denominator: &Self) -> f64 {
        if self.is_zero() {
            return 0.0;
        }
        let (a, i) = self.leading();
        let (b, j) = denominator.leading();
        a / b * (BASE as f64).powi(i - j)
    }

    fn fixed(&self) -> Option<i128> {
        if self.limbs.len() > 1 {
            return None;
        }
        let value = self.limbs.first().copied().unwrap_or(0);
        if value > FIXED_LIMIT {
            return None;
        }
        Some(i128::from(if self.negative { -value } else { value }))
    }
}

struct Decimal {
    digits: Vec<u8>,
    exponent: i32,
    negative: bool,
}

impl Decimal {
    fn parse(token: &str) -> Self {
        let (mantissa, power) = token
            .split_once(['e', 'E'])
            .map_or((token, 0), |(m, e)| (m, e.parse::<i32>().unwrap()));
        let unsigned = mantissa.trim_start_matches(['+', '-']);
        let (whole, fraction) = unsigned.split_once('.').unwrap_or((unsigned, ""));
        let mut exponent = power - fraction.len() as i32;
        let mut digits: Vec<_> = whole
            .bytes()
            .chain(fraction.bytes())
            .skip_while(|&byte| byte == b'0')
            .collect();
        while digits.last() == Some(&b'0') {
            digits.pop();
            exponent += 1;
        }
        if digits.is_empty() {
            exponent = 0;
        }
        Self {
            digits,
            exponent,
            negative: token.starts_with('-'),
        }
    }

    fn scaled(mut self, exponent: i32) -> Integer {
        if self.digits.is_empty() {
            return Integer::default();
        }
        self.digits.resize(
            self.digits.len() + (self.exponent - exponent) as usize,
            b'0',
        );
        let limbs = self
            .digits
            .rchunks(LIMB_DIGITS)
            .map(|chunk| std::str::from_utf8(chunk).unwrap().parse().unwrap())
            .collect();
        Integer::new(limbs, self.negative)
    }
}

fn arrival(a: &[Integer; COMPONENTS], b: &[Integer; COMPONENTS], limit: &Integer) -> Option<f64> {
    let (mut projection, mut speed) = (Integer::default(), Integer::default());
    let mut gap = Integer::default().sub(limit);
    for k in 0..DIM {
        let p = b[k].sub(&a[k]);
        let v = b[k + DIM].sub(&a[k + DIM]);
        projection = projection.add(&p.mul(&v));
        speed = speed.add(&v.mul(&v));
        gap = gap.add(&p.mul(&p));
    }
    if !projection.negative {
        return None;
    }
    let square = projection.mul(&projection);
    let discriminant = square.sub(&speed.mul(&gap));
    if discriminant.negative {
        return None;
    }
    // With the sign settled exactly, the stable smaller root needs only ratios.
    let root = discriminant.absolute_ratio(&square).sqrt();
    Some(gap.absolute_ratio(&projection) / (1.0 + root))
}

fn fixed_arrival(a: &[i128; COMPONENTS], b: &[i128; COMPONENTS], limit: i128) -> Option<f64> {
    let (mut projection, mut speed, mut gap) = (0, 0, -limit);
    for k in 0..DIM {
        let p = b[k] - a[k];
        let v = b[k + DIM] - a[k + DIM];
        projection += p * v;
        speed += v * v;
        gap += p * p;
    }
    let discriminant = projection * projection - speed * gap;
    if projection >= 0 || discriminant < 0 {
        return None;
    }
    Some(gap as f64 / (-projection as f64 + (discriminant as f64).sqrt()))
}

fn search<T>(objects: &[T], collision: impl Fn(&T, &T) -> Option<f64>) {
    let mut best = f64::INFINITY;
    let mut pair = None;
    for (i, a) in objects.iter().enumerate() {
        for (j, b) in objects.iter().enumerate().skip(i + 1) {
            if let Some(time) = collision(a, b) {
                if time < best {
                    best = time;
                    pair = Some((i + 1, j + 1));
                }
            }
        }
    }
    match pair {
        Some((a, b)) => println!("ALARM!\n{best:.OUTPUT_PRECISION$} {a} {b}"),
        None => println!("OK"),
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_ascii_whitespace();
    let Some(count) = tokens.next() else {
        return;
    };
    let count: usize = count.parse().unwrap();
    let distance = Decimal::parse(tokens.next().unwrap());
    let values: Vec<_> = tokens
        .take(count * COMPONENTS)
        .map(Decimal::parse)
        .collect();
    let exponent = values
        .iter()
        .filter(|value| !value.digits.is_empty())
        .map(|value| value.exponent)
        .fold(distance.exponent, i32::min);
    let distance = distance.scaled(exponent);
    let mut scaled = values.into_iter().map(|value| value.scaled(exponent));
    let objects: Vec<[Integer; COMPONENTS]> = (0..count)
        .map(|_| std::array::from_fn(|_| scaled.next().unwrap()))
        .collect();

    if let Some(threshold) = distance.fixed() {
        let fixed: Option<Vec<_>> = objects
            .iter()
            .map(|object| {
                let mut result = [0i128; COMPONENTS];
                for (slot, value) in result.iter_mut().zip(object) {
                    *slot = value.fixed()?;
                }
                Some(result)
            })
            .collect();
        if let Some(fixed) = fixed {
            search(&fixed, |a, b| fixed_arrival(a, b, threshold * threshold));
            return;
        }
    }
    let limit = distance.mul(&distance);
    search(&objects, |a, b| arrival(a, b, &limit));
}
