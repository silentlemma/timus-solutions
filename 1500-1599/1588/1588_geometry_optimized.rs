use std::io::{self, Read};

const COORDINATE_LIMIT: i32 = 10000;
const DIRECTION_WIDTH: i32 = 2 * COORDINATE_LIMIT + 1;

fn gcd(mut a: i32, mut b: i32) -> i32 {
    while b != 0 {
        (a, b) = (b, a % b);
    }
    a.abs()
}

fn main() -> io::Result<()> {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input)?;
    let mut numbers = input
        .split_ascii_whitespace()
        .map(|s| s.parse::<i32>().unwrap());
    let count = numbers.next().unwrap() as usize;
    let mut cities: Vec<_> = (0..count)
        .map(|_| (numbers.next().unwrap(), numbers.next().unwrap()))
        .collect();
    cities.sort_unstable();
    let mut directions = Vec::with_capacity(count);
    let (mut total, mut correction) = (0.0, 0.0);
    for (i, &(x, y)) in cities.iter().enumerate() {
        directions.clear();
        for (j, &(other_x, other_y)) in cities.iter().enumerate() {
            if i == j {
                continue;
            }
            let (dx, dy, sign) = if j < i {
                (x - other_x, y - other_y, -1)
            } else {
                (other_x - x, other_y - y, 1)
            };
            let step = gcd(dx, dy);
            let direction = dx / step * DIRECTION_WIDTH + dy / step + COORDINATE_LIMIT;
            directions.push((direction, sign * (dx * dx + dy * dy)));
        }
        directions.sort_unstable();
        let mut at = 0;
        while at < directions.len() {
            let (direction, first) = directions[at];
            let mut last = first;
            at += 1;
            while at < directions.len() && directions[at].0 == direction {
                last = directions[at].1;
                at += 1;
            }
            // A negative distance means an earlier city already counts this road.
            if first > 0 {
                let term = f64::from(last).sqrt() - correction;
                let next = total + term;
                correction = (next - total) - term;
                total = next;
            }
        }
    }
    println!("{}", total.round() as i64);
    Ok(())
}
