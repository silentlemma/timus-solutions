use std::io::{self, Read};

#[derive(Clone, Copy)]
struct Vector {
    x: i128,
    y: i128,
    z: i128,
}

fn dot(a: Vector, b: Vector) -> i128 {
    a.x * b.x + a.y * b.y + a.z * b.z
}

fn subtract(a: Vector, b: Vector) -> Vector {
    Vector {
        x: a.x - b.x,
        y: a.y - b.y,
        z: a.z - b.z,
    }
}

fn scale(a: Vector, factor: i128) -> Vector {
    Vector {
        x: a.x * factor,
        y: a.y * factor,
        z: a.z * factor,
    }
}

fn cross(a: Vector, b: Vector) -> Vector {
    Vector {
        x: a.y * b.z - a.z * b.y,
        y: a.z * b.x - a.x * b.z,
        z: a.x * b.y - a.y * b.x,
    }
}

fn projection_sign(
    point: Vector,
    edge: Vector,
    velocity: Vector,
    a: i128,
    b: i128,
    plane_discriminant: i128,
    radius_squared: i128,
) -> i32 {
    let x = dot(edge, point);
    let y = dot(edge, velocity);
    if y == 0 {
        return x.signum() as i32;
    }
    let numerator = if y > 0 { -x } else { x };
    let denominator = y.abs();
    let vertex_offset = a * numerator + b * denominator;
    let comparison = if vertex_offset >= 0 {
        if vertex_offset == 0 && plane_discriminant == 0 {
            0
        } else {
            -1
        }
    } else {
        let scaled = subtract(scale(point, y), scale(velocity, x));
        (dot(scaled, scaled) - radius_squared * y * y).signum() as i32
    };
    comparison * y.signum() as i32
}

fn ray_hits(point: Vector, velocity: Vector, radius_squared: i128) -> bool {
    let projection = dot(point, velocity);
    projection < 0
        && projection * projection >= dot(velocity, velocity) * (dot(point, point) - radius_squared)
}

fn classify(
    center: Vector,
    radius: i128,
    first: Vector,
    second: Vector,
    velocity: Vector,
) -> &'static str {
    let left = subtract(first, center);
    let right = subtract(second, center);
    let edge = subtract(right, left);
    let normal = cross(edge, velocity);
    let offset = cross(edge, left);
    let radius_squared = radius * radius;
    let a = dot(normal, normal);
    let b = dot(offset, normal);
    let c = dot(offset, offset) - radius_squared * dot(edge, edge);
    if a != 0 && c > 0 && b < 0 {
        let height = dot(left, normal);
        let plane_discriminant = radius_squared * a - height * height;
        if plane_discriminant >= 0 {
            let left_sign = projection_sign(
                left,
                edge,
                velocity,
                a,
                b,
                plane_discriminant,
                radius_squared,
            );
            let right_sign = projection_sign(
                right,
                edge,
                velocity,
                a,
                b,
                plane_discriminant,
                radius_squared,
            );
            if left_sign < 0 && right_sign > 0 {
                return "Warning";
            }
        }
    }
    if ray_hits(left, velocity, radius_squared) || ray_hits(right, velocity, radius_squared) {
        return "Crash";
    }
    "False alarm"
}

fn read_vector(tokens: &mut impl Iterator<Item = i128>) -> Vector {
    Vector {
        x: tokens.next().unwrap(),
        y: tokens.next().unwrap(),
        z: tokens.next().unwrap(),
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input
        .split_whitespace()
        .map(|word| word.parse::<i128>().unwrap());
    let center = read_vector(&mut tokens);
    let radius = tokens.next().unwrap();
    let first = read_vector(&mut tokens);
    let second = read_vector(&mut tokens);
    let velocity = read_vector(&mut tokens);
    println!("{}", classify(center, radius, first, second, velocity));
}
