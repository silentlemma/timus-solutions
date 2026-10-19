use std::cmp::Ordering;
use std::io::{self, Read};

const LIMB_BITS: usize = 32;
const LIMB_BASE: f64 = 4294967296.0;
const ROOT_DIGIT_MASK: u32 = 3;
const FLOAT_PRECISION: usize = 53;
const FRACTION_BITS: u32 = 52;
const EXPONENT_MASK: u64 = 2047;
const SUBNORMAL_EXPONENT: i32 = -1074;
const MANTISSA_EXPONENT_BIAS: i32 = 1075;
const INITIAL_ROOT_DIGITS: usize = 16;
const BOUND_ROOT_DIGITS: usize = 32;
const MISSING_PARENT: u8 = 255;
const MASK_KEY_BITS: usize = 16;

#[derive(Clone, PartialEq, Eq)]
struct Nat(Vec<u32>);

// Little-endian limbs are used only by the exact comparison fallback.
impl Nat {
    fn new(x: u64) -> Self {
        if x == 0 {
            Self(Vec::new())
        } else if x <= u32::MAX as u64 {
            Self(vec![x as u32])
        } else {
            Self(vec![x as u32, (x >> LIMB_BITS) as u32])
        }
    }

    fn trim(&mut self) {
        while self.0.last() == Some(&0) {
            self.0.pop();
        }
    }

    fn zero(&self) -> bool {
        self.0.is_empty()
    }

    fn cmp(&self, b: &Self) -> Ordering {
        if self.0.len() != b.0.len() {
            return self.0.len().cmp(&b.0.len());
        }
        for i in (0..self.0.len()).rev() {
            if self.0[i] != b.0[i] {
                return self.0[i].cmp(&b.0[i]);
            }
        }
        Ordering::Equal
    }

    fn add(&self, b: &Self) -> Self {
        let n = self.0.len().max(b.0.len());
        let mut v = Vec::with_capacity(n + 1);
        let mut carry = 0u64;
        for i in 0..n {
            let x = if i < self.0.len() {
                self.0[i] as u64
            } else {
                0
            };
            let y = if i < b.0.len() { b.0[i] as u64 } else { 0 };
            let sum = x + y + carry;
            v.push(sum as u32);
            carry = sum >> LIMB_BITS;
        }
        if carry != 0 {
            v.push(carry as u32);
        }
        Self(v)
    }

    fn sub(&self, b: &Self) -> Self {
        let mut v = self.clone();
        let mut borrow = 0u64;
        for i in 0..v.0.len() {
            let y = if i < b.0.len() { b.0[i] as u64 } else { 0 };
            let x = v.0[i] as u64;
            let rhs = y + borrow;
            v.0[i] = x.wrapping_sub(rhs) as u32;
            borrow = u64::from(x < rhs);
        }
        v.trim();
        v
    }

    fn mul(&self, b: &Self) -> Self {
        if self.zero() || b.zero() {
            return Self::new(0);
        }
        let mut v = vec![0u32; self.0.len() + b.0.len()];
        for i in 0..self.0.len() {
            let mut carry = 0u64;
            for j in 0..b.0.len() {
                let x = self.0[i] as u64 * b.0[j] as u64 + v[i + j] as u64 + carry;
                v[i + j] = x as u32;
                carry = x >> LIMB_BITS;
            }
            v[i + b.0.len()] = carry as u32;
        }
        let mut result = Self(v);
        result.trim();
        result
    }

    fn bits(&self) -> usize {
        match self.0.last() {
            Some(x) => {
                (self.0.len() - 1) * LIMB_BITS + (LIMB_BITS - x.leading_zeros() as usize) as usize
            }
            None => 0,
        }
    }

    fn zeros(&self) -> usize {
        for i in 0..self.0.len() {
            if self.0[i] != 0 {
                return i * LIMB_BITS + self.0[i].trailing_zeros() as usize;
            }
        }
        0
    }

    fn shl(&self, n: usize) -> Self {
        if self.zero() {
            return self.clone();
        }
        let words = n / LIMB_BITS;
        let shift = n % LIMB_BITS;
        let mut v = vec![0u32; words];
        let mut carry = 0u64;
        for &x in &self.0 {
            let y = ((x as u64) << shift) | carry;
            v.push(y as u32);
            carry = y >> LIMB_BITS;
        }
        if carry != 0 {
            v.push(carry as u32);
        }
        Self(v)
    }

    fn shr(&self, n: usize) -> Self {
        let words = n / LIMB_BITS;
        if words >= self.0.len() {
            return Self::new(0);
        }
        let shift = n % LIMB_BITS;
        let mut v = self.0[words..].to_vec();
        if shift != 0 {
            let mut carry = 0;
            for i in (0..v.len()).rev() {
                let x = v[i];
                v[i] = (x >> shift) | carry;
                carry = x << (LIMB_BITS - shift);
            }
        }
        let mut result = Self(v);
        result.trim();
        result
    }

    fn div(&self, b: &Self) -> Self {
        assert!(!b.zero());
        if self.cmp(b) == Ordering::Less {
            return Self::new(0);
        }
        if b.0.len() == 1 {
            let mut v = self.clone();
            let mut rem = 0u64;
            for i in (0..v.0.len()).rev() {
                let x = (rem << LIMB_BITS) | v.0[i] as u64;
                v.0[i] = (x / b.0[0] as u64) as u32;
                rem = x % b.0[0] as u64;
            }
            v.trim();
            return v;
        }
        let shift = self.bits() - b.bits();
        let mut divisor = b.shl(shift);
        let mut rem = self.clone();
        let mut v = vec![0u32; shift / LIMB_BITS + 1];
        for bit in (0..=shift).rev() {
            if rem.cmp(&divisor) != Ordering::Less {
                rem = rem.sub(&divisor);
                v[bit / LIMB_BITS] |= 1 << (bit % LIMB_BITS);
            }
            divisor = divisor.shr(1);
        }
        let mut result = Self(v);
        result.trim();
        result
    }

    fn gcd(&self, b: &Self) -> Self {
        if self.zero() {
            return b.clone();
        }
        if b.zero() {
            return self.clone();
        }
        let shift = self.zeros().min(b.zeros());
        let mut a = self.shr(self.zeros());
        let mut b = b.shr(b.zeros());
        loop {
            match a.cmp(&b) {
                Ordering::Equal => return a.shl(shift),
                Ordering::Greater => {
                    a = a.sub(&b);
                    a = a.shr(a.zeros());
                }
                Ordering::Less => {
                    b = b.sub(&a);
                    b = b.shr(b.zeros());
                }
            }
        }
    }

