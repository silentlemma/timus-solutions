use std::io::{self, Read, Write};
use std::ops::Range;

const MAX_LENGTH: usize = 140;
const MAX_USERS: usize = 100;
const MAX_NAME_LENGTH: usize = 30;
const PREFIX: usize = "RT @: ".len();
const INPUT_SIZE: usize = 1024;
const NAME_SLOTS: usize = 256;
const HASH_MULTIPLIER: u32 = 16_777_619;
const HASH_INITIAL: u32 = 2_166_136_261;
const COUNT_DIGITS: usize = 3;
const OUTPUT_SIZE: usize = MAX_USERS * (MAX_NAME_LENGTH + 1) + COUNT_DIGITS + 1;
const DECIMAL: usize = 10;

struct Input<R> {
    reader: R,
    bytes: [u8; INPUT_SIZE],
    cursor: usize,
    end: usize,
}

impl<R: Read> Input<R> {
    fn peek(&mut self) -> Option<u8> {
        if self.cursor == self.end {
            let size = self.reader.read(&mut self.bytes).ok()?;
            if size == 0 {
                return None;
            }
            self.cursor = 0;
            self.end = size;
        }
        Some(self.bytes[self.cursor])
    }

    fn skip_spaces(&mut self) -> Option<()> {
        while self.peek()?.is_ascii_whitespace() {
            self.cursor += 1;
        }
        Some(())
    }

    fn number(&mut self) -> Option<usize> {
        self.skip_spaces()?;
        let mut value = 0;
        while let Some(digit) = self.peek().filter(u8::is_ascii_digit) {
            value = value * DECIMAL + usize::from(digit - b'0');
            self.cursor += 1;
        }
        Some(value)
    }

    fn name(&mut self) -> Option<(Name, u32)> {
        self.skip_spaces()?;
        let mut name = EMPTY_NAME;
        let mut hash = HASH_INITIAL;
        while let Some(byte) = self.peek().filter(|byte| !byte.is_ascii_whitespace()) {
            *name.bytes.get_mut(usize::from(name.len))? = byte;
            name.len += 1;
            hash = (hash ^ u32::from(byte)).wrapping_mul(HASH_MULTIPLIER);
            self.cursor += 1;
        }
        Some((name, hash))
    }

    fn tweet_length(&mut self) -> Option<usize> {
        // Leave the last follower's delimiter for this step. Only the
        // account line is skipped, so spaces in the tweet are counted.
        loop {
            let byte = self.peek()?;
            self.cursor += 1;
            if byte == b'\n' {
                break;
            }
        }
        let (mut size, mut last) = (0usize, 0);
        while let Some(byte) = self.peek() {
            self.cursor += 1;
            if byte == b'\n' {
                break;
            }
            size += 1;
            last = byte;
        }
        Some(size - usize::from(last == b'\r'))
    }
}

#[derive(Clone, Copy, PartialEq, Eq)]
struct Name {
    bytes: [u8; MAX_NAME_LENGTH],
    len: u8,
}

const EMPTY_NAME: Name = Name {
    bytes: [0; MAX_NAME_LENGTH],
    len: 0,
};

impl Name {
    fn text(&self) -> &[u8] {
        &self.bytes[..usize::from(self.len)]
    }
}

struct Names {
    entries: [Name; MAX_USERS],
    slots: [u8; NAME_SLOTS],
    count: usize,
}

impl Names {
    fn intern(&mut self, (name, hash): (Name, u32)) -> Option<usize> {
        let mut slot = hash as usize % NAME_SLOTS;
        loop {
            let stored = self.slots[slot];
            if stored == 0 {
                let id = self.count;
                *self.entries.get_mut(id)? = name;
                self.count += 1;
                self.slots[slot] = self.count as u8;
                return Some(id);
            }
            let id = usize::from(stored) - 1;
            if self.entries[id] == name {
                return Some(id);
            }
            slot = (slot + 1) % NAME_SLOTS;
        }
    }
}

fn reachable(length: usize, audience: &[u128; MAX_USERS], names: &Names) -> u128 {
    let mut buckets = [0u128; MAX_LENGTH + 1];
    let (mut sent, mut knows) = (0u128, 1u128);
    buckets[length] = 1;
    let everyone = (1u128 << names.count) - 1;
    // Processing by increasing length sends only each user's shortest retweet.
    for length in length..=MAX_LENGTH {
        let mut waiting = buckets[length] & !sent;
        while waiting != 0 {
            let user = waiting.trailing_zeros() as usize;
            waiting &= waiting - 1;
            sent |= 1 << user;
            knows |= audience[user];
            if knows == everyone {
                return knows;
            }
            let longer = length + PREFIX + usize::from(names.entries[user].len);
            if longer <= MAX_LENGTH {
                buckets[longer] |= audience[user] & !sent;
            }
        }
    }
    knows
}

fn solve(input: &mut Input<impl Read>, output: &mut [u8; OUTPUT_SIZE]) -> Option<Range<usize>> {
    let mut names = Names {
        entries: [EMPTY_NAME; MAX_USERS],
        slots: [0; NAME_SLOTS],
        count: 0,
    };
    let mut audience = [0u128; MAX_USERS];
    for _ in 0..input.number()? {
        let user = names.intern(input.name()?)?;
        for _ in 0..input.number()? {
            let follower = names.intern(input.name()?)?;
            audience[user] |= 1 << follower;
        }
    }
    let length = input.tweet_length()?;
    if length > MAX_LENGTH {
        return None;
    }
    let mut knows = reachable(length, &audience, &names);
    let mut count = knows.count_ones() as usize;
    let mut begin = COUNT_DIGITS;
    let mut end = begin + 1;
    output[begin] = b'\n';
    while count != 0 {
        begin -= 1;
        output[begin] = b'0' + (count % DECIMAL) as u8;
        count /= DECIMAL;
    }
    while knows != 0 {
        let user = knows.trailing_zeros() as usize;
        knows &= knows - 1;
        let name = names.entries[user].text();
        let after = end + name.len();
        output[end..after].copy_from_slice(name);
        output[after] = b'\n';
        end = after + 1;
    }
    Some(begin..end)
}

fn main() -> io::Result<()> {
    let mut input = Input {
        reader: io::stdin().lock(),
        bytes: [0; INPUT_SIZE],
        cursor: 0,
        end: 0,
    };
    let mut output = [0; OUTPUT_SIZE];
    let answer = solve(&mut input, &mut output).ok_or(io::ErrorKind::InvalidData)?;
    io::stdout().lock().write_all(&output[answer])
}
