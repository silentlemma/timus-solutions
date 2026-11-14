use std::io::{self, BufRead, Write};

const START_HEIGHT: usize = 100_000;

fn number(input: &mut impl BufRead) -> io::Result<i32> {
    let (mut value, mut sign, mut reading) = (0, 1, false);
    loop {
        let bytes = input.fill_buf()?;
        if bytes.is_empty() {
            return Ok(sign * value);
        }
        let size = bytes.len();
        for (i, &byte) in bytes.iter().enumerate() {
            if byte.is_ascii_digit() {
                value = value * 10 + i32::from(byte - b'0');
                reading = true;
            } else if reading {
                input.consume(i + 1);
                return Ok(sign * value);
            } else if byte == b'-' {
                sign = -1;
            }
        }
        input.consume(size);
    }
}

fn main() -> io::Result<()> {
    let mut input = io::stdin().lock();
    let count = number(&mut input)? as usize;
    let mut at_height = vec![0u16; START_HEIGHT + 1];
    let mut coordinates = vec![0; count + 1];
    for (id, x) in coordinates.iter_mut().enumerate().skip(1) {
        *x = number(&mut input)?;
        let height = number(&mut input)? as usize;
        at_height[height] = id as u16;
    }
    let mut path = Vec::<u16>::with_capacity(count);
    let mut right = false;
    for &id in at_height.iter().rev().filter(|&&id| id != 0) {
        if let Some(&last) = path.last() {
            let step = coordinates[id as usize] > coordinates[last as usize];
            // Keep the farthest flag while moving in the same direction.
            if path.len() == 1 || step != right {
                path.push(id);
            } else {
                *path.last_mut().unwrap() = id;
            }
            right = step;
        } else {
            path.push(id);
        }
    }
    let mut output = io::BufWriter::new(io::stdout().lock());
    writeln!(output, "{}", path.len())?;
    for (i, flag) in path.into_iter().enumerate() {
        if i > 0 {
            output.write_all(b" ")?;
        }
        write!(output, "{flag}")?;
    }
    writeln!(output)?;
    output.flush()
}