    fn sqrt(&self) -> Self {
        let mut root = Self::new(0);
        let mut rem = Self::new(0);
        for pair in (0..(self.bits() + 1) / 2).rev() {
            let bit = pair * 2;
            let digit = (self.0[bit / LIMB_BITS] >> (bit % LIMB_BITS)) & ROOT_DIGIT_MASK;
            rem = rem.shl(2).add(&Self::new(digit as u64));
            let trial = root.shl(2).add(&Self::new(1));
            root = root.shl(1);
            if rem.cmp(&trial) != Ordering::Less {
                rem = rem.sub(&trial);
                root = root.add(&Self::new(1));
            }
        }
        root
    }

    fn mantissa(&self) -> (f64, i32) {
        let shift = self.bits().saturating_sub(FLOAT_PRECISION);
        let top = self.shr(shift);
        let mut value = 0.0;
        for i in (0..top.0.len()).rev() {
            value = value * LIMB_BASE + top.0[i] as f64;
        }
        (value, shift as i32)
    }
}

#[derive(Clone, PartialEq, Eq)]
struct Rat {
    sign: i32,
    num: Nat,
    den: Nat,
}

impl Rat {
    fn new(sign: i32, num: Nat, den: Nat) -> Self {
        if num.zero() {
            return Self::int(0);
        }
        let g = num.gcd(&den);
        Self {
            sign,
            num: num.div(&g),
            den: den.div(&g),
        }
    }

    fn int(x: i64) -> Self {
        Self {
            sign: x.signum() as i32,
            num: Nat::new(x.unsigned_abs()),
            den: Nat::new(1),
        }
    }

    fn add(&self, b: &Self) -> Self {
        if self.sign == 0 {
            return b.clone();
        }
        if b.sign == 0 {
            return self.clone();
        }
        let g = self.den.gcd(&b.den);
        let left = self.den.div(&g);
        let right = b.den.div(&g);
        let x = self.num.mul(&right);
        let y = b.num.mul(&left);
        let den = self.den.mul(&right);
        if self.sign == b.sign {
            Self::new(self.sign, x.add(&y), den)
        } else if x.cmp(&y) != Ordering::Less {
            Self::new(self.sign, x.sub(&y), den)
        } else {
            Self::new(b.sign, y.sub(&x), den)
        }
    }

    fn mul(&self, b: &Self) -> Self {
        if self.sign == 0 || b.sign == 0 {
            return Self::int(0);
        }
        let g = self.num.gcd(&b.den);
        let h = b.num.gcd(&self.den);
        Self {
            sign: self.sign * b.sign,
            num: self.num.div(&g).mul(&b.num.div(&h)),
            den: self.den.div(&h).mul(&b.den.div(&g)),
        }
    }

    fn div_int(&self, x: i64) -> Self {
        Self::new(
            self.sign * x.signum() as i32,
            self.num.clone(),
            self.den.mul(&Nat::new(x.unsigned_abs())),
        )
    }

    fn cmp(&self, b: &Self) -> Ordering {
        if self.sign != b.sign {
            return self.sign.cmp(&b.sign);
        }
        let order = self.num.mul(&b.den).cmp(&b.num.mul(&self.den));
        if self.sign < 0 {
            order.reverse()
        } else {
            order
        }
    }

    fn float(x: f64) -> Self {
        if x == 0.0 {
            return Self::int(0);
        }
        let (mantissa, exponent) = float_parts(x.abs());
        let num = Nat::new(mantissa);
        let sign = if x < 0.0 { -1 } else { 1 };
        if exponent >= 0 {
            Self::new(sign, num.shl(exponent as usize), Nat::new(1))
        } else {
            Self::new(sign, num, Nat::new(1).shl((-exponent) as usize))
        }
    }

    fn approx(&self) -> f64 {
        let (num, a) = self.num.mantissa();
        let (den, b) = self.den.mantissa();
        self.sign as f64 * (num / den) * 2.0f64.powi(a - b)
    }
}

fn float_parts(x: f64) -> (u64, i32) {
    let bits = x.to_bits();
    let e = ((bits >> FRACTION_BITS) & EXPONENT_MASK) as i32;
    let m = bits & ((1u64 << FRACTION_BITS) - 1);
    if e == 0 {
        (m, SUBNORMAL_EXPONENT)
    } else {
        (m | (1u64 << FRACTION_BITS), e - MANTISSA_EXPONENT_BIAS)
    }
}

fn down(x: f64) -> f64 {
    if x == f64::NEG_INFINITY {
        x
    } else if x == 0.0 {
        -f64::from_bits(1)
    } else if x > 0.0 {
        f64::from_bits(x.to_bits() - 1)
    } else {
        f64::from_bits(x.to_bits() + 1)
    }
}

fn up(x: f64) -> f64 {
    -down(-x)
}

#[derive(Clone, Copy, Default)]
struct Interval {
    low: f64,
    high: f64,
}

impl Interval {
    fn exact(x: i64) -> Self {
        Self {
            low: x as f64,
            high: x as f64,
        }
    }
    fn add(self, b: Self) -> Self {
        Self {
            low: down(self.low + b.low),
            high: up(self.high + b.high),
        }
    }
    fn sub(self, b: Self) -> Self {
        Self {
            low: down(self.low - b.high),
            high: up(self.high - b.low),
        }
    }
    fn mul(self, b: Self) -> Self {
        let values = [
            self.low * b.low,
            self.low * b.high,
            self.high * b.low,
            self.high * b.high,
        ];
        let mut low = values[0];
        let mut high = low;
        for &x in &values[1..] {
            low = low.min(x);
            high = high.max(x);
        }
        Self {
            low: down(low),
            high: up(high),
        }
    }
    fn div(self, b: i64) -> Self {
        Self {
            low: down(self.low / b as f64),
            high: up(self.high / b as f64),
        }
    }
    fn min(self, b: Self) -> Self {
        Self {
            low: self.low.min(b.low),
            high: self.high.min(b.high),
        }
    }
    fn max(self, b: Self) -> Self {
        Self {
            low: self.low.max(b.low),
            high: self.high.max(b.high),
        }
    }
    fn positive(self) -> Self {
        self.max(Self::default())
    }
}

#[derive(Clone, Copy, Default)]
struct Point {
    x: i64,
    y: i64,
}
#[derive(Clone, Copy)]
struct Aura {
    cap: i64,
    rise: i64,
    fall: i64,
}
#[derive(Clone)]
struct Spell {
    kind: u8,
    power: i64,
    duration: i64,
    places: Vec<Point>,
}

fn squared_distance(a: Point, b: Point) -> i64 {
    let x = a.x - b.x;
    let y = a.y - b.y;
    x * x + y * y
}

