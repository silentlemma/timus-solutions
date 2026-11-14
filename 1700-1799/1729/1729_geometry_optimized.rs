use std::f64::consts::PI;
use std::io::{self, Read};

const SCALE: f64 = 1000.0;
const HALF_TURN: u32 = 180_000;

fn main() -> io::Result<()> {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input)?;
    let mut fields = input.split_ascii_whitespace();
    let radius: f64 = fields.next().unwrap().parse().unwrap();
    let angle: f64 = fields.next().unwrap().parse().unwrap();
    let units = (angle * SCALE).round() as u32;
    let full_chords = f64::from(HALF_TURN / units - 1);
    let remainder = f64::from(HALF_TURN % units);
    let radians_per_unit = PI / f64::from(HALF_TURN);
    let distance = radius
        * (1.0
            + 2.0
                * (full_chords * (f64::from(units) * radians_per_unit).sin()
                    + (remainder * radians_per_unit).sin()));
    println!("{:.7}", distance);
    Ok(())
}
