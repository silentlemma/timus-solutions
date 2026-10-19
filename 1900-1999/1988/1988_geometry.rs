use std::io::{self, Read};

const DIMENSIONS: usize = 3;
const ITERATIONS: usize = 80;
type Vector = [i64; DIMENSIONS];

fn dot(a: Vector, b: Vector) -> i64 {
    a.iter().zip(b.iter()).map(|(x, y)| x * y).sum()
}

fn meeting_time(carrier: Vector, ship: Vector, speed: f64) -> f64 {
    let radius_squared = dot(carrier, carrier);
    let distance_squared = dot(ship, ship);
    let radius = (radius_squared as f64).sqrt();
    let distance = (distance_squared as f64).sqrt();
    let delta = distance_squared - radius_squared;
    let tangent = (delta as f64).sqrt();
    let radial_gap = delta as f64 / (distance + radius);
    let cross = [
        carrier[1] * ship[2] - carrier[2] * ship[1],
        carrier[2] * ship[0] - carrier[0] * ship[2],
        carrier[0] * ship[1] - carrier[1] * ship[0],
    ];
    let angle = (dot(cross, cross) as f64)
        .sqrt()
        .atan2(dot(carrier, ship) as f64);
    let visible_angle = tangent.atan2(radius);
    let ship_length = |beta: f64| {
        if beta <= visible_angle {
            let sideways = 2.0 * (distance * radius).sqrt() * (beta / 2.0).sin();
            radial_gap.hypot(sideways)
        } else {
            tangent + radius * (beta - visible_angle)
        }
    };
    let radial_time = radial_gap / speed;
    if radius * angle <= radial_time {
        return radial_time;
    }
    let (mut low, mut high) = (0.0, angle);
    for _ in 0..ITERATIONS {
        let beta = (low + high) / 2.0;
        if radius * (angle - beta) > ship_length(beta) / speed {
            low = beta;
        } else {
            high = beta;
        }
    }
    let beta = (low + high) / 2.0;
    (radius * (angle - beta)).max(ship_length(beta) / speed)
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let mut carrier = [0; DIMENSIONS];
    let mut ship = [0; DIMENSIONS];
    for value in &mut carrier {
        *value = tokens.next().unwrap().parse().unwrap();
    }
    for value in &mut ship {
        *value = tokens.next().unwrap().parse().unwrap();
    }
    let speed = tokens.next().unwrap().parse().unwrap();
    println!("{:.10}", meeting_time(carrier, ship, speed));
}
