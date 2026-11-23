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

const INPUT_SIZE: usize = 4096;

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

const OUTPUT_SIZE: usize = 64;
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

const MAX_SIDE: usize = 50;
const MAX_CELLS: usize = MAX_SIDE * MAX_SIDE;
const COLORS: usize = 10;
const PLAYERS: usize = 2;

struct Simulation {
    width: usize,
    cells: usize,
    color: [u8; MAX_CELLS],
    owner: [u8; MAX_CELLS],
    offered: [u8; MAX_CELLS],
    area: [usize; PLAYERS],
    frontier: [[i16; COLORS]; PLAYERS],
    next: [[i16; MAX_CELLS]; PLAYERS],
}

impl Simulation {
    fn new(width: usize, cells: usize) -> Self {
        Self {
            width,
            cells,
            color: [0; MAX_CELLS],
            owner: [0; MAX_CELLS],
            offered: [0; MAX_CELLS],
            area: [0; PLAYERS],
            frontier: [[-1; COLORS]; PLAYERS],
            next: [[-1; MAX_CELLS]; PLAYERS],
        }
    }
    fn offer(&mut self, side: usize, cell: usize) {
        let bit = 1 << side;
        if self.owner[cell] == 0 && self.offered[cell] & bit == 0 {
            self.offered[cell] |= bit;
            let colour = self.color[cell] as usize;
            self.next[side][cell] = self.frontier[side][colour];
            self.frontier[side][colour] = cell as i16;
        }
    }
    fn claim(&mut self, side: usize, cell: usize) {
        self.owner[cell] = (side + 1) as u8;
        self.area[side] += 1;
        if cell >= self.width {
            self.offer(side, cell - self.width);
        }
        if cell + self.width < self.cells {
            self.offer(side, cell + self.width);
        }
        if cell % self.width != 0 {
            self.offer(side, cell - 1);
        }
        if cell % self.width + 1 < self.width {
            self.offer(side, cell + 1);
        }
    }
    fn expand(&mut self, side: usize, alliance: usize) {
        while self.frontier[side][alliance] >= 0 {
            let cell = self.frontier[side][alliance] as usize;
            self.frontier[side][alliance] = self.next[side][cell];
            // Claims and opposing moves can make queued frontier entries stale.
            if self.owner[cell] == 0 {
                self.claim(side, cell);
            }
        }
    }
}

#[no_mangle]
pub extern "C" fn main() -> i32 {
    let mut input = Input::new();
    let (height, width) = (input.number() as usize, input.number() as usize);
    let mut simulation = Simulation::new(width, height * width);
    for cell in 0..simulation.cells {
        let mut c = input.byte();
        while c <= b' ' {
            c = input.byte();
        }
        simulation.color[cell] = c - b'0';
    }
    let seeds = [(height - 1) * width, width - 1];
    for (side, seed) in seeds.into_iter().enumerate() {
        simulation.claim(side, seed);
        simulation.expand(side, simulation.color[seed] as usize);
    }
    let moves = input.number() as usize;
    for turn in 0..moves {
        simulation.expand(turn % PLAYERS, input.number() as usize);
    }
    let mut output = [0u8; OUTPUT_SIZE];
    let mut used = 0;
    for area in simulation.area {
        write_number(&mut output, &mut used, area);
        output[used] = b'\n';
        used += 1;
    }
    if write_all(&output[..used]) {
        0
    } else {
        1
    }
}
