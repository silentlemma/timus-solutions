use std::io::{self, Read, Write};

const MAX_DISTANCE: f64 = 3.0e9;
const CLOSE_DISTANCE: f64 = 1.0e-5;
const SPLITTER: f64 = 134217729.0;
const PI_HIGH: f64 = 3.141592653589793;
const PI_LOW: f64 = 1.2246467991473532e-16;

#[derive(Clone, Copy)]
struct DoubleDouble {
    high: f64,
    low: f64,
}

impl DoubleDouble {
    fn integer(value: i64) -> Self {
        let high = value as f64;
        Self {
            high,
            low: (value - high as i64) as f64,
        }
    }

    fn add(self, other: Self) -> Self {
        let sum = self.high + other.high;
        let part = sum - self.high;
        let error = (self.high - (sum - part)) + (other.high - part) + self.low + other.low;
        let high = sum + error;
        Self {
            high,
            low: error - (high - sum),
        }
    }

    fn subtract(self, other: Self) -> Self {
        self.add(Self {
            high: -other.high,
            low: -other.low,
        })
    }

    fn multiply(self, other: Self) -> Self {
        let product = self.high * other.high;
        let split_a = SPLITTER * self.high;
        let high_a = split_a - (split_a - self.high);
        let low_a = self.high - high_a;
        let split_b = SPLITTER * other.high;
        let high_b = split_b - (split_b - other.high);
        let low_b = other.high - high_b;
        let mut error = ((high_a * high_b - product) + high_a * low_b) + low_a * high_b;
        error += low_a * low_b + self.high * other.low + self.low * other.high;
        let high = product + error;
        Self {
            high,
            low: error - (high - product),
        }
    }

    fn nonnegative(self) -> bool {
        self.high > 0.0 || (self.high == 0.0 && self.low >= 0.0)
    }
}

#[derive(Clone, Copy)]
struct Point {
    x: i64,
    y: i64,
}

#[derive(Clone, Copy)]
struct Distance {
    value: f64,
    base: i64,
    denominator: i64,
    square: bool,
}

fn cross(ax: i64, ay: i64, bx: i64, by: i64) -> i64 {
    ax * by - ay * bx
}

struct Polygon {
    vertices: Vec<Point>,
    dx: Vec<i64>,
    dy: Vec<i64>,
    length_squared: Vec<i64>,
    rx: Vec<i64>,
    ry: Vec<i64>,
    radii: Vec<f64>,
    extras: Vec<DoubleDouble>,
    perimeter: f64,
    size: usize,
}

impl Polygon {
    fn new(input: Vec<Point>) -> Self {
        let count = input.len();
        let mut vertices = Vec::new();
        for i in 0..count {
            let previous = input[(i + count - 1) % count];
            let current = input[i];
            let next = input[(i + 1) % count];
            if cross(
                current.x - previous.x,
                current.y - previous.y,
                next.x - current.x,
                next.y - current.y,
            ) != 0
            {
                vertices.push(current);
            }
        }
        let size = vertices.len();
        let mut polygon = Self {
            vertices,
            dx: vec![0; size],
            dy: vec![0; size],
            length_squared: vec![0; size],
            rx: vec![0; size],
            ry: vec![0; size],
            radii: vec![0.0],
            extras: vec![DoubleDouble {
                high: 0.0,
                low: 0.0,
            }],
            perimeter: 0.0,
            size,
        };
        let mut correction = 0.0;
        let mut twice_area = 0_i64;
        for i in 0..size {
            let current = polygon.vertices[i];
            let next = polygon.vertices[(i + 1) % size];
            polygon.dx[i] = next.x - current.x;
            polygon.dy[i] = next.y - current.y;
            polygon.length_squared[i] =
                polygon.dx[i] * polygon.dx[i] + polygon.dy[i] * polygon.dy[i];
            polygon.rx[i] = current.x - polygon.vertices[0].x;
            polygon.ry[i] = current.y - polygon.vertices[0].y;
            let adjusted = (polygon.dx[i] as f64).hypot(polygon.dy[i] as f64) - correction;
            let total = polygon.perimeter + adjusted;
            correction = (total - polygon.perimeter) - adjusted;
            polygon.perimeter = total;
            if i > 1 {
                twice_area += cross(
                    polygon.rx[i - 1],
                    polygon.ry[i - 1],
                    polygon.rx[i],
                    polygon.ry[i],
                );
            }
        }
        let area = twice_area as f64 / 2.0;
        let half_perimeter = polygon.perimeter / 2.0;
        let mut multiplier = 1.0;
        let mut radius = 0.0;
        let exact_area = DoubleDouble::integer(twice_area).multiply(DoubleDouble {
            high: 1.0 / 2.0,
            low: 0.0,
        });
        let mut threshold = exact_area;
        // A + P*r + pi*r*r = A*2^day; use the stable positive root.
        while radius <= MAX_DISTANCE {
            threshold = threshold.add(threshold);
            polygon.extras.push(threshold.subtract(exact_area));
            multiplier *= 2.0;
            let extra = area * (multiplier - 1.0);
            radius = extra
                / (half_perimeter
                    + (half_perimeter * half_perimeter + std::f64::consts::PI * extra).sqrt());
            polygon.radii.push(radius);
        }
        polygon
    }

    fn visible(&self, edge: usize, query: Point) -> bool {
        cross(
            self.dx[edge],
            self.dy[edge],
            query.x - self.vertices[edge].x,
            query.y - self.vertices[edge].y,
        ) < 0
    }

