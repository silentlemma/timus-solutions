use std::io::{self, Read};

const VERTEX_COUNT: usize = 3;
const DECIMAL_PLACES: usize = 10;
const SCALE: i128 = 10_000_000_000;

#[derive(Clone, Copy)]
struct Point {
    x: i64,
    y: i64,
}

fn subtract(a: Point, b: Point) -> Point {
    Point {
        x: a.x - b.x,
        y: a.y - b.y,
    }
}

fn dot(a: Point, b: Point) -> i64 {
    a.x * b.x + a.y * b.y
}

fn cross(a: Point, b: Point) -> i64 {
    a.x * b.y - a.y * b.x
}

fn consider(numerator: i128, denominator: i128, best: &mut i128, count: &mut i64) {
    let rounded = (numerator * SCALE + denominator / 2) / denominator;
    *best = (*best).max(rounded);
    *count += 1;
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut values = input
        .split_whitespace()
        .map(|value| value.parse::<i64>().unwrap());
    let mut vertices = [Point { x: 0, y: 0 }; VERTEX_COUNT];
    for point in &mut vertices {
        point.x = values.next().unwrap();
        point.y = values.next().unwrap();
    }
    let hole = Point {
        x: values.next().unwrap(),
        y: values.next().unwrap(),
    };

    let mut best = 0;
    let mut count = 0;
    for index in 0..VERTEX_COUNT {
        let origin = vertices[index];
        let base = subtract(vertices[(index + 1) % VERTEX_COUNT], origin);
        let apex = subtract(vertices[(index + 2) % VERTEX_COUNT], origin);
        let inside = subtract(hole, origin);
        let length = dot(base, base);
        let projection = dot(base, apex);
        if projection < 0 || projection >= length {
            continue;
        }

        let position = dot(base, inside);
        let height = cross(base, apex).abs() as i128;
        let offset = cross(base, inside).abs() as i128;
        // Omitting one right-angle base also removes all repeated rectangles.
        consider(offset * (height - offset), height, &mut best, &mut count);
        if position < projection {
            consider(
                height * position as i128 * (projection - position) as i128,
                projection as i128 * projection as i128,
                &mut best,
                &mut count,
            );
        } else if position > projection {
            let remaining = (length - projection) as i128;
            consider(
                height * (length - position) as i128 * (position - projection) as i128,
                remaining * remaining,
                &mut best,
                &mut count,
            );
        }
    }

    println!(
        "{}.{:0width$}\n{}",
        best / SCALE,
        best % SCALE,
        count,
        width = DECIMAL_PLACES
    );
}
