use std::io::{self, Read};

const SHOOTERS: usize = 3;
const INDEX_SUM: usize = 0 + 1 + 2;
const RATIO_DIGITS: usize = 16;
const OUTPUT_SCALE: usize = 100000;
const ROUND_EPS: f64 = 1e-8; // absorb floating-point noise at output rounding midpoints

type Chances = [f64; SHOOTERS];

struct Truel {
    acc: [f64; SHOOTERS],
    order: [usize; SHOOTERS],
    values: [String; SHOOTERS],
    stronger: usize,
    weaker: usize,
    attack: [bool; 2],
}

impl Truel {
    fn ratio(&self, first: usize, second: usize) -> f64 {
        let (a, b) = (&self.values[first], &self.values[second]);
        let (x, y) = (
            &a[..a.len().min(RATIO_DIGITS)],
            &b[..b.len().min(RATIO_DIGITS)],
        );
        let exponent = (a.len() - x.len()) as i32 - (b.len() - y.len()) as i32;
        (x.parse::<f64>().unwrap() / y.parse::<f64>().unwrap()) * 10.0_f64.powi(exponent)
    }

    /// Two left, first to shoot: first wins p / (p + q - p q).
    fn duel(&self, first: usize, second: usize) -> Chances {
        let (p, q) = (self.acc[first], self.acc[second]);
        let mut c = [0.0; SHOOTERS];
        if !less_than(&self.values[first], &self.values[second]) {
            c[first] = 1.0 / (1.0 + self.ratio(second, first) * (1.0 - p));
        } else {
            let r = self.ratio(first, second);
            c[first] = r / (1.0 + r * (1.0 - q));
        }
        c[second] = 1.0 - c[first];
        c
    }

    /// The duel left after a hit, with the next living shooter first.
    fn after_hit(&self, turn: usize, killed: usize) -> Chances {
        let mut first = self.order[(turn + 1) % SHOOTERS];
        if first == killed {
            first = self.order[(turn + 2) % SHOOTERS];
        }
        self.duel(first, INDEX_SUM - killed - first)
    }

    /// Chances when all three live and order[turn] shoots; A never misses,
    /// so the shooting stops at A's turn at the latest.
    fn three(&self, turn: usize) -> Chances {
        let shooter = self.order[turn];
        if shooter == 0 {
            return self.after_hit(turn, self.stronger);
        }
        let p = self.acc[shooter];
        let miss = self.three((turn + 1) % SHOOTERS);
        // the weaker shooter attacks A iff (1-h)^k (1-l) >= h; ties attack
        let next_is_stronger = (self.order[(turn + 1) % SHOOTERS] != 0) as usize;
        if shooter == self.weaker && !self.attack[next_is_stronger] {
            return miss;
        }
        let hit = self.after_hit(turn, 0);
        let mut mixed = [0.0; SHOOTERS];
        for i in 0..SHOOTERS {
            mixed[i] = p * hit[i] + (1.0 - p) * miss[i];
        }
        mixed
    }
}

fn canonical(s: &str) -> String {
    let trimmed = s.trim_start_matches('0');
    if trimmed.is_empty() {
        "0".to_string()
    } else {
        trimmed.to_string()
    }
}

fn less_than(a: &str, b: &str) -> bool {
    if a.len() != b.len() {
        a.len() < b.len()
    } else {
        a < b
    }
}

fn subtract(a: &str, b: &str) -> String {
    let mut digits = a.as_bytes().to_vec();
    let mut borrow = 0;
    for offset in 0..digits.len() {
        let i = digits.len() - 1 - offset;
        let other = if offset < b.len() {
            b.as_bytes()[b.len() - 1 - offset] - b'0'
        } else {
            0
        };
        let digit = (digits[i] - b'0') as i32 - borrow - other as i32;
        borrow = (digit < 0) as i32;
        digits[i] = b'0' + (digit + 10 * borrow) as u8;
    }
    canonical(&String::from_utf8(digits).unwrap())
}

fn multiply(a: &str, b: &str) -> String {
    let mut digits = vec![0; a.len() + b.len()];
    for (i, x) in a.bytes().rev().enumerate() {
        let mut carry = 0;
        for (j, y) in b.bytes().rev().enumerate() {
            let value = digits[i + j] + (x - b'0') * (y - b'0') + carry;
            digits[i + j] = value % 10;
            carry = value / 10;
        }
        digits[i + b.len()] = carry;
    }
    let result: String = digits
        .into_iter()
        .rev()
        .map(|d| (b'0' + d) as char)
        .collect();
    canonical(&result)
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let tokens: Vec<&str> = text.split_ascii_whitespace().collect();
    let precision = tokens
        .iter()
        .map(|s| s.split('.').nth(1).unwrap_or("").len())
        .max()
        .unwrap();
    let mut values: [String; SHOOTERS] = Default::default();
    let mut acc = [0.0; SHOOTERS];
    for i in 0..SHOOTERS {
        acc[i] = tokens[i].parse().unwrap();
        let fraction = tokens[i].split('.').nth(1).unwrap_or("").len();
        values[i] = canonical(&(tokens[i].replace('.', "") + &"0".repeat(precision - fraction)));
    }
    let stronger = if less_than(&values[1], &values[2]) {
        2
    } else {
        1
    };
    let weaker = INDEX_SUM - stronger;
    let scale = "1".to_string() + &"0".repeat(precision);
    let (high, low) = (&values[stronger], &values[weaker]);
    let complement = subtract(&scale, high);
    let product = multiply(&complement, &subtract(&scale, low));
    let bound = multiply(high, &scale);
    let attack = [
        low == "0" || !less_than(&product, &bound),
        low == "0" || !less_than(&multiply(&product, &complement), &multiply(&bound, &scale)),
    ];
    let mut truel = Truel {
        acc,
        order: [0; SHOOTERS],
        values,
        stronger,
        weaker,
        attack,
    };
    let mut total = [0.0; SHOOTERS];
    let mut orders = 0;
    for a in 0..SHOOTERS {
        for b in (0..SHOOTERS).filter(|&b| b != a) {
            truel.order = [a, b, INDEX_SUM - a - b];
            let c = truel.three(0);
            for i in 0..SHOOTERS {
                total[i] += c[i];
            }
            orders += 1;
        }
    }
    let share = 1.0 / orders as f64;
    let mut rounded = [0; SHOOTERS];
    for i in 0..SHOOTERS {
        rounded[i] = (total[i] * share * OUTPUT_SCALE as f64 + 0.5 + ROUND_EPS) as usize;
    }
    println!(
        "{}.{:05} {}.{:05} {}.{:05}",
        rounded[0] / OUTPUT_SCALE,
        rounded[0] % OUTPUT_SCALE,
        rounded[1] / OUTPUT_SCALE,
        rounded[1] % OUTPUT_SCALE,
        rounded[2] / OUTPUT_SCALE,
        rounded[2] % OUTPUT_SCALE
    );
}
