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

const INPUT_SIZE: usize = 8192;

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

const WORD_BITS: usize = 64;
const OUTPUT_SIZE: usize = 16384;

fn reset(unseen: &mut [u64], vertices: usize) {
    unseen.fill(u64::MAX);
    if vertices % WORD_BITS != 0 {
        *unseen.last_mut().unwrap() = (1_u64 << (vertices % WORD_BITS)) - 1;
    }
}

fn visit(root: usize, graph: &[u64], words: usize, unseen: &mut [u64], queue: &mut Vec<u16>) {
    unseen[root / WORD_BITS] &= !(1_u64 << (root % WORD_BITS));
    queue.clear();
    queue.push(root as u16);
    let mut head = 0;
    while head < queue.len() {
        let vertex = queue[head] as usize;
        head += 1;
        for word in 0..words {
            let mut fresh = graph[vertex * words + word] & unseen[word];
            unseen[word] &= !fresh;
            while fresh != 0 {
                queue.push((word * WORD_BITS + fresh.trailing_zeros() as usize) as u16);
                fresh &= fresh - 1;
            }
        }
    }
}

fn append_number(mut value: usize, output: &mut [u8], used: &mut usize) {
    const MAX_DIGITS: usize = 4;
    let mut digits = [0_u8; MAX_DIGITS];
    let mut first = digits.len();
    loop {
        first -= 1;
        digits[first] = b'0' + (value % 10) as u8;
        value /= 10;
        if value == 0 {
            break;
        }
    }
    output[*used..*used + digits.len() - first].copy_from_slice(&digits[first..]);
    *used += digits.len() - first;
}

#[no_mangle]
pub extern "C" fn main() -> i32 {
    let mut input = Input::new();
    let vertices = input.number() as usize;
    let words = (vertices + WORD_BITS - 1) / WORD_BITS;
    let mut forward = vec![0_u64; vertices * words];
    let mut reverse = vec![0_u64; vertices * words];
    for from in 0..vertices {
        loop {
            let to = input.number() as usize;
            if to == 0 {
                break;
            }
            let to = to - 1;
            forward[from * words + to / WORD_BITS] |= 1_u64 << (to % WORD_BITS);
            reverse[to * words + from / WORD_BITS] |= 1_u64 << (from % WORD_BITS);
        }
    }
    let mut unseen = vec![0_u64; words];
    let mut queue = Vec::with_capacity(vertices);
    reset(&mut unseen, vertices);
    let mut root = 0;
    for vertex in 0..vertices {
        if unseen[vertex / WORD_BITS] >> (vertex % WORD_BITS) & 1 != 0 {
            root = vertex;
            visit(root, &forward, words, &mut unseen, &mut queue);
        }
    }
    reset(&mut unseen, vertices);
    visit(root, &forward, words, &mut unseen, &mut queue);
    if unseen.iter().any(|&word| word != 0) {
        write_all(b"0\n");
        return 0;
    }
    reset(&mut unseen, vertices);
    visit(root, &reverse, words, &mut unseen, &mut queue);
    let mut output = [0_u8; OUTPUT_SIZE];
    let mut used = 0;
    for vertex in 0..vertices {
        if unseen[vertex / WORD_BITS] >> (vertex % WORD_BITS) & 1 == 0 {
            append_number(vertex + 1, &mut output, &mut used);
            output[used] = b' ';
            used += 1;
        }
    }
    output[used] = b'0';
    output[used + 1] = b'\n';
    used += 2;
    if write_all(&output[..used]) {
        0
    } else {
        1
    }
}
