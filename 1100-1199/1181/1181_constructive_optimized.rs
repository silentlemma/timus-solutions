#![no_main]

#[cfg(windows)]
#[link(name = "msvcrt")]
extern "C" {
    #[link_name = "_read"]
    fn system_read(fd: i32, buffer: *mut u8, length: u32) -> i32;
    #[link_name = "_write"]
    fn system_write(fd: i32, buffer: *const u8, length: u32) -> i32;
}

#[cfg(not(windows))]
extern "C" {
    #[link_name = "read"]
    fn system_read(fd: i32, buffer: *mut u8, length: usize) -> isize;
    #[link_name = "write"]
    fn system_write(fd: i32, buffer: *const u8, length: usize) -> isize;
}

fn read_input(buffer: &mut [u8]) -> usize {
    // SAFETY: the writable slice stays live for the call, and its length is bounded by INPUT_SIZE.
    // Both CRT _read and POSIX read write no more than the supplied length.
    let count = unsafe {
        #[cfg(windows)]
        {
            system_read(0, buffer.as_mut_ptr(), buffer.len() as u32)
        }
        #[cfg(not(windows))]
        {
            system_read(0, buffer.as_mut_ptr(), buffer.len())
        }
    };
    if count > 0 {
        count as usize
    } else {
        0
    }
}

fn write_all(mut buffer: &[u8]) -> bool {
    while !buffer.is_empty() {
        // SAFETY: this live slice contains at most OUTPUT_SIZE readable bytes.
        // Both write functions access at most the specified length and return a byte count.
        let count = unsafe {
            #[cfg(windows)]
            {
                system_write(1, buffer.as_ptr(), buffer.len() as u32)
            }
            #[cfg(not(windows))]
            {
                system_write(1, buffer.as_ptr(), buffer.len())
            }
        };
        if count <= 0 {
            return false;
        }
        buffer = &buffer[count as usize..];
    }
    true
}

const INPUT_SIZE: usize = 256;

struct Input {
    bytes: [u8; INPUT_SIZE],
    position: usize,
    length: usize,
}

impl Input {
    fn new() -> Self {
        Self {
            bytes: [0; INPUT_SIZE],
            position: 0,
            length: 0,
        }
    }
    fn byte(&mut self) -> u8 {
        if self.position == self.length {
            self.length = read_input(&mut self.bytes);
            self.position = 0;
            if self.length == 0 {
                return 0;
            }
        }
        let value = self.bytes[self.position];
        self.position += 1;
        value
    }
    fn number(&mut self) -> i32 {
        let mut c = self.byte();
        while c != 0 && c <= b' ' {
            c = self.byte();
        }
        let sign = if c == b'-' {
            c = self.byte();
            -1
        } else {
            1
        };
        let mut value = 0;
        while c.is_ascii_digit() {
            value = value * 10 + i32::from(c - b'0');
            c = self.byte();
        }
        sign * value
    }
}

const OUTPUT_SIZE: usize = 12000;
const MAX_DIGITS: usize = 20;

fn write_number(output: &mut [u8], used: &mut usize, mut value: usize) {
    let mut digits = [0; MAX_DIGITS];
    let mut first = digits.len();
    loop {
        first -= 1;
        digits[first] = b'0' + (value % 10) as u8;
        value /= 10;
        if value == 0 {
            break;
        }
    }
    let count = digits.len() - first;
    output[*used..*used + count].copy_from_slice(&digits[first..]);
    *used += count;
}

const MAX_VERTICES: usize = 1000;
const COLOR_COUNT: usize = 3;
const TRIANGLE_SIZE: usize = 3;

fn print_cut(output: &mut [u8], used: &mut usize, a: usize, b: usize) {
    write_number(output, used, a + 1);
    output[*used] = b' ';
    *used += 1;
    write_number(output, used, b + 1);
    output[*used] = b'\n';
    *used += 1;
}

#[no_mangle]
pub extern "C" fn main() -> i32 {
    let mut input = Input::new();
    let n = input.number() as usize;
    let mut color = [0u8; MAX_VERTICES];
    let mut left = [0usize; MAX_VERTICES];
    let mut right = [0usize; MAX_VERTICES];
    let mut alive = [false; MAX_VERTICES];
    let mut counts = [0usize; COLOR_COUNT];
    for v in 0..n {
        let mut c = input.byte();
        while c <= b' ' {
            c = input.byte();
        }
        color[v] = match c {
            b'R' => 0,
            b'G' => 1,
            _ => 2,
        };
        counts[color[v] as usize] += 1;
        left[v] = (v + n - 1) % n;
        right[v] = (v + 1) % n;
        alive[v] = true;
    }
    let mut pending = [0usize; MAX_VERTICES + 2 * MAX_VERTICES];
    let (mut head, mut tail) = (0, 0);
    for v in 0..n {
        if color[left[v]] != color[right[v]] {
            pending[tail] = v;
            tail += 1;
        }
    }
    // At most 997 diagonals; 12000 bytes fit every pair of four-digit indices.
    let mut output = [0u8; OUTPUT_SIZE];
    let mut used = 0;
    write_number(&mut output, &mut used, n - TRIANGLE_SIZE);
    output[used] = b'\n';
    used += 1;
    let mut remaining = n;
    while remaining > TRIANGLE_SIZE {
        if counts.contains(&1) {
            let anchor = (0..n)
                .find(|&v| alive[v] && counts[color[v] as usize] == 1)
                .unwrap();
            let mut v = right[right[anchor]];
            while right[v] != anchor {
                print_cut(&mut output, &mut used, anchor, v);
                v = right[v];
            }
            break;
        }
        let v = pending[head];
        head += 1;
        if !alive[v] || color[left[v]] == color[right[v]] {
            continue;
        }
        let (before, after) = (left[v], right[v]);
        print_cut(&mut output, &mut used, before, after);
        alive[v] = false;
        right[before] = after;
        left[after] = before;
        counts[color[v] as usize] -= 1;
        remaining -= 1;
        // Only the neighbours change, giving at most 3*n queue entries in total.
        pending[tail] = before;
        pending[tail + 1] = after;
        tail += 2;
    }
    if write_all(&output[..used]) {
        0
    } else {
        1
    }
}
