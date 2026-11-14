use std::io::{self, BufRead};

const MODULUS: i32 = 9973;
const PERIOD_SCALE: i32 = 5219;
const PERIOD_SHIFT: i32 = 2283;
const CUBIC_LINEAR_TERM: i32 = 3;
const SCALE_OFFSET: i32 = 7;

fn main() -> io::Result<()> {
    let mut input = String::new();
    io::stdin().lock().read_line(&mut input)?;
    let n: i32 = input.trim().parse().unwrap();

    // One complete period composes to y -> PERIOD_SCALE * y + PERIOD_SHIFT.
    let mut periods = n / MODULUS;
    let (mut scale, mut shift) = (PERIOD_SCALE, PERIOD_SHIFT);
    let mut value = 0;
    while periods > 0 {
        if periods % 2 != 0 {
            value = (scale * value + shift) % MODULUS;
        }
        shift = ((scale + 1) * shift) % MODULUS;
        scale = (scale * scale) % MODULUS;
        periods /= 2;
    }

    for x in 1..=n % MODULUS {
        let square = x * x % MODULUS;
        let cube = square * x % MODULUS;
        let fifth = cube * square % MODULUS;
        value = ((fifth - x + SCALE_OFFSET) * value + cube + CUBIC_LINEAR_TERM * x - fifth)
            .rem_euclid(MODULUS);
    }
    println!("{value}");
    Ok(())
}
