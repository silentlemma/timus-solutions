use std::io::{self, Read};

const GRAVITY_NUMERATOR: i64 = 49;
const GRAVITY_DENOMINATOR: i64 = 5;
const POINT_COUNT: usize = 3;

fn can_reach(speed: i64, dx: i64, dy: i64) -> bool {
    let threshold = GRAVITY_DENOMINATOR * speed * speed - GRAVITY_NUMERATOR * dy;
    threshold >= 0
        && threshold * threshold >= GRAVITY_NUMERATOR * GRAVITY_NUMERATOR * (dx * dx + dy * dy)
}

fn solve(speed: i64, head: (i64, i64), left: (i64, i64), right: (i64, i64)) -> bool {
    let jump = |start: (i64, i64), target: (i64, i64)| {
        can_reach(speed, target.0 - start.0, target.1 - start.1)
    };
    jump(left, right) && jump(right, left) && (jump(left, head) || jump(right, head))
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let speed: i64 = tokens.next().unwrap().parse().unwrap();
    let points: Vec<(i64, i64)> = (0..POINT_COUNT)
        .map(|_| {
            (
                tokens.next().unwrap().parse().unwrap(),
                tokens.next().unwrap().parse().unwrap(),
            )
        })
        .collect();
    println!(
        "{}",
        if solve(speed, points[0], points[1], points[2]) {
            "Yes"
        } else {
            "No"
        }
    );
}
