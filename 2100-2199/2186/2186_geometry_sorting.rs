use std::cmp::Ordering;
use std::f64::consts::PI;
use std::io::{self, Read};

const PROBABILITY_SCALE: usize = 100_000;
const PROBABILITY_DIGITS: usize = 5;
const OUTPUT_DIGITS: usize = 10;
const HALF_TURN: f64 = 180.0;
const FULL_TURN: f64 = 2.0 * PI;
const ANGLE_EPSILON: f64 = 1e-12;
const PROBABILITY_EPSILON: f64 = 1e-7;
const BIG_DIGITS: usize = 9;
const BIG_BASE: u128 = 1_000_000_000;

#[derive(Clone, Copy)]
struct Big {
    digits: [u64; BIG_DIGITS],
}

impl Big {
    fn one() -> Self {
        let mut result = Self {
            digits: [0; BIG_DIGITS],
        };
        result.digits[0] = 1;
        result
    }

    fn multiply(&mut self, value: u64) {
        let mut carry = 0;
        for digit in &mut self.digits {
            let current = *digit as u128 * value as u128 + carry;
            *digit = (current % BIG_BASE) as u64;
            carry = current / BIG_BASE;
        }
    }

    fn compare(&self, other: &Self) -> Ordering {
        self.digits.iter().rev().cmp(other.digits.iter().rev())
    }
}

fn power(value: u64, exponent: usize) -> Big {
    let mut result = Big::one();
    for _ in 0..exponent {
        result.multiply(value);
    }
    result
}

#[derive(Clone, Copy)]
struct Gun {
    x: i64,
    y: i64,
    norm: u64,
    angle: f64,
}

fn normalize(angle: f64) -> f64 {
    let result = angle % FULL_TURN;
    if result < 0.0 {
        result + FULL_TURN
    } else {
        result
    }
}

fn fits(first: Gun, last: Gun, delta: f64, width: f64, distance: u64, cosine: i64) -> bool {
    if (delta - width).abs() > ANGLE_EPSILON {
        return delta < width;
    }
    let cross = first.x * last.y - first.y * last.x;
    let dot = first.x * last.x + first.y * last.y;
    if cross < 0 {
        return false;
    }
    if cross == 0 {
        return dot > 0;
    }
    if dot >= 0 && cosine < 0 {
        return true;
    }
    if dot < 0 && cosine >= 0 {
        return false;
    }
    // Compare boundary cosines exactly when angles are almost equal.
    let mut left = Big::one();
    left.multiply(dot.unsigned_abs());
    left.multiply(dot.unsigned_abs());
    left.multiply(distance);
    left.multiply(distance);
    let mut right = Big::one();
    right.multiply(cosine.unsigned_abs());
    right.multiply(cosine.unsigned_abs());
    right.multiply(first.norm);
    right.multiply(last.norm);
    let order = left.compare(&right);
    if cosine >= 0 {
        order != Ordering::Less
    } else {
        order != Ordering::Greater
    }
}

fn probability(token: &str) -> usize {
    let mut value = 0;
    let mut digits = 0;
    let mut fraction = false;
    for byte in token.bytes() {
        if byte == b'.' {
            fraction = true;
        } else {
            value = value * 10 + (byte - b'0') as usize;
            if fraction {
                digits += 1;
            }
        }
    }
    while digits < PROBABILITY_DIGITS {
        value *= 10;
        digits += 1;
    }
    value
}

fn capacity(hits: usize, n: usize, shots: usize, total_power: &Big) -> usize {
    if shots == 1 {
        return PROBABILITY_SCALE * hits / n;
    }
    let miss = (n - hits) as f64 / n as f64;
    let scaled = PROBABILITY_SCALE as f64 * (1.0 - miss.powi(shots as i32));
    let mut result = scaled.floor() as usize;
    if (scaled - scaled.round()).abs() < PROBABILITY_EPSILON {
        // Decimal query boundaries require an exact integer comparison.
        let mut left = power((n - hits) as u64, shots);
        left.multiply(PROBABILITY_SCALE as u64);
        while result > 0 {
            let mut right = *total_power;
            right.multiply((PROBABILITY_SCALE - result) as u64);
            if left.compare(&right) != Ordering::Greater {
                break;
            }
            result -= 1;
        }
        while result < PROBABILITY_SCALE {
            let mut right = *total_power;
            right.multiply((PROBABILITY_SCALE - result - 1) as u64);
            if left.compare(&right) == Ordering::Greater {
                break;
            }
            result += 1;
        }
    }
    result
}

