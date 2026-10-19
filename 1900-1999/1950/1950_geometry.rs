use std::io::{self, Read};

const DECIMAL_SCALE: i64 = 1000;
const DECIMAL_PLACES: usize = 3;
const SIDE: i64 = 10 * DECIMAL_SCALE;
const CUTS: usize = 30;
const GRID_SCALE: i64 = 1i64 << CUTS;
const INITIAL_AREA: f64 = 50.0;

#[derive(Clone, Copy)]
struct Point {
    x: i64,
    y: i64,
}

fn parse_coordinate(text: &str) -> i64 {
    let text = if text.starts_with('+') { &text[1..] } else { text };
    let (whole, fractional) = text.split_once('.').unwrap_or((text, ""));
    let mut digits = fractional.to_owned();
    while digits.len() < DECIMAL_PLACES {
        digits.push('0');
    }
    let integer = if whole.is_empty() { "0" } else { whole };
    integer.parse::<i64>().unwrap() * DECIMAL_SCALE
        + digits[..DECIMAL_PLACES].parse::<i64>().unwrap()
}

fn opposite(first: i64, second: i64) -> bool {
    (first < 0 && second > 0) || (second < 0 && first > 0)
}

fn area_for_sale(x: i64, y: i64) -> f64 {
    let target = Point {
        x: x * GRID_SCALE,
        y: y * GRID_SCALE,
    };
    let mut right = Point {
        x: SIDE * GRID_SCALE,
        y: 0,
    };
    let mut first = Point { x: 0, y: 0 };
    let mut second = Point {
        x: SIDE * GRID_SCALE,
        y: SIDE * GRID_SCALE,
    };
    let (mut area, mut answer) = (INITIAL_AREA, 0.0);
    for _ in 0..CUTS {
        let middle = Point {
            x: (first.x + second.x) / 2,
            y: (first.y + second.y) / 2,
        };
        let normal_x = (middle.y - right.y).signum();
        let normal_y = -(middle.x - right.x).signum();
        let origin_side = -normal_x * right.x - normal_y * right.y;
        let target_side = normal_x * (target.x - right.x) + normal_y * (target.y - right.y);
        let ray_right = x * right.y - y * right.x;
        let ray_middle = x * middle.y - y * middle.x;
        let half = area / 2.0;
        if opposite(ray_right, ray_middle)
            && (opposite(origin_side, target_side) || target_side == 0)
        {
            answer += half;
        }
        if target_side == 0 {
            break;
        }
        let first_side = normal_x * (first.x - right.x) + normal_y * (first.y - right.y);
        if (target_side > 0) == (first_side > 0) {
            second = right;
        } else {
            first = right;
        }
        right = middle;
        area = half;
    }
    answer
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_whitespace();
    let x = parse_coordinate(words.next().unwrap());
    let y = parse_coordinate(words.next().unwrap());
    println!("{:.10}", area_for_sale(x, y));
}