fn travel(a: Point, b: Point, speed: i64) -> f64 {
    (squared_distance(a, b) as f64).sqrt() / speed as f64
}

fn check_travel(x: f64, speed: i64, squared: i64) -> Ordering {
    let (m, e) = float_parts(x);
    let value = Nat::new(m).mul(&Nat::new(speed as u64));
    let mut left = value.mul(&value);
    let mut right = Nat::new(squared as u64);
    if e >= 0 {
        left = left.shl((2 * e) as usize);
    } else {
        right = right.shl((-2 * e) as usize);
    }
    left.cmp(&right)
}

fn travel_interval(a: Point, b: Point, speed: i64) -> Interval {
    let squared = squared_distance(a, b);
    if squared == 0 {
        return Interval::default();
    }
    let value = travel(a, b, speed);
    let mut low = down(value);
    let mut high = up(value);
    while check_travel(low, speed, squared) == Ordering::Greater {
        low = down(low);
    }
    while check_travel(high, speed, squared) == Ordering::Less {
        high = up(high);
    }
    Interval { low, high }
}

#[derive(Clone, Copy)]
struct AuraValue {
    power: f64,
    damage: f64,
    deficit: f64,
}

fn aura_float(start: f64, a: Aura, running: f64, duration: f64) -> AuraValue {
    let (cap, rise, fall) = (a.cap as f64, a.rise as f64, a.fall as f64);
    let falling = running.min(start / fall);
    let after = 0.0f64.max(start - fall * running);
    let run_area = (start + after) * falling / 2.0;
    let run_loss = ((cap - start) + (cap - after)) * falling / 2.0 + cap * (running - falling);
    let casting = 0.0f64.max(duration - running);
    let rising = casting.min((cap - after) / rise);
    let final_power = cap.min(after + rise * casting);
    let cast_area = (after + final_power) * rising / 2.0 + cap * (casting - rising);
    let cast_loss = ((cap - after) + (cap - final_power)) * rising / 2.0;
    AuraValue {
        power: final_power,
        damage: run_area + cast_area,
        deficit: run_loss + cast_loss,
    }
}

fn aura_interval(
    start: Interval,
    a: Aura,
    running: Interval,
    duration: Interval,
) -> (Interval, Interval) {
    let cap = Interval::exact(a.cap);
    let falling = running.min(start.div(a.fall)).positive();
    let after = start.sub(Interval::exact(a.fall).mul(running)).positive();
    let casting = duration.sub(running).positive();
    let rising = casting
        .min(cap.sub(after).positive().div(a.rise))
        .positive();
    let final_power = cap.min(after.add(Interval::exact(a.rise).mul(casting)));
    let run = cap
        .sub(start)
        .positive()
        .add(cap.sub(after).positive())
        .mul(falling)
        .div(2)
        .add(cap.mul(running.sub(falling).positive()));
    let cast = cap
        .sub(after)
        .positive()
        .add(cap.sub(final_power).positive())
        .mul(rising)
        .div(2);
    (final_power, run.add(cast).positive())
}

// Distinct squarefree radicals give a canonical exact zero test.
#[derive(Clone, PartialEq, Eq)]
struct Surd(Vec<(u64, Rat)>);

impl Surd {
    fn int(x: i64) -> Self {
        if x == 0 {
            Self(Vec::new())
        } else {
            Self(vec![(1, Rat::int(x))])
        }
    }

    fn term(&mut self, key: u64, value: Rat) {
        if value.sign == 0 {
            return;
        }
        match self.0.binary_search_by_key(&key, |entry| entry.0) {
            Ok(i) => {
                let sum = self.0[i].1.add(&value);
                if sum.sign == 0 {
                    self.0.remove(i);
                } else {
                    self.0[i].1 = sum;
                }
            }
            Err(i) => self.0.insert(i, (key, value)),
        }
    }

    fn add(&self, b: &Self) -> Self {
        let mut result = self.clone();
        for (key, value) in &b.0 {
            result.term(*key, value.clone());
        }
        result
    }

    fn neg(&self) -> Self {
        let mut result = self.clone();
        for entry in &mut result.0 {
            entry.1.sign = -entry.1.sign;
        }
        result
    }

    fn sub(&self, b: &Self) -> Self {
        self.add(&b.neg())
    }

    fn mul(&self, b: &Self) -> Self {
        let mut result = Self::int(0);
        for (first, x) in &self.0 {
            for (second, y) in &b.0 {
                let common = gcd(*first, *second);
                let key = (first / common) * (second / common);
                result.term(key, x.mul(y).mul(&Rat::int(common as i64)));
            }
        }
        result
    }

    fn scale(&self, x: i64) -> Self {
        if x == 0 {
            return Self::int(0);
        }
        let mut result = self.clone();
        for entry in &mut result.0 {
            entry.1 = entry.1.mul(&Rat::int(x));
        }
        result
    }

    fn div(&self, x: i64) -> Self {
        let mut result = self.clone();
        for entry in &mut result.0 {
            entry.1 = entry.1.div_int(x);
        }
        result
    }
}

fn gcd(mut a: u64, mut b: u64) -> u64 {
    while b != 0 {
        let r = a % b;
        a = b;
        b = r;
    }
    a
}

struct Exact {
    roots: Vec<(u64, usize, Rat, Rat)>,
    factors: Vec<(i64, Surd)>,
}

impl Exact {
    fn new() -> Self {
        Self {
            roots: Vec::new(),
            factors: Vec::new(),
        }
    }

    fn root_bounds(&mut self, radicand: u64, digits: usize) -> (Rat, Rat) {
        for (key, precision, low, high) in &self.roots {
            if *key == radicand && *precision == digits {
                return (low.clone(), high.clone());
            }
        }
        let mut den = Nat::new(1);
        for _ in 0..digits {
            den = den.mul(&Nat::new(10));
        }
        let value = den.mul(&den).mul(&Nat::new(radicand)).sqrt();
        let low = Rat::new(1, value.clone(), den.clone());
        let high = Rat::new(1, value.add(&Nat::new(1)), den);
        self.roots
            .push((radicand, digits, low.clone(), high.clone()));
        (low, high)
    }

    fn bound(&mut self, a: &Surd, digits: usize) -> (Rat, Rat) {
        let mut low = Rat::int(0);
        let mut high = Rat::int(0);
        for (key, value) in &a.0 {
            if *key == 1 {
                low = low.add(value);
                high = high.add(value);
            } else {
                let (mut left, mut right) = self.root_bounds(*key, digits);
                if value.sign < 0 {
                    std::mem::swap(&mut left, &mut right);
                }
                low = low.add(&value.mul(&left));
                high = high.add(&value.mul(&right));
            }
        }
        (low, high)
    }

