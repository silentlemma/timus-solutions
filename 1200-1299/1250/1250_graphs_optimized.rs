use std::io::{self, Read};

const HEADER: usize = 4;
const DECIMAL: usize = 10;
const PADDING: usize = 4;
const SEA: u8 = 0;
const LAND: u8 = 1;
const EXTERIOR: u8 = 2;
const BLOCKED: u8 = 4;
const VISITED: u8 = 8;

fn flood(
    cells: &mut [u8],
    stack: &mut Vec<u32>,
    start: usize,
    steps: &[isize],
    mask: u8,
    want: u8,
    mark: u8,
) {
    cells[start] = mark;
    stack.push(start as u32);
    while let Some(cell) = stack.pop() {
        for &step in steps {
            let neighbor = (cell as isize + step) as usize;
            if cells[neighbor] & mask == want {
                cells[neighbor] = mark;
                stack.push(neighbor as u32);
            }
        }
    }
}

fn main() {
    let mut input = Vec::new();
    io::stdin().lock().read_to_end(&mut input).unwrap();
    let mut cursor = 0;
    let mut header = [0; HEADER];
    for number in &mut header {
        while !input[cursor].is_ascii_digit() {
            cursor += 1;
        }
        while cursor < input.len() && input[cursor].is_ascii_digit() {
            *number = *number * DECIMAL + usize::from(input[cursor] - b'0');
            cursor += 1;
        }
    }
    let [width, height, x, y] = header;
    let stride = width + PADDING;
    let mut cells = vec![BLOCKED; stride * (height + PADDING)];
    // The exterior ring is passable only for the four-neighbor exterior flood.
    for row in 1..height + PADDING - 1 {
        cells[row * stride + 1..(row + 1) * stride - 1].fill(EXTERIOR);
    }
    let mut map = input[cursor..]
        .iter()
        .filter(|&&cell| cell == b'.' || cell == b'#');
    for row in 2..height + 2 {
        for cell in &mut cells[row * stride + 2..row * stride + width + 2] {
            *cell = if *map.next().unwrap() == b'#' {
                LAND
            } else {
                SEA
            };
        }
    }
    let step = stride as isize;
    let sides = [1, -1, step, -step];
    let all = [1, -1, step, -step, step + 1, step - 1, -step + 1, -step - 1];
    let mut stack = Vec::new();
    let start = (y + 1) * stride + x + 1;
    if cells[start] == SEA {
        flood(
            &mut cells,
            &mut stack,
            start,
            &all,
            LAND | EXTERIOR | BLOCKED,
            SEA,
            BLOCKED,
        );
    }
    flood(
        &mut cells,
        &mut stack,
        stride + 1,
        &sides,
        BLOCKED | VISITED,
        SEA,
        VISITED,
    );
    let mut islands = 0;
    for index in 0..cells.len() {
        if cells[index] == LAND {
            islands += 1;
            flood(&mut cells, &mut stack, index, &sides, LAND, LAND, VISITED);
        }
    }
    println!("{}", islands);
}
