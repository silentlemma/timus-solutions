use std::os::raw::c_int;

const MAX_SIDE: usize = 33;
const MIN_SIDE: usize = 3;
const INPUT_BYTES: usize = 128;
const OUTPUT_BYTES: usize = 12;
const TILE_AREA: u32 = 9;
const ENTRANCE_SIDES: u32 = 4;

extern "C" {
    fn read(fd: c_int, buffer: *mut u8, length: usize) -> isize;
    fn write(fd: c_int, buffer: *const u8, length: usize) -> isize;
}

struct Input {
    bytes: [u8; INPUT_BYTES],
    position: usize,
    length: usize,
}

impl Input {
    fn byte(&mut self) -> u8 {
        if self.position == self.length {
            let count = unsafe { read(0, self.bytes.as_mut_ptr(), INPUT_BYTES) };
            if count <= 0 {
                return 0;
            }
            self.position = 0;
            self.length = count as usize;
        }
        let result = self.bytes[self.position];
        self.position += 1;
        result
    }
}

fn enqueue(
    row: usize,
    queue: &mut [u8; MAX_SIDE],
    tail: &mut usize,
    pending: &mut usize,
    queued: &mut u64,
) {
    let bit = 1u64 << row;
    if *queued & bit == 0 {
        queue[*tail] = row as u8;
        *tail = (*tail + 1) % MAX_SIDE;
        *pending += 1;
        *queued |= bit;
    }
}

fn main() {
    let mut input = Input {
        bytes: [0; INPUT_BYTES],
        position: 0,
        length: 0,
    };
    let mut byte = input.byte();
    while byte != 0 && byte.is_ascii_whitespace() {
        byte = input.byte();
    }
    let mut n = 0usize;
    while byte.is_ascii_digit() {
        n = n * 10 + usize::from(byte - b'0');
        byte = input.byte();
    }
    if !(MIN_SIDE..=MAX_SIDE).contains(&n) {
        return;
    }
    let mut open = [0u64; MAX_SIDE];
    for mask in open.iter_mut().take(n) {
        for column in 0..n {
            let mut cell = input.byte();
            while cell != b'.' && cell != b'#' {
                if cell == 0 {
                    return;
                }
                cell = input.byte();
            }
            if cell == b'.' {
                *mask |= 1u64 << column;
            }
        }
    }
    let mut reached = [0u64; MAX_SIDE];
    reached[0] = 1;
    reached[n - 1] = 1u64 << (n - 1);
    let mut queue = [0u8; MAX_SIDE];
    let (mut head, mut tail, mut pending, mut queued) = (0, 0, 0, 0);
    enqueue(0, &mut queue, &mut tail, &mut pending, &mut queued);
    enqueue(n - 1, &mut queue, &mut tail, &mut pending, &mut queued);
    while pending != 0 {
        let row = usize::from(queue[head]);
        head = (head + 1) % MAX_SIDE;
        pending -= 1;
        queued &= !(1u64 << row);
        let mut mask = reached[row];
        loop {
            let expanded = (mask | (mask << 1) | (mask >> 1)) & open[row];
            if expanded == mask {
                break;
            }
            mask = expanded;
        }
        reached[row] = mask;
        // Only a newly reached cell can schedule a row; at most n rows are queued.
        for next in [row.wrapping_sub(1), row + 1] {
            if next < n {
                let added = mask & open[next] & !reached[next];
                if added != 0 {
                    reached[next] |= added;
                    enqueue(next, &mut queue, &mut tail, &mut pending, &mut queued);
                }
            }
        }
    }
    let mut walls = 0;
    for row in 0..n {
        let up = if row == 0 { 0 } else { open[row - 1] };
        let down = if row + 1 == n { 0 } else { open[row + 1] };
        let mask = reached[row];
        walls += (mask & !up).count_ones() + (mask & !down).count_ones();
        walls += (mask & !(open[row] << 1)).count_ones();
        walls += (mask & !(open[row] >> 1)).count_ones();
    }
    let mut area = (walls - ENTRANCE_SIDES) * TILE_AREA;
    let mut output = [0u8; OUTPUT_BYTES];
    let mut start = OUTPUT_BYTES - 1;
    output[start] = b'\n';
    loop {
        start -= 1;
        output[start] = b'0' + (area % 10) as u8;
        area /= 10;
        if area == 0 {
            break;
        }
    }
    while start < OUTPUT_BYTES {
        let count = unsafe { write(1, output[start..].as_ptr(), OUTPUT_BYTES - start) };
        if count <= 0 {
            break;
        }
        start += count as usize;
    }
}