    fn sign(&mut self, a: &Surd) -> i32 {
        if a.0.is_empty() {
            return 0;
        }
        if a.0.len() == 1 {
            return a.0[0].1.sign;
        }
        let mut digits = INITIAL_ROOT_DIGITS;
        loop {
            let (low, high) = self.bound(a, digits);
            if low.sign > 0 {
                return 1;
            }
            if high.sign < 0 {
                return -1;
            }
            digits *= 2;
        }
    }

    fn cmp(&mut self, a: &Surd, b: &Surd) -> i32 {
        self.sign(&a.sub(b))
    }

    fn min(&mut self, a: Surd, b: Surd) -> Surd {
        if self.cmp(&a, &b) <= 0 {
            a
        } else {
            b
        }
    }

    fn max(&mut self, a: Surd, b: Surd) -> Surd {
        if self.cmp(&a, &b) >= 0 {
            a
        } else {
            b
        }
    }

    fn float_bounds(&mut self, a: &Surd) -> Interval {
        let (left, right) = self.bound(a, BOUND_ROOT_DIGITS);
        let mut low = left.approx();
        let mut high = right.approx();
        while Rat::float(low).cmp(&left) == Ordering::Greater {
            low = down(low);
        }
        while Rat::float(high).cmp(&right) == Ordering::Less {
            high = up(high);
        }
        Interval { low, high }
    }

    fn square_root(&mut self, value: i64) -> Surd {
        if value == 0 {
            return Surd::int(0);
        }
        for (key, result) in &self.factors {
            if *key == value {
                return result.clone();
            }
        }
        let (mut remaining, mut outside, mut inside) = (value, 1, 1);
        let mut divisor = 2;
        while divisor * divisor <= remaining {
            let mut count = 0;
            while remaining % divisor == 0 {
                remaining /= divisor;
                count += 1;
            }
            for _ in 0..count / 2 {
                outside *= divisor;
            }
            if count % 2 != 0 {
                inside *= divisor;
            }
            divisor += 1;
        }
        let result = Surd(vec![((inside * remaining) as u64, Rat::int(outside))]);
        self.factors.push((value, result.clone()));
        result
    }

    fn travel(&mut self, a: Point, b: Point, speed: i64) -> Surd {
        self.square_root(squared_distance(a, b)).div(speed)
    }

    fn aura(
        &mut self,
        start: &Surd,
        a: Aura,
        running: &Surd,
        duration: &Surd,
        healing: bool,
    ) -> (Surd, Surd) {
        let cap = Surd::int(a.cap);
        let after = self.max(Surd::int(0), start.sub(&running.scale(a.fall)));
        let final_power = self.min(cap.clone(), after.add(&duration.sub(running).scale(a.rise)));
        let run = start.mul(start).sub(&after.mul(&after)).div(2 * a.fall);
        let left = cap.sub(&after);
        let right = cap.sub(&final_power);
        let deficit = left.mul(&left).sub(&right.mul(&right)).div(2 * a.rise);
        let metric = if healing {
            running.scale(a.cap).sub(&run).add(&deficit)
        } else {
            run.add(&duration.sub(running).scale(a.cap)).sub(&deficit)
        };
        (final_power, metric)
    }
}

type ExactWeights = Vec<Vec<Vec<Surd>>>;
type FloatWeights = Vec<Vec<Vec<f64>>>;

#[derive(Clone)]
struct Block {
    attackers: Vec<Aura>,
    healers: Vec<Aura>,
    health: i64,
    speed: i64,
    start: Point,
    breaths: Vec<Spell>,
    storm: Spell,
    initial: bool,
}

impl Block {
    fn exact_group(&self, auras: &[Aura], healing: bool, exact: &mut Exact) -> ExactWeights {
        let first = if self.breaths.is_empty() {
            &self.storm
        } else {
            &self.breaths[0]
        };
        let size = first.places.len();
        let mut outgoing = Vec::new();
        for &p in &first.places {
            outgoing.push(exact.travel(self.start, p, self.speed));
        }
        let mut returning = Vec::new();
        let mut latest = outgoing[0].clone();
        if let Some(last) = self.breaths.last() {
            latest = Surd::int(0);
            for &p in &last.places {
                let t = exact.travel(p, self.storm.places[0], self.speed);
                latest = exact.max(latest, t.clone());
                returning.push(t);
            }
        }
        let pairs = self.breaths.len() == 2;
        let mut between = vec![Vec::new(); size];
        if pairs {
            for i in 0..size {
                for &q in &self.breaths[1].places {
                    between[i].push(exact.travel(first.places[i], q, self.speed));
                }
            }
        }
        let mut result = Vec::new();
        for &a in auras {
            let initial_power = Surd::int(if self.initial && !healing { 0 } else { a.cap });
            let mut person = Vec::new();
            for left in 0..size {
                let duration = if healing && self.breaths.is_empty() {
                    latest.clone()
                } else {
                    Surd::int(first.duration)
                };
                let (power, metric) =
                    exact.aura(&initial_power, a, &outgoing[left], &duration, healing);
                let columns = if pairs { returning.len() } else { 1 };
                let mut row = Vec::new();
                for right in 0..columns {
                    let mut value = metric.clone();
                    if !self.breaths.is_empty() {
                        let mut at = power.clone();
                        let mut slot = left;
                        if pairs {
                            let (middle, extra) = exact.aura(
                                &power,
                                a,
                                &between[left][right],
                                &Surd::int(self.breaths[1].duration),
                                healing,
                            );
                            at = middle;
                            value = value.add(&extra);
                            slot = right;
                        }
                        let end = if healing {
                            latest.clone()
                        } else {
                            Surd::int(self.storm.duration)
                        };
                        let (_, extra) = exact.aura(&at, a, &returning[slot], &end, healing);
                        value = value.add(&extra);
                    }
                    row.push(value);
                }
                person.push(row);
            }
            result.push(person);
        }
        result
    }

    fn exact_budget(&self, exact: &mut Exact) -> Surd {
        let mut cap_sum = 0;
        for a in &self.healers {
            cap_sum += a.cap;
        }
        let mut fixed = 0;
        for s in &self.breaths {
            fixed += (s.power - cap_sum) * s.duration;
        }
        let mut latest = exact.travel(self.start, self.storm.places[0], self.speed);
        if let Some(last) = self.breaths.last() {
            latest = Surd::int(0);
            for &p in &last.places {
                let t = exact.travel(p, self.storm.places[0], self.speed);
                latest = exact.max(latest, t);
            }
        }
        Surd::int(self.health - fixed).sub(&latest.scale(self.storm.power - cap_sum))
    }
}

