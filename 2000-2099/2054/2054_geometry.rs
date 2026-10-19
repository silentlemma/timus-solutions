use std::f64::consts::PI;
use std::fmt::Write as FmtWrite;
use std::io::{self, Read};

const LONG_MONTH: i32 = 31;
const SHORT_MONTH: i32 = 30;
const FEBRUARY: i32 = 28;
const SOLSTICE_DAY: i32 = 171;
const HOURS_PER_DAY: i32 = 24;
const HOURS_PER_YEAR: i32 = 8760;
const NOON: i32 = 12;
const HALF_TURN: f64 = 180.0;
const TILT_DEGREES: f64 = 23.439281;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut fields = input.split_whitespace();
    let radians = PI / HALF_TURN;
    let latitude = fields.next().unwrap().parse::<f64>().unwrap() * radians;
    let count: usize = fields.next().unwrap().parse().unwrap();
    let months = [
        "jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec",
    ];
    let lengths = [
        LONG_MONTH,
        FEBRUARY,
        LONG_MONTH,
        SHORT_MONTH,
        LONG_MONTH,
        SHORT_MONTH,
        LONG_MONTH,
        LONG_MONTH,
        SHORT_MONTH,
        LONG_MONTH,
        SHORT_MONTH,
        LONG_MONTH,
    ];
    let equatorial = latitude.cos() * (TILT_DEGREES * radians).cos();
    let transverse = latitude.cos();
    let axial = latitude.sin() * (TILT_DEGREES * radians).sin();
    let mut output = String::new();
    for _ in 0..count {
        let day: i32 = fields.next().unwrap().parse().unwrap();
        let month = fields.next().unwrap();
        let hour: i32 = fields.next().unwrap().parse().unwrap();
        let index = months.iter().position(|&value| value == month).unwrap();
        let day_index = lengths[..index].iter().sum::<i32>() + day - 1;
        let elapsed = (day_index - SOLSTICE_DAY) * HOURS_PER_DAY + hour - NOON;
        let orbit = 2.0 * PI * f64::from(elapsed) / f64::from(HOURS_PER_YEAR);
        let spin = orbit + 2.0 * PI * f64::from(hour - NOON) / f64::from(HOURS_PER_DAY);
        let sine = equatorial * spin.cos() * orbit.cos()
            + transverse * spin.sin() * orbit.sin()
            + axial * orbit.cos();
        let angle = sine.clamp(0.0, 1.0).asin() / radians;
        writeln!(output, "{:.10}", angle).unwrap();
    }
    print!("{}", output);
}
