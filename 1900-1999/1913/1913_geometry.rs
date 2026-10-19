use std::io::{self, Read};

const TERMINALS: usize = 3;
const DISCRIMINANT_SCALE: i128 = 4;
type Point = (i128, i128);
type Position = (f64, f64);

fn squared_distance(first: Point, second: Point) -> i128 {
    let dx = first.0 - second.0;
    let dy = first.1 - second.1;
    dx * dx + dy * dy
}

fn radical_at_most(target: i128, coefficient: i128, radicand: i128) -> bool {
    if coefficient == 0 || radicand == 0 {
        return target >= 0;
    }
    let left = target * target;
    let right = coefficient * coefficient * radicand;
    if coefficient > 0 {
        return target >= 0 && left >= right;
    }
    target >= 0 || left <= right
}

fn common_point(points: &[Point; TERMINALS], radii: &[i128; TERMINALS]) -> Option<Position> {
    for &point in points {
        if (0..TERMINALS)
            .all(|index| squared_distance(point, points[index]) <= radii[index] * radii[index])
        {
            return Some((point.0 as f64, point.1 as f64));
        }
    }
    for first in 0..TERMINALS {
        for second in first + 1..TERMINALS {
            let third = TERMINALS - first - second;
            let origin = points[first];
            let dx = points[second].0 - origin.0;
            let dy = points[second].1 - origin.1;
            let distance = dx * dx + dy * dy;
            let radius_squared = radii[first] * radii[first];
            let along = distance + radius_squared - radii[second] * radii[second];
            let discriminant = DISCRIMINANT_SCALE * radius_squared * distance - along * along;
            if discriminant < 0 {
                continue;
            }
            let wx = origin.0 - points[third].0;
            let wy = origin.1 - points[third].1;
            let target = distance
                * (radii[third] * radii[third] - radius_squared - wx * wx - wy * wy)
                - along * (wx * dx + wy * dy);
            let cross = wy * dx - wx * dy;
            for sign in [-1, 1] {
                if radical_at_most(target, sign * cross, discriminant) {
                    let height = sign as f64 * (discriminant as f64).sqrt();
                    return Some((
                        origin.0 as f64
                            + (along as f64 * dx as f64 - height * dy as f64)
                                / (2 * distance) as f64,
                        origin.1 as f64
                            + (along as f64 * dy as f64 + height * dx as f64)
                                / (2 * distance) as f64,
                    ));
                }
            }
        }
    }
    None
}

fn solve(radius: i128, points: &[Point; TERMINALS]) -> Option<[Position; 2]> {
    let reach_squared = (2 * radius) * (2 * radius);
    if squared_distance(points[0], points[1]) <= reach_squared
        && squared_distance(points[0], points[2]) <= reach_squared
    {
        let mut answer = [(0.0, 0.0); 2];
        for index in 0..2 {
            answer[index] = (
                (points[0].0 + points[index + 1].0) as f64 / 2.0,
                (points[0].1 + points[index + 1].1) as f64 / 2.0,
            );
        }
        return Some(answer);
    }
    for doubled in 0..TERMINALS {
        let mut radii = [radius; TERMINALS];
        radii[doubled] *= 2;
        if let Some(hub) = common_point(points, &radii) {
            let midpoint = (
                (hub.0 + points[doubled].0 as f64) / 2.0,
                (hub.1 + points[doubled].1 as f64) / 2.0,
            );
            return Some([hub, midpoint]);
        }
    }
    None
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut values = input
        .split_whitespace()
        .map(|token| token.parse::<i128>().unwrap());
    let radius = values.next().unwrap();
    let mut points = [(0, 0); TERMINALS];
    for point in &mut points {
        *point = (values.next().unwrap(), values.next().unwrap());
    }
    if let Some(answer) = solve(radius, &points) {
        println!("Now we have enough power");
        for point in answer {
            println!("{:.12} {:.12}", point.0, point.1);
        }
    } else {
        println!("Death");
    }
}