fn mask_places(mut mask: usize) -> Vec<usize> {
    let mut result = Vec::new();
    while mask != 0 {
        result.push(mask.trailing_zeros() as usize);
        mask &= mask - 1;
    }
    result
}

fn restrict_weights(
    weights: &ExactWeights,
    first: usize,
    second: usize,
    pairs: bool,
) -> ExactWeights {
    let first = mask_places(first);
    let second = if pairs { mask_places(second) } else { vec![0] };
    let mut result = Vec::new();
    for person in weights {
        let mut converted = Vec::new();
        for &a in &first {
            let mut row = Vec::new();
            for &b in &second {
                row.push(person[a][b].clone());
            }
            converted.push(row);
        }
        result.push(converted);
    }
    result
}

fn path(
    parent: &[u8],
    mut index: usize,
    mut people: usize,
    size: usize,
    pairs: bool,
) -> Vec<(usize, usize)> {
    let limit = 1 << size;
    let mut result = vec![(0, 0); people];
    while people > 0 {
        let code = parent[index] as usize;
        let (a, b) = if pairs {
            (code / size, code % size)
        } else {
            (code, 0)
        };
        result[people - 1] = (a, b);
        if pairs {
            let left = (index / limit) ^ (1 << a);
            let right = (index % limit) ^ (1 << b);
            index = left * limit + right;
        } else {
            index ^= 1 << a;
        }
        people -= 1;
    }
    result
}

fn compare_paths(
    weights: &ExactWeights,
    parent: &[u8],
    index: usize,
    target: usize,
    actor: usize,
    choice: (usize, usize),
    pairs: bool,
    exact: &mut Exact,
) -> bool {
    let mut candidate = path(parent, index, actor, weights.len(), pairs);
    candidate.push(choice);
    let incumbent = path(parent, target, actor + 1, weights.len(), pairs);
    let mut difference = Surd::int(0);
    for person in 0..candidate.len() {
        let (a, b) = candidate[person];
        let (c, d) = incumbent[person];
        if (a, b) != (c, d) {
            difference = difference.add(&weights[person][a][b].sub(&weights[person][c][d]));
        }
    }
    exact.sign(&difference) < 0
}

// Exact DP stores parent bytes and outward intervals, reconstructing close paths.
fn restricted_optimum(mut weights: ExactWeights, mut pairs: bool, exact: &mut Exact) -> Surd {
    let size = weights.len();
    let mut identical = true;
    for person in &weights[1..] {
        identical &= *person == weights[0];
    }
    if identical {
        if !pairs {
            let mut result = Surd::int(0);
            for row in &weights[0] {
                result = result.add(&row[0]);
            }
            return result;
        }
        let matrix = weights[0].clone();
        weights.clear();
        for row in &matrix {
            let mut person = Vec::new();
            for value in row {
                person.push(vec![value.clone()]);
            }
            weights.push(person);
        }
        pairs = false;
    }
    let limit = 1usize << size;
    let count = if pairs { limit * limit } else { limit };
    let mut lower = vec![f64::INFINITY; count];
    let mut upper = vec![f64::INFINITY; count];
    let mut parent = vec![MISSING_PARENT; count];
    lower[0] = 0.0;
    upper[0] = 0.0;
    let mut bounds = Vec::new();
    for person in &weights {
        let mut converted = Vec::new();
        for row in person {
            let mut values = Vec::new();
            for value in row {
                values.push(exact.float_bounds(value));
            }
            converted.push(values);
        }
        bounds.push(converted);
    }
    let layout = Layout::new(size);
    for actor in 0..size {
        let seconds: &[usize] = if pairs { &layout.groups[actor] } else { &[0] };
        for &left in &layout.groups[actor] {
            for &right in seconds {
                let index = if pairs { left * limit + right } else { left };
                if lower[index] == f64::INFINITY {
                    continue;
                }
                let mut free_a = (limit - 1) ^ left;
                while free_a != 0 {
                    let a = free_a.trailing_zeros() as usize;
                    let bit_a = 1 << a;
                    free_a ^= bit_a;
                    let mut free_b = if pairs { (limit - 1) ^ right } else { 1 };
                    while free_b != 0 {
                        let b = free_b.trailing_zeros() as usize;
                        let bit_b = 1 << b;
                        free_b ^= bit_b;
                        let target = if pairs {
                            (left | bit_a) * limit + (right | bit_b)
                        } else {
                            left | bit_a
                        };
                        let bound = bounds[actor][a][b];
                        let low = down(lower[index] + bound.low);
                        let high = up(upper[index] + bound.high);
                        let mut choose = lower[target] == f64::INFINITY || high < lower[target];
                        if !choose && low < upper[target] {
                            choose = compare_paths(
                                &weights,
                                &parent,
                                index,
                                target,
                                actor,
                                (a, b),
                                pairs,
                                exact,
                            );
                        }
                        if choose {
                            lower[target] = low;
                            upper[target] = high;
                            parent[target] = if pairs { (a * size + b) as u8 } else { a as u8 };
                        }
                    }
                }
            }
        }
    }
    let choices = path(&parent, count - 1, size, size, pairs);
    let mut result = Surd::int(0);
    for actor in 0..size {
        let (a, b) = choices[actor];
        result = result.add(&weights[actor][a][b]);
    }
    result
}

struct SurvivalRefiner {
    weights: ExactWeights,
    budget: Surd,
    pairs: bool,
    cache: Vec<(usize, bool)>,
}

impl SurvivalRefiner {
    fn new(block: &Block, exact: &mut Exact) -> Self {
        Self {
            weights: block.exact_group(&block.healers, true, exact),
            budget: block.exact_budget(exact),
            pairs: block.breaths.len() == 2,
            cache: Vec::new(),
        }
    }

    fn feasible(&mut self, first: usize, second: usize, exact: &mut Exact) -> bool {
        let key = (first << MASK_KEY_BITS) | second;
        for &(k, result) in &self.cache {
            if k == key {
                return result;
            }
        }
        let weights = restrict_weights(&self.weights, first, second, self.pairs);
        let mut low = Surd::int(0);
        let mut diagonal = Surd::int(0);
        for actor in 0..weights.len() {
            let person = &weights[actor];
            let mut best = person[0][0].clone();
            for row in person {
                for value in row {
                    best = exact.min(best, value.clone());
                }
            }
            low = low.add(&best);
            let column = if self.pairs { actor } else { 0 };
            diagonal = diagonal.add(&person[actor][column]);
        }
        let mut result = false;
        if exact.cmp(&low, &self.budget) < 0 {
            result = exact.cmp(&diagonal, &self.budget) < 0;
            if !result {
                let optimum = restricted_optimum(weights, self.pairs, exact);
                result = exact.cmp(&optimum, &self.budget) < 0;
            }
        }
        self.cache.push((key, result));
        result
    }
}

