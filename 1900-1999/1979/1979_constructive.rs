use std::io::{self, Read, Write};

const FACE_COUNT: usize = 6;
const HALF_FACES: usize = 3;
const BAND_COUNT: usize = 3;
const BELT_FACES: usize = 4;

fn label(n: usize, band: usize, row: usize, col: usize) -> usize {
    let area = n * n;
    let complement = FACE_COUNT * area + 1;
    if band == 0 {
        return 2 * area + row * n + col + 1;
    }
    if band == 2 {
        return complement - (HALF_FACES * area - row * n - n + col + 1);
    }
    let face = col / n;
    let col = col % n;
    if face < 2 {
        return face * area + row * n + col + 1;
    }
    complement - ((face - 2) * area + row * n + n - col)
}

fn write_cube<W: Write>(n: usize, out: &mut W) {
    for band in 0..BAND_COUNT {
        let width = if band == 1 { BELT_FACES * n } else { n };
        for row in 0..n {
            for col in 0..width {
                if col > 0 {
                    write!(out, " ").unwrap();
                }
                write!(out, "{}", label(n, band, row, col)).unwrap();
            }
            writeln!(out).unwrap();
        }
    }
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let n: usize = match text.split_whitespace().next() {
        Some(s) => s.parse().unwrap(),
        None => return,
    };
    let mut out = io::BufWriter::new(io::stdout().lock());
    write_cube(n, &mut out);
}
