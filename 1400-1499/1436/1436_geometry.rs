use std::f64::consts::PI;
use std::io::{self, Read};

fn angle(px: f64, ax: f64, ay: f64, bx: f64, by: f64) -> f64 {
    let (ux, uy, vx, vy) = (ax - px, ay, bx - px, by);
    (ux * vy - uy * vx).abs().atan2(ux * vx + uy * vy)
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_whitespace().map(|x| x.parse::<i64>().unwrap());
    let (x1, mut y1, x2, mut y2) = (
        it.next().unwrap(),
        it.next().unwrap(),
        it.next().unwrap(),
        it.next().unwrap(),
    );
    let best = if y1 * y2 < 0 || (y1 * y2 == 0 && x1 != x2) {
        PI // stand on the billboard itself
    } else if y1 * y2 == 0 {
        PI / 2.0 // a vertical billboard standing on the road
    } else {
        y1 = y1.abs();
        y2 = y2.abs();
        let (fx1, fy1, fx2, fy2) = (x1 as f64, y1 as f64, x2 as f64, y2 as f64);
        let spots = if y1 == y2 {
            vec![(fx1 + fx2) / 2.0]
        } else {
            // the best spot is where a circle through both ends touches the road:
            // its distance from where the billboard's line meets the road is sqrt(QA * QB)
            let qx = fx1 - fy1 * (fx2 - fx1) / (fy2 - fy1);
            let reach = ((fx1 - qx).hypot(fy1) * (fx2 - qx).hypot(fy2)).sqrt();
            vec![qx - reach, qx + reach]
        };
        spots
            .iter()
            .map(|&p| angle(p, fx1, fy1, fx2, fy2))
            .fold(0.0, f64::max)
    };
    println!("{:.6}", best);
}
