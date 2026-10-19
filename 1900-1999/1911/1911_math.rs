use std::io::{self, Read};

const OUTPUT_PRECISION: usize = 12;

struct Parameters {
    speed: i128,
    length: i128,
    fire_speed: i128,
    fire_width: i128,
    gap: i128,
    natural: i128,
    shield: i128,
    braking: i128,
}

fn minimum_energy(p: &Parameters, branches: &[(i128, i128)]) -> f64 {
    let difference = p.fire_speed - p.speed;
    let mut best = f64::INFINITY;
    for &(left, right) in branches {
        let entry = left + p.length;
        let distance = right - entry;
        let held = entry * difference - p.gap * p.speed;
        let shield_numerator = held.max(0) * p.shield;
        let shield_denominator = p.speed * difference;
        let delay_numerator = p.speed * (right - left + p.fire_width) + (-held).max(0);
        let (brake_numerator, brake_denominator) = if delay_numerator >= 2 * distance * p.fire_speed
        {
            (p.speed * p.speed, 2 * distance)
        } else if delay_numerator <= distance * p.fire_speed {
            (0, 1)
        } else {
            (
                2 * p.speed * p.speed * p.fire_speed * (delay_numerator - distance * p.fire_speed),
                delay_numerator * delay_numerator,
            )
        };
        let extra = (brake_numerator - p.natural * brake_denominator).max(0);
        let cost = shield_numerator as f64 / shield_denominator as f64
            + (p.braking * extra) as f64 / brake_denominator as f64;
        best = best.min(cost);
    }
    best
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input
        .split_whitespace()
        .map(|token| token.parse::<i128>().unwrap());
    let parameters = Parameters {
        speed: tokens.next().unwrap(),
        length: tokens.next().unwrap(),
        fire_speed: tokens.next().unwrap(),
        fire_width: tokens.next().unwrap(),
        gap: tokens.next().unwrap(),
        natural: tokens.next().unwrap(),
        shield: tokens.next().unwrap(),
        braking: tokens.next().unwrap(),
    };
    let count = tokens.next().unwrap() as usize;
    let branches: Vec<_> = (0..count)
        .map(|_| (tokens.next().unwrap(), tokens.next().unwrap()))
        .collect();
    println!(
        "{:.*}",
        OUTPUT_PRECISION,
        minimum_energy(&parameters, &branches)
    );
}
