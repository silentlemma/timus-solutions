use std::io::{self, Read};

const FIRST_ODD: i128 = 3;
const MIN_HYPOTENUSE: i128 = 5;
const COORDINATES: usize = 6;

fn integer_root(value: i128) -> i128 {
    let (mut low, mut high) = (0, 1);
    while high * high <= value {
        high *= 2;
    }
    while high - low > 1 {
        let middle = (low + high) / 2;
        if middle * middle <= value {
            low = middle;
        } else {
            high = middle;
        }
    }
    low
}

fn gcd(mut a: i128, mut b: i128) -> i128 {
    while b != 0 {
        (a, b) = (b, a % b);
    }
    a
}

fn divisors(mut number: i128) -> Vec<i128> {
    let mut values = vec![1];
    let mut prime = 2;
    while prime * prime <= number {
        let previous = values.len();
        let mut power = 1;
        while number % prime == 0 {
            number /= prime;
            power *= prime;
            for i in 0..previous {
                values.push(values[i] * power);
            }
        }
        prime = if prime == 2 { FIRST_ODD } else { prime + 2 };
    }
    if number > 1 {
        let previous = values.len();
        for i in 0..previous {
            values.push(values[i] * number);
        }
    }
    values
}

struct Geometry {
    dot: i128,
    cross: i128,
    denominator: i128,
}

impl Geometry {
    fn point(&self, x: i128, y: i128) -> Option<[i128; COORDINATES]> {
        let u = self.dot * x - self.cross * y;
        let v = self.dot * y + self.cross * x;
        if u % self.denominator != 0 || v % self.denominator != 0 {
            return None;
        }
        Some([0, 0, x, y, u / self.denominator, v / self.denominator])
    }
}

fn solve(input: &[i128]) -> Option<[i128; COORDINATES]> {
    let mut sides = input.to_vec();
    sides.sort_unstable();
    let (radius, length, opposite) = (sides[0], sides[1], sides[2]);
    let twice_dot = radius * radius + length * length - opposite * opposite;
    if twice_dot % 2 != 0 {
        return None;
    }
    let dot = twice_dot / 2;
    let square = radius * radius * length * length - dot * dot;
    if square < 0 {
        return None;
    }
    let cross = integer_root(square);
    if cross * cross != square {
        return None;
    }
    let geometry = Geometry {
        dot,
        cross,
        denominator: radius * radius,
    };
    if let Some(answer) = geometry.point(radius, 0) {
        return Some(answer);
    }
    if let Some(answer) = geometry.point(0, radius) {
        return Some(answer);
    }
    for hypotenuse in divisors(radius) {
        if hypotenuse < MIN_HYPOTENUSE || hypotenuse % 2 == 0 {
            continue;
        }
        let mut m = integer_root(hypotenuse / 2) + 1;
        let end = integer_root(hypotenuse - 1);
        while m <= end {
            let rest = hypotenuse - m * m;
            let k = integer_root(rest);
            if k * k == rest && gcd(m, k) == 1 && (m - k) % 2 != 0 {
                let scale = radius / hypotenuse;
                let (x, y) = (scale * (m * m - k * k), scale * 2 * m * k);
                if let Some(answer) = geometry.point(x, y) {
                    return Some(answer);
                }
                if let Some(answer) = geometry.point(y, x) {
                    return Some(answer);
                }
            }
            m += 1;
        }
    }
    None
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let sides: Vec<i128> = input
        .split_whitespace()
        .map(|word| word.parse().unwrap())
        .collect();
    if sides.is_empty() {
        return;
    }
    match solve(&sides) {
        Some(answer) => {
            for pair in answer.chunks(2) {
                println!("{} {}", pair[0], pair[1]);
            }
        }
        None => println!("-1"),
    }
}
