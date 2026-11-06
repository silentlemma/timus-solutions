use std::io::{self, Read};

const ALICE: i8 = 1;
const BOB: i8 = -1;
const DRAW: i8 = 0;
const DECIMAL: usize = 10;

#[derive(Clone, Copy)]
struct Face<'a> {
    cells: &'a [u8],
    reversed: bool,
}

fn fold(face: Face<'_>, top: bool, next_alice: bool) -> i8 {
    let color = face.cells[0];
    if face.cells.iter().all(|&cell| cell == color) {
        return if color == b'A' { ALICE } else { BOB };
    }
    let (left, right) = face.cells.split_at(face.cells.len() / 2);
    let (left, right) = if face.reversed {
        (right, left)
    } else {
        (left, right)
    };
    let left = Face {
        cells: left,
        reversed: face.reversed,
    };
    let right = Face {
        cells: right,
        reversed: !face.reversed,
    };
    if top {
        play(left, right, next_alice)
    } else {
        play(right, left, next_alice)
    }
}

fn play(top: Face<'_>, bottom: Face<'_>, alice: bool) -> i8 {
    if top.cells.len() % 2 != 0 {
        return DRAW;
    }
    let first = fold(top, true, !alice);
    if first == if alice { ALICE } else { BOB } {
        return first;
    }
    let second = fold(bottom, false, !alice);
    if alice {
        first.max(second)
    } else {
        first.min(second)
    }
}

fn byte(input: &mut impl Read) -> io::Result<u8> {
    let mut buffer = [0];
    input.read_exact(&mut buffer)?;
    Ok(buffer[0])
}

fn non_space(input: &mut impl Read) -> io::Result<u8> {
    loop {
        let next = byte(input)?;
        if !next.is_ascii_whitespace() {
            return Ok(next);
        }
    }
}

fn main() -> io::Result<()> {
    let mut input = io::stdin().lock();
    let mut next = non_space(&mut input)?;
    let mut size = 0;
    while next.is_ascii_digit() {
        size = size * DECIMAL + usize::from(next - b'0');
        next = byte(&mut input)?;
    }
    let mut cells = vec![0; 2 * size];
    let (top, bottom) = cells.split_at_mut(size);
    for side in [&mut *top, &mut *bottom] {
        side[0] = non_space(&mut input)?;
        input.read_exact(&mut side[1..])?;
    }
    let top = Face {
        cells: top,
        reversed: false,
    };
    let bottom = Face {
        cells: bottom,
        reversed: false,
    };
    println!(
        "{}",
        match play(top, bottom, true) {
            ALICE => "Alice",
            BOB => "Bob",
            _ => "Draw",
        }
    );
    Ok(())
}