    fn end_dot(&self, edge: usize, query: Point) -> i64 {
        let next = self.vertices[(edge + 1) % self.size];
        (next.x - query.x) * self.dx[edge] + (next.y - query.y) * self.dy[edge]
    }

    fn distance(&self, query: Point) -> Distance {
        let first = self.visible(0, query);
        let last = self.visible(self.size - 1, query);
        let (shown, hidden);
        if first != last {
            if first {
                shown = 0;
                hidden = self.size - 1;
            } else {
                shown = self.size - 1;
                hidden = 0;
            }
        } else {
            let qx = query.x - self.vertices[0].x;
            let qy = query.y - self.vertices[0].y;
            let (mut low, mut high) = (1, self.size - 1);
            while high - low > 1 {
                let middle = (low + high) / 2;
                let turn = cross(self.rx[middle], self.ry[middle], qx, qy);
                if if first { turn <= 0 } else { turn >= 0 } {
                    low = middle;
                } else {
                    high = middle;
                }
            }
            if first {
                shown = 0;
                hidden = low;
            } else {
                shown = low;
                hidden = 0;
                if !self.visible(shown, query) {
                    return Distance {
                        value: 0.0,
                        base: 0,
                        denominator: 1,
                        square: false,
                    };
                }
            }
        }

        let mut projection = (query.x - self.vertices[shown].x) * self.dx[shown]
            + (query.y - self.vertices[shown].y) * self.dy[shown];
        let mut closest = shown;
        // Restrict the derivative test to the visible chain to keep each search monotone.
        if projection > self.length_squared[shown] {
            let (mut low, mut high) = (0, (hidden + self.size - shown) % self.size);
            while high - low > 1 {
                let middle = (low + high) / 2;
                let edge = (shown + middle) % self.size;
                if !self.visible(edge, query) || self.end_dot(edge, query) >= 0 {
                    high = middle;
                } else {
                    low = middle;
                }
            }
            closest = (shown + high) % self.size;
        } else if projection < 0 {
            let (mut low, mut high) = (0, (shown + self.size - hidden) % self.size);
            while high - low > 1 {
                let middle = (low + high) / 2;
                let edge = (hidden + middle) % self.size;
                if self.visible(edge, query) && self.end_dot(edge, query) >= 0 {
                    high = middle;
                } else {
                    low = middle;
                }
            }
            closest = (hidden + high) % self.size;
        }

        let mut qx = query.x - self.vertices[closest].x;
        let mut qy = query.y - self.vertices[closest].y;
        projection = qx * self.dx[closest] + qy * self.dy[closest];
        if projection <= 0 {
            return Distance {
                value: (qx as f64).hypot(qy as f64),
                base: qx * qx + qy * qy,
                denominator: 1,
                square: false,
            };
        }
        if projection >= self.length_squared[closest] {
            let next = self.vertices[(closest + 1) % self.size];
            qx = query.x - next.x;
            qy = query.y - next.y;
            return Distance {
                value: (qx as f64).hypot(qy as f64),
                base: qx * qx + qy * qy,
                denominator: 1,
                square: false,
            };
        }
        let base = cross(self.dx[closest], self.dy[closest], qx, qy);
        Distance {
            value: (base as f64).abs() / (self.length_squared[closest] as f64).sqrt(),
            base,
            denominator: self.length_squared[closest],
            square: true,
        }
    }

    fn infected(&self, day: usize, separation: Distance) -> bool {
        let difference = self.radii[day] - separation.value;
        if difference.abs() > CLOSE_DISTANCE {
            return difference > 0.0;
        }
        // Squared distance is numerator/denominator; compare areas without a square root.
        let mut numerator = DoubleDouble::integer(separation.base);
        if separation.square {
            numerator = numerator.multiply(numerator);
        }
        let denominator = DoubleDouble::integer(separation.denominator);
        let remainder = self.extras[day].multiply(denominator).subtract(
            DoubleDouble {
                high: PI_HIGH,
                low: PI_LOW,
            }
            .multiply(numerator),
        );
        let boundary = DoubleDouble {
            high: self.perimeter,
            low: 0.0,
        };
        let left = boundary
            .multiply(boundary)
            .multiply(numerator)
            .multiply(denominator);
        remainder.nonnegative() && remainder.multiply(remainder).subtract(left).nonnegative()
    }

    fn day(&self, query: Point) -> usize {
        let separation = self.distance(query);
        if separation.value == 0.0 {
            return 0;
        }
        let (mut low, mut high) = (0, self.radii.len());
        while low < high {
            let middle = (low + high) / 2;
            if self.radii[middle] >= separation.value {
                high = middle;
            } else {
                low = middle + 1;
            }
        }
        while low > 0 && self.infected(low - 1, separation) {
            low -= 1;
        }
        while !self.infected(low, separation) {
            low += 1;
        }
        low
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let count: usize = tokens.next().unwrap().parse().unwrap();
    let mut vertices = Vec::with_capacity(count);
    for _ in 0..count {
        vertices.push(Point {
            x: tokens.next().unwrap().parse().unwrap(),
            y: tokens.next().unwrap().parse().unwrap(),
        });
    }
    let polygon = Polygon::new(vertices);
    let queries: usize = tokens.next().unwrap().parse().unwrap();
    let mut output = String::new();
    for _ in 0..queries {
        let query = Point {
            x: tokens.next().unwrap().parse().unwrap(),
            y: tokens.next().unwrap().parse().unwrap(),
        };
        output.push_str(&polygon.day(query).to_string());
        output.push('\n');
    }
    io::stdout().write_all(output.as_bytes()).unwrap();
}
