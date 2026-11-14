use std::io::{self, BufRead, Write};

const CORNERS: usize = 3;
const INNER: f64 = 0.5;
const OUTER: f64 = -1.5;
const PRECISION: usize = 10;

fn main() -> io::Result<()> {
    let mut input = io::stdin().lock();
    let mut line = String::new();
    let mut points = [(0.0, 0.0); CORNERS];
    let (mut cx, mut cy) = (0.0, 0.0);
    for point in &mut points {
        loop {
            line.clear();
            if input.read_line(&mut line)? == 0 {
                return Ok(());
            }
            let mut coordinates = line.split_ascii_whitespace();
            if let Some(x) = coordinates.next() {
                *point = (
                    x.parse::<f64>().unwrap(),
                    coordinates.next().unwrap().parse().unwrap(),
                );
                break;
            }
        }
        cx += point.0;
        cy += point.1;
    }
    cx /= CORNERS as f64;
    cy /= CORNERS as f64;

    let mut output = io::stdout().lock();
    for scale in [INNER, OUTER] {
        for (x, y) in points {
            let px = cx + scale * (x - cx);
            let py = cy + scale * (y - cy);
            writeln!(output, "{px:.PRECISION$} {py:.PRECISION$}")?;
        }
    }
    Ok(())
}