impl Block {
    fn group(&self, auras: &[Aura], healing: bool) -> (FloatWeights, f64) {
        let first = if self.breaths.is_empty() {
            &self.storm
        } else {
            &self.breaths[0]
        };
        let size = first.places.len();
        let mut outgoing = Vec::new();
        let mut out_bounds = Vec::new();
        for &p in &first.places {
            outgoing.push(travel(self.start, p, self.speed));
            out_bounds.push(travel_interval(self.start, p, self.speed));
        }
        let mut returning = Vec::new();
        let mut ret_bounds = Vec::new();
        let mut latest = outgoing[0];
        let mut latest_bounds = out_bounds[0];
        if let Some(last) = self.breaths.last() {
            latest = 0.0;
            latest_bounds = Interval::default();
            for &p in &last.places {
                let t = travel(p, self.storm.places[0], self.speed);
                let bound = travel_interval(p, self.storm.places[0], self.speed);
                returning.push(t);
                ret_bounds.push(bound);
                latest = latest.max(t);
                latest_bounds = latest_bounds.max(bound);
            }
        }
        let pairs = self.breaths.len() == 2;
        let mut between = vec![Vec::new(); size];
        let mut between_bounds = vec![Vec::new(); size];
        if pairs {
            for i in 0..size {
                for &q in &self.breaths[1].places {
                    between[i].push(travel(first.places[i], q, self.speed));
                    between_bounds[i].push(travel_interval(first.places[i], q, self.speed));
                }
            }
        }
        let mut result = Vec::new();
        let mut error = 0.0;
        let mut largest_sum = 0.0;
        for &a in auras {
            let initial_power = if self.initial && !healing { 0 } else { a.cap };
            let mut largest_error = 0.0f64;
            let mut largest_weight = 0.0f64;
            let mut person = Vec::new();
            for left in 0..size {
                let (duration, duration_bounds) = if healing && self.breaths.is_empty() {
                    (latest, latest_bounds)
                } else {
                    (first.duration as f64, Interval::exact(first.duration))
                };
                let state = aura_float(initial_power as f64, a, outgoing[left], duration);
                let (power_bound, loss_bound) = aura_interval(
                    Interval::exact(initial_power),
                    a,
                    out_bounds[left],
                    duration_bounds,
                );
                let columns = if pairs { size } else { 1 };
                let mut row = Vec::new();
                for right in 0..columns {
                    let mut value = if healing { state.deficit } else { state.damage };
                    let mut loss = loss_bound;
                    let mut area = Interval::exact(a.cap).mul(duration_bounds);
                    if !self.breaths.is_empty() {
                        let mut middle = state;
                        let mut middle_bound = power_bound;
                        let mut slot = left;
                        if pairs {
                            middle = aura_float(
                                state.power,
                                a,
                                between[left][right],
                                self.breaths[1].duration as f64,
                            );
                            let (power, extra) = aura_interval(
                                power_bound,
                                a,
                                between_bounds[left][right],
                                Interval::exact(self.breaths[1].duration),
                            );
                            middle_bound = power;
                            loss = loss.add(extra);
                            area = area.add(Interval::exact(a.cap * self.breaths[1].duration));
                            value += if healing {
                                middle.deficit
                            } else {
                                middle.damage
                            };
                            slot = right;
                        }
                        let (end, end_bound) = if healing {
                            (latest, latest_bounds)
                        } else {
                            (
                                self.storm.duration as f64,
                                Interval::exact(self.storm.duration),
                            )
                        };
                        let final_state = aura_float(middle.power, a, returning[slot], end);
                        let (_, extra) =
                            aura_interval(middle_bound, a, ret_bounds[slot], end_bound);
                        loss = loss.add(extra);
                        area = area.add(Interval::exact(a.cap).mul(end_bound));
                        value += if healing {
                            final_state.deficit
                        } else {
                            final_state.damage
                        };
                    }
                    let bound = if healing { loss } else { area.sub(loss) };
                    largest_error = up(largest_error
                        .max((value - bound.low).abs().max((bound.high - value).abs())));
                    largest_weight =
                        largest_weight.max(value.abs().max(bound.low.abs().max(bound.high.abs())));
                    row.push(value);
                }
                person.push(row);
            }
            result.push(person);
            error = up(error + largest_error);
            largest_sum = up(largest_sum + largest_weight);
        }
        let ulp = up(largest_sum) - largest_sum;
        (result, up(error + 2.0 * auras.len() as f64 * ulp))
    }
}

struct Layout {
    groups: Vec<Vec<usize>>,
    ranks: Vec<usize>,
    offsets: Vec<usize>,
}

impl Layout {
    fn new(size: usize) -> Self {
        let limit = 1usize << size;
        let mut groups = vec![Vec::new(); size + 1];
        let mut ranks = vec![0; limit];
        let mut offsets = vec![0; size + 2];
        for mask in 0..limit {
            let count = mask.count_ones() as usize;
            ranks[mask] = groups[count].len();
            groups[count].push(mask);
        }
        for count in 0..=size {
            offsets[count + 1] = offsets[count] + groups[count].len() * groups[count].len();
        }
        Self {
            groups,
            ranks,
            offsets,
        }
    }
}

struct CostTable {
    values: Vec<f64>,
    layout: Layout,
    pairs: bool,
}

impl CostTable {
    fn get(&self, first: usize, second: usize) -> f64 {
        let mut index = first;
        if self.pairs {
            let count = first.count_ones() as usize;
            index = self.layout.offsets[count]
                + self.layout.ranks[first] * self.layout.groups[count].len()
                + self.layout.ranks[second];
        }
        self.values[index]
    }
}

fn assignment(
    weights: &FloatWeights,
    size: usize,
    pairs: bool,
    maximize: bool,
    cutoff: f64,
) -> CostTable {
    let limit = 1usize << size;
    let layout = Layout::new(size);
    let count = if pairs {
        layout.offsets[weights.len() + 1]
    } else {
        limit
    };
    let mut result = vec![if maximize { -1.0 } else { cutoff }; count];
    result[0] = 0.0;
    for actor in 0..weights.len() {
        let person = &weights[actor];
        let seconds: &[usize] = if pairs { &layout.groups[actor] } else { &[0] };
        for &left in &layout.groups[actor] {
            for &right in seconds {
                let index = if pairs {
                    layout.offsets[actor]
                        + layout.ranks[left] * layout.groups[actor].len()
                        + layout.ranks[right]
                } else {
                    left
                };
                let current = result[index];
                if (maximize && current < 0.0) || (!maximize && current >= cutoff) {
                    continue;
                }
                let mut free_a = (limit - 1) ^ left;
                while free_a != 0 {
                    let a = free_a.trailing_zeros() as usize;
                    let bit_a = 1 << a;
                    free_a ^= bit_a;
                    let mut free_b = if pairs { (limit - 1) ^ right } else { 1 };
                    while free_b != 0 {
                        let b = free_b.trailing_zeros() as usize;
                        let bit_b = 1 << b;
                        free_b ^= bit_b;
                        let mut target = left | bit_a;
                        if pairs {
                            target = layout.offsets[actor + 1]
                                + layout.ranks[target] * layout.groups[actor + 1].len()
                                + layout.ranks[right | bit_b];
                        }
                        let candidate = current + person[a][b];
                        if (maximize && candidate > result[target])
                            || (!maximize && candidate < result[target])
                        {
                            result[target] = candidate;
                        }
                    }
                }
            }
        }
    }
    CostTable {
        values: result,
        layout,
        pairs,
    }
}

