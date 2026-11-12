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

const MAX_SIDE: usize = 100;
const MAX_CELLS: usize = MAX_SIDE * MAX_SIDE;
const MAX_PADDED: usize = (MAX_SIDE + 2) * (MAX_SIDE + 2);
const MAX_HEIGHT: i32 = 100000;
const INF: u16 = u16::MAX;
const OUTPUT_SIZE: usize = 20;

struct Terrain {
    stride: usize,
    size: usize,
    start: usize,
    height: [i32; MAX_PADDED],
    flood: [u16; MAX_PADDED],
    distance: [u16; MAX_PADDED],
    queue: [u16; MAX_CELLS],
}

impl Terrain {
    fn spread(&mut self, source: usize) {
        self.queue[0] = source as u16;
        self.flood[source] = 0;
        let (mut head, mut tail) = (0, 1);
        while head < tail {
            let cell = self.queue[head] as usize;
            head += 1;
            for next in [cell - self.stride, cell - 1, cell + 1, cell + self.stride] {
                if self.flood[next] == INF && self.height[next] <= self.height[cell] {
                    self.flood[next] = self.flood[cell] + 1;
                    self.queue[tail] = next as u16;
                    tail += 1;
                }
            }
        }
    }

    fn can_escape(&mut self, jump: i32) -> bool {
        self.distance[..self.size].fill(INF);
        self.distance[self.start] = 0;
        self.queue[0] = self.start as u16;
        let (mut head, mut tail) = (0, 1);
        while head < tail {
            let cell = self.queue[head] as usize;
            head += 1;
            if self.flood[cell] == INF {
                return true;
            }
            let arrival = self.distance[cell] + 1;
            for next in [cell - self.stride, cell - 1, cell + 1, cell + self.stride] {
                // Padded borders have flood time zero and can never satisfy this deadline.
                if self.distance[next] == INF
                    && arrival < self.flood[next]
                    && self.height[next] - self.height[cell] <= jump
                {
                    self.distance[next] = arrival;
                    self.queue[tail] = next as u16;
                    tail += 1;
                }
            }
        }
        false
    }
}

#[no_mangle]
pub extern "C" fn main() -> i32 {
    let mut input = Input::new();
    let (rows, columns) = (input.number() as usize, input.number() as usize);
    let stride = columns + 2;
    let mut terrain = Terrain {
        stride,
        size: (rows + 2) * stride,
        start: 0,
        height: [-1; MAX_PADDED],
        flood: [0; MAX_PADDED],
        distance: [INF; MAX_PADDED],
        queue: [0; MAX_CELLS],
    };
    for row in 1..=rows {
        for column in 1..=columns {
            let cell = row * stride + column;
            terrain.height[cell] = input.number();
            terrain.flood[cell] = INF;
        }
    }
    let (row, column) = (input.number() as usize, input.number() as usize);
    terrain.start = row * stride + column;
    let (row, column) = (input.number() as usize, input.number() as usize);
    terrain.spread(row * stride + column);
    if !terrain.can_escape(MAX_HEIGHT) {
        write_all(b"-1\n");
        return 0;
    }
    let (mut low, mut high) = (0, MAX_HEIGHT);
    while low < high {
        let middle = (low + high) / 2;
        if terrain.can_escape(middle) {
            high = middle;
        } else {
            low = middle + 1;
        }
    }
    let mut answer = low as u32;
    let mut output = [0_u8; OUTPUT_SIZE];
    let mut first = output.len() - 1;
    output[first] = b'\n';
    loop {
        first -= 1;
        output[first] = (answer % 10) as u8 + b'0';
        answer /= 10;
        if answer == 0 {
            break;
        }
    }
    write_all(&output[first..]);
    0
}
