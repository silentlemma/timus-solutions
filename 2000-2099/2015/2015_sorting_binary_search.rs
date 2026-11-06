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

const INPUT_SIZE: usize = 64;
const OUTPUT_SIZE: usize = 96;
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

    fn number(&mut self) -> u64 {
        let mut c = self.next_byte();
        while c != 0 && c <= b' ' {
            c = self.next_byte();
        }
        let mut value = 0;
        while c.is_ascii_digit() {
            value = value * 10 + u64::from(c - b'0');
            c = self.next_byte();
        }
        value
    }
}

fn write_number(output: &mut [u8], used: &mut usize, mut value: u64) {
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

const MAX_FRIENDS: usize = 256;

#[derive(Clone, Copy)]
struct Friend {
    budget: i32,
    benefit: i32,
    id: u16,
}

fn write_text(output: &mut [u8], used: &mut usize, text: &[u8]) {
    output[*used..*used + text.len()].copy_from_slice(text);
    *used += text.len();
}

// The C runtime calls this symbol directly.
#[no_mangle]
pub extern "C" fn main() -> i32 {
    let mut input = Input {
        bytes: [0; INPUT_SIZE],
        position: 0,
        length: 0,
    };
    let budget = input.number() as i32;
    let alone = [input.number() as i32, input.number() as i32];
    let n = input.number() as usize;
    let mut friends = [Friend {
        budget: 0,
        benefit: 0,
        id: 0,
    }; MAX_FRIENDS];
    for (index, friend) in friends[..n].iter_mut().enumerate() {
        *friend = Friend {
            budget: input.number() as i32,
            benefit: input.number() as i32,
            id: (index + 1) as u16,
        };
    }
    friends[..n].sort_unstable_by_key(|friend| friend.budget);
    // Keep the budget order while storing the best choice in each suffix.
    for i in (1..n).rev() {
        if friends[i].benefit > friends[i - 1].benefit {
            friends[i - 1].benefit = friends[i].benefit;
            friends[i - 1].id = friends[i].id;
        }
    }
    let mut best = -1;
    let mut choice = (0, 0u16);
    let apartments = input.number();
    for apartment in 1..=apartments {
        let rooms = input.number();
        let rent = input.number() as i32;
        let benefit = input.number() as i32;
        if rent <= budget {
            let score = benefit + alone[(rooms - 1) as usize];
            if score > best {
                best = score;
                choice = (apartment, 0);
            }
        }
        if rooms == 2 && rent <= 2 * budget {
            let start = friends[..n].partition_point(|friend| 2 * friend.budget < rent);
            if let Some(friend) = friends[..n].get(start) {
                let score = benefit + friend.benefit;
                if score > best {
                    best = score;
                    choice = (apartment, friend.id);
                }
            }
        }
    }
    if choice.0 == 0 {
        return i32::from(!write_all(
            b"Forget about apartments. Live in the dormitory.\n",
        ));
    }
    let mut output = [0; OUTPUT_SIZE];
    let mut used = 0;
    write_text(&mut output, &mut used, b"You should rent the apartment #");
    write_number(&mut output, &mut used, choice.0);
    if choice.1 == 0 {
        write_text(&mut output, &mut used, b" alone.\n");
    } else {
        write_text(&mut output, &mut used, b" with the friend #");
        write_number(&mut output, &mut used, u64::from(choice.1));
        write_text(&mut output, &mut used, b".\n");
    }
    i32::from(!write_all(&output[..used]))
}