#[derive(Clone, Copy)]
struct Candidate {
    first: usize,
    second: usize,
    value: f64,
}

struct DamageCertificate {
    bounds: Interval,
    exact: Option<Surd>,
    block: Block,
    candidates: Vec<Candidate>,
    error: f64,
}

impl DamageCertificate {
    fn exact_value(&mut self, exact: &mut Exact) -> Surd {
        if self.exact.is_none() {
            self.exact = Some(
                self.block
                    .exact_damage(&mut self.candidates, self.error, exact),
            );
        }
        self.exact.as_ref().unwrap().clone()
    }
}

fn weight_extreme(person: &[Vec<Surd>], maximize: bool, exact: &mut Exact) -> Surd {
    let mut best = person[0][0].clone();
    for row in person {
        for value in row {
            best = if maximize {
                exact.max(best, value.clone())
            } else {
                exact.min(best, value.clone())
            };
        }
    }
    best
}

fn negative_weights(weights: &ExactWeights) -> ExactWeights {
    let mut result = Vec::new();
    for person in weights {
        let mut converted = Vec::new();
        for row in person {
            let mut values = Vec::new();
            for value in row {
                values.push(value.neg());
            }
            converted.push(values);
        }
        result.push(converted);
    }
    result
}

impl Block {
    fn exact_damage(&self, candidates: &mut [Candidate], error: f64, exact: &mut Exact) -> Surd {
        let weights = self.exact_group(&self.attackers, false, exact);
        if self.breaths.is_empty() {
            let mut result = Surd::int(0);
            for person in &weights {
                result = result.add(&person[0][0]);
            }
            return result;
        }
        let pairs = self.breaths.len() == 2;
        candidates.sort_unstable_by(|a, b| b.value.partial_cmp(&a.value).unwrap());
        let mut global_upper = Surd::int(0);
        for person in &weights {
            global_upper = global_upper.add(&weight_extreme(person, true, exact));
        }
        for choice in &*candidates {
            if pairs && choice.first != choice.second {
                continue;
            }
            let places = mask_places(choice.first);
            let mut diagonal = Surd::int(0);
            for actor in 0..places.len() {
                let place = places[actor];
                let column = if pairs { place } else { 0 };
                diagonal = diagonal.add(&weights[actor][place][column]);
            }
            if diagonal == global_upper {
                return global_upper;
            }
            break;
        }
        let mut best: Option<Surd> = None;
        let mut best_low = f64::NEG_INFINITY;
        for choice in &*candidates {
            if up(choice.value + error) < best_low {
                break;
            }
            let part = restrict_weights(&weights, choice.first, choice.second, pairs);
            let mut upper = Surd::int(0);
            let mut diagonal = Surd::int(0);
            for actor in 0..part.len() {
                upper = upper.add(&weight_extreme(&part[actor], true, exact));
                let column = if pairs { actor } else { 0 };
                diagonal = diagonal.add(&part[actor][actor][column]);
            }
            if let Some(old) = &best {
                if exact.cmp(&upper, old) <= 0 {
                    continue;
                }
            }
            let value = if diagonal == upper {
                upper
            } else {
                restricted_optimum(negative_weights(&part), pairs, exact).neg()
            };
            let improve = match &best {
                Some(old) => exact.cmp(&value, old) > 0,
                None => true,
            };
            if improve {
                if value == global_upper {
                    return value;
                }
                best_low = exact.float_bounds(&value).low;
                best = Some(value);
            }
        }
        best.unwrap()
    }

    fn survives(
        &self,
        value: f64,
        first: usize,
        second: usize,
        budget: f64,
        error: f64,
        refiner: &mut Option<SurvivalRefiner>,
        exact: &mut Exact,
    ) -> bool {
        if value == f64::INFINITY {
            return false;
        }
        if up(value + error) < budget {
            return true;
        }
        if down(value - error) >= budget {
            return false;
        }
        if self.breaths.is_empty() {
            let mut loss = Surd::int(0);
            for person in &self.exact_group(&self.healers, true, exact) {
                loss = loss.add(&person[0][0]);
            }
            let budget = self.exact_budget(exact);
            return exact.cmp(&loss, &budget) < 0;
        }
        if refiner.is_none() {
            *refiner = Some(SurvivalRefiner::new(self, exact));
        }
        refiner.as_mut().unwrap().feasible(first, second, exact)
    }

