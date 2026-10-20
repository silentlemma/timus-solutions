use std::fmt::Write as FmtWrite;
use std::io::{self, Read, Write};

const FULL_TURN: i64 = 360000;
const QUARTER_TURN: i64 = 90000;
const OCTANT: i64 = 45000;
const HALF_TURN: f64 = 180000.0;
const PI: f64 = 3.141592653589793;
const BOUNDARY_EPSILON: f64 = 1e-11;
const MICRO_SCALE: i64 = 1000000;
const FRACTION_DIGITS: usize = 6;
const HALF: f64 = 0.5;
const SINE_COUNT: usize = 9;
const COSINE_COUNT: usize = 10;
const SINE_COEFFICIENTS: [f64; SINE_COUNT] = [
    2.8114572543455206e-15,
    -7.647163731819816e-13,
    1.6059043836821613e-10,
    -2.505210838544172e-08,
    2.7557319223985893e-06,
    -0.0001984126984126984,
    0.008333333333333333,
    -0.16666666666666666,
    1.0,
];
const COSINE_COEFFICIENTS: [f64; COSINE_COUNT] = [
    -1.5619206968586225e-16,
    4.779477332387385e-14,
    -1.1470745597729725e-11,
    2.08767569878681e-09,
    -2.755731922398589e-07,
    2.48015873015873e-05,
    -0.001388888888888889,
    0.041666666666666664,
    -HALF,
    1.0,
];

#[derive(Clone, Copy, Default)]
struct Point {
    x: i64,
    y: i64,
}

fn fixed(token: &str) -> i64 {
    let mut value = 0;
    let mut sign = 1;
    for ch in token.bytes() {
        if ch == b'-' {
            sign = -1;
        } else if ch != b'.' {
            value = value * 10 + i64::from(ch - b'0');
        }
    }
    sign * value
}

fn cross(a: Point, b: Point) -> i64 {
    a.x * b.y - a.y * b.x
}

fn sin_cos(angle: i64) -> (f64, f64) {
    let a = angle.rem_euclid(FULL_TURN);
    let quadrant = a / QUARTER_TURN;
    let mut r = a % QUARTER_TURN;
    let mirror = r > OCTANT;
    if mirror {
        r = QUARTER_TURN - r;
    }
    let x = r as f64 * (PI / HALF_TURN);
    let z = x * x;
    let mut sine = 0.0;
    let mut cosine = 0.0;
    for coefficient in SINE_COEFFICIENTS {
        sine = sine * z + coefficient;
    }
    for coefficient in COSINE_COEFFICIENTS {
        cosine = cosine * z + coefficient;
    }
    sine *= x;
    if r == OCTANT {
        sine = cosine;
    }
    if mirror {
        std::mem::swap(&mut sine, &mut cosine);
    }
    match quadrant {
        0 => (sine, cosine),
        1 => (cosine, -sine),
        2 => (-sine, -cosine),
        _ => (-cosine, sine),
    }
}

fn height(p: Point, sine: f64, cosine: f64) -> f64 {
    p.x as f64 * sine + p.y as f64 * cosine
}

fn capacity(points: &[Point], prefix: &[i64], angle: i64) -> f64 {
    let (sine, cosine) = sin_cos(angle);
    let first = height(points[0], sine, cosine);
    let total = prefix[points.len() - 1];
    if first == 0.0 {
        if cosine * points[0].x as f64 - sine * (points[0].y as f64) < 0.0 {
            return total as f64;
        }
        return 0.0;
    }
    let negative = first < 0.0;
    let mut lo = 0;
    let mut hi = points.len() - 1;
    while hi - lo > 1 {
        let mid = (lo + hi) / 2;
        if (height(points[mid], sine, cosine) < 0.0) == negative {
            lo = mid;
        } else {
            hi = mid;
        }
    }
    let left = height(points[lo], sine, cosine);
    let right = height(points[hi], sine, cosine);
    let mut t = left / (left - right);
    if t < 0.0 {
        t = 0.0;
    }
    if t > 1.0 {
        t = 1.0;
    }
    let triangle = (prefix[hi] - prefix[lo]) as f64;
    if negative {
        prefix[lo] as f64 + t * triangle
    } else {
        (total - prefix[hi]) as f64 + (1.0 - t) * triangle
    }
}

fn print_area(output: &mut String, area: f64) {
    let units = (area * HALF + HALF) as i64;
    writeln!(
        output,
        "{}.{:0width$}000",
        units / MICRO_SCALE,
        units % MICRO_SCALE,
        width = FRACTION_DIGITS
    )
    .unwrap();
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let n: usize = tokens.next().unwrap().parse().unwrap();
    let mut vertices = Vec::with_capacity(n);
    for _ in 0..n {
        vertices.push(Point {
            x: fixed(tokens.next().unwrap()),
            y: fixed(tokens.next().unwrap()),
        });
    }
    let hole = Point {
        x: fixed(tokens.next().unwrap()),
        y: fixed(tokens.next().unwrap()),
    };
    for point in &mut vertices {
        point.x -= hole.x;
        point.y -= hole.y;
    }
    let mut edge = 0;
    for i in 0..n {
        let a = vertices[i];
        let b = vertices[(i + 1) % n];
        if cross(a, b) == 0 && a.x * b.x + a.y * b.y < 0 {
            edge = i;
            break;
        }
    }
    let points: Vec<Point> = (0..n).map(|i| vertices[(edge + 1 + i) % n]).collect();
    let mut prefix = vec![0; n];
    for i in 1..n {
        prefix[i] = prefix[i - 1] + cross(points[i - 1], points[i]);
    }
    let first = points[0];
    let zero = -(first.y as f64).atan2(first.x as f64) * (HALF_TURN / PI);
    let (lower, upper) = if zero > 0.0 {
        (zero - FULL_TURN as f64, zero)
    } else {
        (zero, zero + FULL_TURN as f64)
    };
    let mut drained = first.y == 0 && first.x > 0;
    let mut remaining = capacity(&points, &prefix, 0);
    if drained {
        remaining = 0.0;
    }
    let mut output = String::new();
    print_area(&mut output, remaining);
    let q: usize = tokens.next().unwrap().parse().unwrap();
    let mut angle = 0;
    for _ in 0..q {
        angle += fixed(tokens.next().unwrap());
        if angle as f64 <= lower + BOUNDARY_EPSILON || angle as f64 >= upper - BOUNDARY_EPSILON {
            drained = true;
        }
        if drained {
            remaining = 0.0;
        } else {
            let current = capacity(&points, &prefix, angle);
            if current < remaining {
                remaining = current;
            }
        }
        print_area(&mut output, remaining);
    }
    io::stdout().lock().write_all(output.as_bytes()).unwrap();
}
