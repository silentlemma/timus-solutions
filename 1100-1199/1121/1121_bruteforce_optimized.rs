use std::io::{self, BufWriter, Read, Write};

const DIAMOND_SIDES: usize = 4;

const REACH: usize = 5;

fn number(input: &mut impl Iterator<Item = u8>) -> usize {
    let first = input.find(|byte| byte.is_ascii_digit()).unwrap();
    let mut value = usize::from(first - b'0');
    for byte in input.take_while(u8::is_ascii_digit) {
        value = value * 10 + usize::from(byte - b'0');
    }
    value
}

fn main() {
    let stdin = io::stdin();
    let mut input = stdin.lock().bytes().map(Result::unwrap);
    let (height, width) = (number(&mut input), number(&mut input));
    let stride = width + 2 * REACH;
    // A zero border lets every ring be read without checking grid edges.
    let mut grid = vec![0u16; (height + 2 * REACH) * stride];
    for row in REACH..height + REACH {
        let start = row * stride + REACH;
        for cell in &mut grid[start..start + width] {
            *cell = number(&mut input) as u16;
        }
    }
    let rings: [Vec<isize>; REACH] = std::array::from_fn(|index| {
        let distance = (index + 1) as isize;
        let mut offsets = Vec::with_capacity(DIAMOND_SIDES * (index + 1));
        for row in -distance..=distance {
            let col = distance - row.abs();
            let base = row * stride as isize;
            offsets.push(base + col);
            if col != 0 {
                offsets.push(base - col);
            }
        }
        offsets
    });
    let mut out = BufWriter::new(io::stdout().lock());
    for row in REACH..height + REACH {
        for col in REACH..width + REACH {
            if col != REACH {
                out.write_all(b" ").unwrap();
            }
            let cell = row * stride + col;
            if grid[cell] != 0 {
                out.write_all(b"-1").unwrap();
                continue;
            }
            let mut mask = 0;
            for ring in &rings {
                for &offset in ring {
                    mask |= grid[(cell as isize + offset) as usize];
                }
                if mask != 0 {
                    break;
                }
            }
            write!(out, "{}", mask).unwrap();
        }
        writeln!(out).unwrap();
    }
    out.flush().unwrap();
}