fn format_angle(angle: f64) -> String {
    format!(
        "{:.precision$}",
        angle * HALF_TURN / PI,
        precision = OUTPUT_DIGITS
    )
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let n: usize = tokens.next().unwrap().parse().unwrap();
    let shots: usize = tokens.next().unwrap().parse().unwrap();
    let queries: usize = tokens.next().unwrap().parse().unwrap();
    let mut guns = Vec::with_capacity(n);
    for _ in 0..n {
        let x: i64 = tokens.next().unwrap().parse().unwrap();
        let y: i64 = tokens.next().unwrap().parse().unwrap();
        guns.push(Gun {
            x,
            y,
            norm: (x * x + y * y) as u64,
            angle: (y as f64).atan2(x as f64),
        });
    }
    let a: i64 = tokens.next().unwrap().parse().unwrap();
    let b: i64 = tokens.next().unwrap().parse().unwrap();
    let radius: i64 = tokens.next().unwrap().parse().unwrap();
    let distance = (a * a + b * b) as u64;
    let radius_squared = (radius * radius) as u64;
    let cosine = distance as i64 - 2 * radius_squared as i64;
    let center = (b as f64).atan2(a as f64);
    let half_width = (radius as f64).atan2(((distance - radius_squared) as f64).sqrt());
    let width = 2.0 * half_width;
    let mut active = 0;
    for gun in &guns {
        let dot = a * gun.x + b * gun.y;
        let cross = (a * gun.y - b * gun.x) as i128;
        let right = radius_squared as i128 * gun.norm as i128;
        if dot >= 0 && cross * cross <= right {
            active += 1;
        }
    }
    guns.sort_unstable_by(|first, last| {
        let order = first.angle.partial_cmp(&last.angle).unwrap();
        if order != Ordering::Equal {
            return order;
        }
        let cross = first.x * last.y - first.y * last.x;
        0.cmp(&cross)
    });
    let mut earliest = vec![f64::INFINITY; n + 1];
    earliest[0] = 0.0;
    earliest[active] = 0.0;
    let mut end = 0;
    for begin in 0..n {
        while end < begin + n {
            let last = guns[end % n];
            let mut delta = last.angle - guns[begin].angle;
            if end >= n {
                delta += FULL_TURN;
            }
            if !fits(guns[begin], last, delta, width, distance, cosine) {
                break;
            }
            end += 1;
        }
        let count = end - begin;
        let mut angle = normalize(center - half_width - guns[begin].angle);
        // Resolve which side of zero contains an almost tangent entry.
        if angle <= ANGLE_EPSILON || FULL_TURN - angle <= ANGLE_EPSILON {
            let cross = (a * guns[begin].y - b * guns[begin].x) as i128;
            let right = radius_squared as i128 * guns[begin].norm as i128;
            angle = if cross * cross < right {
                FULL_TURN - ANGLE_EPSILON
            } else {
                0.0
            };
        }
        earliest[count] = earliest[count].min(angle);
    }
    for count in (1..=n).rev() {
        earliest[count - 1] = earliest[count - 1].min(earliest[count]);
    }
    let total_power = power(n as u64, shots);
    let mut answers = vec![None; PROBABILITY_SCALE + 1];
    let mut assigned = 0;
    for (count, angle) in earliest.iter().enumerate() {
        if !angle.is_finite() {
            break;
        }
        let limit = capacity(count, n, shots, &total_power);
        if assigned <= limit {
            let answer = format_angle(*angle);
            while assigned <= limit {
                answers[assigned] = Some(answer.clone());
                assigned += 1;
            }
        }
    }
    let mut output = String::new();
    for _ in 0..queries {
        let query = probability(tokens.next().unwrap());
        output.push_str(answers[query].as_deref().unwrap_or("-1"));
        output.push('\n');
    }
    print!("{}", output);
}