    fn damage(&self, exact: &mut Exact) -> Option<DamageCertificate> {
        let mut cap_sum = 0;
        for a in &self.healers {
            cap_sum += a.cap;
        }
        let mut fixed = 0;
        for s in &self.breaths {
            fixed += (s.power - cap_sum) * s.duration;
        }
        let mut latest = travel(self.start, self.storm.places[0], self.speed);
        let mut latest_bound = travel_interval(self.start, self.storm.places[0], self.speed);
        if let Some(last) = self.breaths.last() {
            latest = 0.0;
            latest_bound = Interval::default();
            for &p in &last.places {
                latest = latest.max(travel(p, self.storm.places[0], self.speed));
                latest_bound =
                    latest_bound.max(travel_interval(p, self.storm.places[0], self.speed));
            }
        }
        let budget = (self.health - fixed) as f64 - (self.storm.power - cap_sum) as f64 * latest;
        let budget_bound = Interval::exact(self.health - fixed)
            .sub(Interval::exact(self.storm.power - cap_sum).mul(latest_bound));
        if budget_bound.high <= 0.0 {
            return None;
        }
        let (healer_weights, mut error) = self.group(&self.healers, true);
        error = up(error
            + up((budget - budget_bound.low)
                .abs()
                .max((budget_bound.high - budget).abs())));
        let mut refiner = None;
        if self.breaths.is_empty() {
            let mut loss = 0.0;
            for person in &healer_weights {
                loss += person[0][0];
            }
            if !self.survives(loss, 0, 0, budget, error, &mut refiner, exact) {
                return None;
            }
            let (weights, damage_error) = self.group(&self.attackers, false);
            let mut value = 0.0;
            for person in &weights {
                value += person[0][0];
            }
            return Some(DamageCertificate {
                bounds: Interval {
                    low: down(value - damage_error),
                    high: up(value + damage_error),
                },
                exact: None,
                block: self.clone(),
                candidates: Vec::new(),
                error: damage_error,
            });
        }
        let size = self.attackers.len() + self.healers.len();
        let pairs = self.breaths.len() == 2;
        let limit = 1usize << size;
        let full = limit - 1;
        let mut masks = Vec::new();
        for mask in 0..limit {
            if mask.count_ones() as usize == self.healers.len() {
                masks.push(mask);
            }
        }
        let mut upper_loss = 0.0;
        for person in &healer_weights {
            let mut largest = 0.0f64;
            for row in person {
                for &value in row {
                    largest = largest.max(value);
                }
            }
            upper_loss = up(upper_loss + largest);
        }
        let all_survive = up(upper_loss + error) < budget;
        let survival = if all_survive {
            None
        } else {
            Some(assignment(
                &healer_weights,
                size,
                pairs,
                false,
                up(budget + error),
            ))
        };
        let seconds: &[usize] = if pairs { &masks } else { &[0] };
        let mut any = all_survive;
        if !any {
            'search: for &first in &masks {
                for &second in seconds {
                    let value = survival.as_ref().unwrap().get(first, second);
                    if self.survives(value, first, second, budget, error, &mut refiner, exact) {
                        any = true;
                        break 'search;
                    }
                }
            }
        }
        if !any {
            return None;
        }
        let (attacker_weights, damage_error) = self.group(&self.attackers, false);
        let damage = assignment(&attacker_weights, size, pairs, true, f64::INFINITY);
        let mut candidates = Vec::new();
        let mut best = f64::NEG_INFINITY;
        for &first in &masks {
            for &second in seconds {
                if let Some(table) = &survival {
                    if !self.survives(
                        table.get(first, second),
                        first,
                        second,
                        budget,
                        error,
                        &mut refiner,
                        exact,
                    ) {
                        continue;
                    }
                }
                let left = full ^ first;
                let right = if pairs { full ^ second } else { 0 };
                let value = damage.get(left, right);
                best = best.max(value);
                candidates.push(Candidate {
                    first: left,
                    second: right,
                    value,
                });
            }
        }
        let threshold = down(best - damage_error);
        let mut kept = Vec::new();
        for choice in candidates {
            if up(choice.value + damage_error) >= threshold {
                kept.push(choice);
            }
        }
        Some(DamageCertificate {
            bounds: Interval {
                low: down(best - damage_error),
                high: up(best + damage_error),
            },
            exact: None,
            block: self.clone(),
            candidates: kept,
            error: damage_error,
        })
    }
}

fn killed(amounts: &mut [DamageCertificate], health: i64, exact: &mut Exact) -> bool {
    let mut total = Interval::default();
    for amount in &*amounts {
        total = total.add(amount.bounds);
    }
    if total.low >= health as f64 {
        return true;
    }
    if total.high < health as f64 {
        return false;
    }
    let mut sum = Surd::int(0);
    for amount in amounts {
        sum = sum.add(&amount.exact_value(exact));
    }
    exact.cmp(&sum, &Surd::int(health)) >= 0
}

fn solve(
    attackers: Vec<Aura>,
    healers: Vec<Aura>,
    health: i64,
    speed: i64,
    dragon: i64,
    spells: Vec<Spell>,
) -> usize {
    let mut start = Point::default();
    let mut initial = true;
    let mut breaths = Vec::new();
    let mut amounts = Vec::new();
    let mut exact = Exact::new();
    for (index, s) in spells.into_iter().enumerate() {
        if s.kind == b'T' {
            break;
        }
        if s.kind == b'B' {
            breaths.push(s);
            continue;
        }
        let next_start = s.places[0];
        let current = Block {
            attackers: attackers.clone(),
            healers: healers.clone(),
            health,
            speed,
            start,
            breaths,
            storm: s,
            initial,
        };
        match current.damage(&mut exact) {
            Some(amount) => amounts.push(amount),
            None => return 0,
        }
        if killed(&mut amounts, dragon, &mut exact) {
            return index + 1;
        }
        start = next_start;
        initial = false;
        breaths = Vec::new();
    }
    0
}

struct Scanner {
    data: Vec<u8>,
    pos: usize,
}

impl Scanner {
    fn token(&mut self) -> &[u8] {
        while self.pos < self.data.len() && self.data[self.pos].is_ascii_whitespace() {
            self.pos += 1;
        }
        let start = self.pos;
        while self.pos < self.data.len() && !self.data[self.pos].is_ascii_whitespace() {
            self.pos += 1;
        }
        &self.data[start..self.pos]
    }

    fn int(&mut self) -> i64 {
        let token = self.token();
        let mut value = 0;
        let mut sign = 1;
        for &c in token {
            if c == b'-' {
                sign = -1;
            } else {
                value = value * 10 + (c - b'0') as i64;
            }
        }
        value * sign
    }

    fn auras(&mut self, count: usize) -> Vec<Aura> {
        let mut result = Vec::new();
        for _ in 0..count {
            result.push(Aura {
                cap: self.int(),
                rise: self.int(),
                fall: self.int(),
            });
        }
        result
    }
}

fn main() {
    let mut data = Vec::new();
    io::stdin().read_to_end(&mut data).unwrap();
    let mut input = Scanner { data, pos: 0 };
    let n = input.int() as usize;
    let m = input.int() as usize;
    let k = input.int() as usize;
    let health = input.int();
    let speed = input.int();
    let dragon = input.int();
    let attackers = input.auras(n);
    let healers = input.auras(m);
    let mut spells = Vec::new();
    for _ in 0..k {
        let kind = input.token()[0];
        let mut spell = Spell {
            kind,
            power: 0,
            duration: 0,
            places: Vec::new(),
        };
        if kind != b'T' {
            spell.power = input.int();
            spell.duration = input.int();
            let places = if kind == b'B' { n + m } else { 1 };
            for _ in 0..places {
                spell.places.push(Point {
                    x: input.int(),
                    y: input.int(),
                });
            }
        }
        spells.push(spell);
    }
    let answer = solve(attackers, healers, health, speed, dragon, spells);
    if answer == 0 {
        println!("You are not prepared");
    } else {
        println!("No useful loot again\n{}", answer);
    }
}
