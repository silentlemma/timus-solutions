use std::io::{self, Read};

const RADIUS: f64 = 6400.0;
const HALF_TURN: f64 = 180.0;
const SHOWN: f64 = 0.0005; // values that print as 0.000

// three decimals, without a minus sign on zero
fn show(value: f64) {
    println!("{:.3}", if value.abs() < SHOWN { 0.0 } else { value });
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<f64>().unwrap());
    let (w, mut lon, side) = (it.next().unwrap(), it.next().unwrap(), it.next().unwrap());
    let arc = side / RADIUS; // the angle of one side seen from the center
    let south = w * std::f64::consts::PI / HALF_TURN;
    let north = south + arc;
    // north and south along meridians cancel; east runs along the northern
    // parallel and west along the southern one, at different speeds
    lon += (arc / north.cos() - arc / south.cos()) * HALF_TURN / std::f64::consts::PI;
    lon %= 2.0 * HALF_TURN;
    if lon > HALF_TURN {
        lon -= 2.0 * HALF_TURN;
    } else if lon <= -HALF_TURN {
        lon += 2.0 * HALF_TURN;
    }
    show(w);
    show(lon);
}
