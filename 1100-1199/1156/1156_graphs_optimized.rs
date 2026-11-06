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
    // SAFETY: the writable slice stays live for the call, and its length is at most INPUT_SIZE.
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
        // SAFETY: the readable slice stays live and has at most OUTPUT_SIZE bytes.
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

const MAX_ROUND: usize = 50;
const VERTICES: usize = 2 * MAX_ROUND + 1;
const MAX_PAIRS: usize = 100;
const INPUT_SIZE: usize = 128;
const OUTPUT_SIZE: usize = VERTICES * 4;
const MAX_DIGITS: usize = 3;

struct Input {
    bytes: [u8; INPUT_SIZE],
    position: usize,
    length: usize,
}

impl Input {
    fn next_byte(&mut self) -> u8 {
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

    fn number(&mut self) -> usize {
        let mut c = self.next_byte();
        while c != 0 && c <= b' ' {
            c = self.next_byte();
        }
        let mut value = 0;
        while c.is_ascii_digit() {
            value = value * 10 + usize::from(c - b'0');
            c = self.next_byte();
        }
        value
    }
}

fn impossible() -> i32 {
    i32::from(!write_all(b"IMPOSSIBLE\n"))
}

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
    let length = digits.len() - first;
    output[*used..*used + length].copy_from_slice(&digits[first..]);
    *used += length;
}

// The C runtime calls this symbol directly.
#[no_mangle]
pub extern "C" fn main() -> i32 {
    let mut input = Input {
        bytes: [0; INPUT_SIZE],
        position: 0,
        length: 0,
    };
    let size = input.number();
    let pairs = input.number();
    let mut first = [0u8; VERTICES];
    let mut edges = [(0u8, 0u8); 2 * MAX_PAIRS + 1];
    for pair in 0..pairs {
        let (a, b) = (input.number(), input.number());
        let id = 2 * pair + 1;
        edges[id] = (b as u8, first[a]);
        edges[id + 1] = (a as u8, first[b]);
        first[a] = id as u8;
        first[b] = (id + 1) as u8;
    }
    let total = 2 * size;
    let mut component = [0u8; VERTICES];
    let mut colour = [0u8; VERTICES];
    let mut sizes = [[0u8; 2]; VERTICES];
    let mut queue = [0u8; VERTICES];
    let mut components = 0;
    for root in 1..=total {
        if component[root] != 0 {
            continue;
        }
        components += 1;
        component[root] = components as u8;
        queue[0] = root as u8;
        let (mut head, mut end) = (0, 1);
        while head < end {
            let node = usize::from(queue[head]);
            head += 1;
            sizes[components][usize::from(colour[node])] += 1;
            let mut index = first[node];
            while index != 0 {
                let (next, link) = edges[usize::from(index)];
                let next = usize::from(next);
                if component[next] == 0 {
                    component[next] = components as u8;
                    colour[next] = 1 - colour[node];
                    queue[end] = next as u8;
                    end += 1;
                } else if colour[next] == colour[node] {
                    return impossible();
                }
                index = link;
            }
        }
    }
    // Only bits up to size <= 50 matter; large colour classes cannot be chosen.
    let mut reach = [0u64; VERTICES];
    reach[0] = 1;
    for k in 1..=components {
        for count in sizes[k] {
            if usize::from(count) <= size {
                reach[k] |= reach[k - 1] << count;
            }
        }
    }
    if (reach[components] >> size) & 1 == 0 {
        return impossible();
    }
    let mut selected = [0u8; VERTICES];
    let mut remaining = size;
    for k in (1..=components).rev() {
        let count = usize::from(sizes[k][0]);
        if remaining < count || (reach[k - 1] >> (remaining - count)) & 1 == 0 {
            selected[k] = 1;
        }
        remaining -= usize::from(sizes[k][usize::from(selected[k])]);
    }
    let mut output = [0; OUTPUT_SIZE];
    let mut used = 0;
    for first_round in [true, false] {
        let mut space = false;
        for node in 1..=total {
            if (colour[node] == selected[usize::from(component[node])]) == first_round {
                if space {
                    output[used] = b' ';
                    used += 1;
                }
                write_number(&mut output, &mut used, node);
                space = true;
            }
        }
        output[used] = b'\n';
        used += 1;
    }
    i32::from(!write_all(&output[..used]))
}
