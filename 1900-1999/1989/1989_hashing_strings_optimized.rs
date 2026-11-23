#![no_main]

use std::io::{self, Write};

const HASH_BLOCK: usize = 64;
const HASH_BASE: u64 = 131;
const CACHE_SIZE: usize = 2048;
const SCAN_FACTOR: usize = 16;

#[derive(Clone, Copy, Default)]
struct HashNode {
    forward: u64,
    backward: u64,
    length: usize,
}

struct HashIndex {
    tree: Vec<HashNode>,
    leaves: usize,
    short_powers: [u64; HASH_BLOCK + 1],
    block_powers: Vec<u64>,
}

impl HashIndex {
    fn power(&self, length: usize) -> u64 {
        self.block_powers[length / HASH_BLOCK].wrapping_mul(self.short_powers[length % HASH_BLOCK])
    }

    fn join(&self, first: HashNode, second: HashNode) -> HashNode {
        HashNode {
            forward: first
                .forward
                .wrapping_mul(self.power(second.length))
                .wrapping_add(second.forward),
            backward: second
                .backward
                .wrapping_mul(self.power(first.length))
                .wrapping_add(first.backward),
            length: first.length + second.length,
        }
    }

    fn characters(word: &[u8], left: usize, end: usize) -> HashNode {
        let mut node = HashNode {
            length: end - left,
            ..HashNode::default()
        };
        for offset in 0..node.length {
            node.forward = node
                .forward
                .wrapping_mul(HASH_BASE)
                .wrapping_add(u64::from(word[left + offset]));
            node.backward = node
                .backward
                .wrapping_mul(HASH_BASE)
                .wrapping_add(u64::from(word[end - 1 - offset]));
        }
        node
    }

    fn new(word: &[u8]) -> Self {
        let blocks = (word.len() + HASH_BLOCK - 1) / HASH_BLOCK;
        let leaves = blocks.next_power_of_two();
        let mut index = Self {
            tree: vec![HashNode::default(); 2 * leaves],
            leaves,
            short_powers: [1; HASH_BLOCK + 1],
            block_powers: vec![1; blocks + 1],
        };
        for i in 1..=HASH_BLOCK {
            index.short_powers[i] = index.short_powers[i - 1].wrapping_mul(HASH_BASE);
        }
        for i in 1..=blocks {
            index.block_powers[i] =
                index.block_powers[i - 1].wrapping_mul(index.short_powers[HASH_BLOCK]);
        }
        for block in 0..blocks {
            index.tree[leaves + block] = Self::characters(
                word,
                block * HASH_BLOCK,
                ((block + 1) * HASH_BLOCK).min(word.len()),
            );
        }
        for node in (1..leaves).rev() {
            index.tree[node] = index.join(index.tree[2 * node], index.tree[2 * node + 1]);
        }
        index
    }

    fn update(&mut self, word: &[u8], position: usize) {
        let block = position / HASH_BLOCK;
        let mut node = self.leaves + block;
        self.tree[node] = Self::characters(
            word,
            block * HASH_BLOCK,
            ((block + 1) * HASH_BLOCK).min(word.len()),
        );
        node /= 2;
        while node != 0 {
            self.tree[node] = self.join(self.tree[2 * node], self.tree[2 * node + 1]);
            node /= 2;
        }
    }

    fn blocks(&self, mut first: usize, mut end: usize) -> HashNode {
        let (mut before, mut after) = (HashNode::default(), HashNode::default());
        first += self.leaves;
        end += self.leaves;
        while first < end {
            if first & 1 != 0 {
                before = self.join(before, self.tree[first]);
                first += 1;
            }
            if end & 1 != 0 {
                end -= 1;
                after = self.join(self.tree[end], after);
            }
            first /= 2;
            end /= 2;
        }
        self.join(before, after)
    }

    fn range(&self, word: &[u8], mut left: usize, end: usize) -> HashNode {
        let mut node = HashNode::default();
        if left % HASH_BLOCK != 0 {
            let stop = end.min((left / HASH_BLOCK + 1) * HASH_BLOCK);
            node = Self::characters(word, left, stop);
            left = stop;
        }
        if left == end {
            return node;
        }
        node = self.join(node, self.blocks(left / HASH_BLOCK, end / HASH_BLOCK));
        let tail = end / HASH_BLOCK * HASH_BLOCK;
        if tail < end {
            node = self.join(node, Self::characters(word, tail, end));
        }
        node
    }
}

#[derive(Clone, Copy, Default)]
struct Proof {
    center: usize,
    left: usize,
    end: usize,
    version: usize,
    palindrome: bool,
}

fn radii(word: &[u8]) -> (Vec<u16>, Vec<u16>) {
    // Both radii fit u16 for a word of at most 100000 characters.
    let size = word.len() as isize;
    let mut odd = vec![0_u16; word.len()];
    let (mut left, mut right) = (0_isize, -1_isize);
    for i in 0..size {
        let mut reach = if i > right {
            1
        } else {
            (odd[(left + right - i) as usize] as isize).min(right - i + 1)
        };
        while i - reach >= 0
            && i + reach < size
            && word[(i - reach) as usize] == word[(i + reach) as usize]
        {
            reach += 1;
        }
        odd[i as usize] = reach as u16;
        if i + reach - 1 > right {
            left = i - reach + 1;
            right = i + reach - 1;
        }
    }
    let mut even = vec![0_u16; word.len()];
    (left, right) = (0, -1);
    for i in 0..size {
        let mut reach = if i > right {
            0
        } else {
            (even[(left + right - i + 1) as usize] as isize).min(right - i + 1)
        };
        while i - reach > 0
            && i + reach < size
            && word[(i - reach - 1) as usize] == word[(i + reach) as usize]
        {
            reach += 1;
        }
        even[i as usize] = reach as u16;
        if i + reach - 1 > right {
            left = i - reach;
            right = i + reach - 1;
        }
    }
    (odd, even)
}

fn solve_entry() {
    let mut tokens = TokenInput::new();
    let mut word = tokens.next().unwrap().as_bytes().to_vec();
    let size = word.len();
    let mut reverse: Vec<u8> = word.iter().rev().copied().collect();
    let mut different = word.windows(2).filter(|pair| pair[0] != pair[1]).count();
    let mut hashes = HashIndex::new(&word);
    let mut proofs = vec![Proof::default(); CACHE_SIZE];
    let mut version = 1;
    let mut scanned = 0;
    let mut static_radii: Option<(Vec<u16>, Vec<u16>)> = None;
    let operations: usize = parse_integer(tokens.next().unwrap());
    let mut answer = String::new();
    for _ in 0..operations {
        let operation = tokens.next().unwrap();
        let left: usize = parse_integer::<usize>(tokens.next().unwrap()) - 1;
        let right = tokens.next().unwrap();
        if operation == "change" {
            let value = right.as_bytes()[0];
            if word[left] == value {
                continue;
            }
            if left > 0 {
                different -= usize::from(word[left - 1] != word[left]);
            }
            if left + 1 < size {
                different -= usize::from(word[left] != word[left + 1]);
            }
            word[left] = value;
            reverse[size - 1 - left] = value;
            if left > 0 {
                different += usize::from(word[left - 1] != word[left]);
            }
            if left + 1 < size {
                different += usize::from(word[left] != word[left + 1]);
            }
            hashes.update(&word, left);
            version += 1;
            scanned = 0;
            static_radii = None;
        } else {
            let end: usize = parse_integer(right);
            let length = end - left;
            let half = length / 2;
            let center = left + end;
            let proof = proofs[center % CACHE_SIZE];
            let palindrome = if half == 0 || different == 0 {
                true
            } else if word[left] != word[end - 1] {
                false
            } else if let Some((odd, even)) = &static_radii {
                if length & 1 != 0 {
                    usize::from(odd[center / 2]) > half
                } else {
                    usize::from(even[center / 2]) >= half
                }
            } else if proof.version == version
                && proof.center == center
                && ((proof.palindrome && left >= proof.left && end <= proof.end)
                    || (!proof.palindrome && left <= proof.left && end >= proof.end))
            {
                proof.palindrome
            } else {
                let digest = hashes.range(&word, left, end);
                // Unequal hashes prove No. Equal hashes never certify Yes:
                // compare the actual bytes, so collisions cannot change an answer.
                let equal = if digest.forward != digest.backward {
                    false
                } else {
                    scanned += half;
                    word[left..left + half] == reverse[size - end..size - end + half]
                };
                proofs[center % CACHE_SIZE] = Proof {
                    center,
                    left,
                    end,
                    version,
                    palindrome: equal,
                };
                // Preprocess a static epoch only after enough exact scanning.
                if scanned >= SCAN_FACTOR * size {
                    static_radii = Some(radii(&word));
                }
                equal
            };
            answer.push_str(if palindrome { "Yes\n" } else { "No\n" });
        }
    }
    io::stdout().write_all(answer.as_bytes()).unwrap();
}

// Input bounds guarantee that each decimal token fits its destination integer.
// Accumulate negative values directly so the minimum signed integer also fits.
fn parse_integer<T>(word: impl AsRef<[u8]>) -> T
where
    T: From<u8> + std::ops::Add<Output = T> + std::ops::Sub<Output = T> + std::ops::Mul<Output = T>,
{
    let digits = word.as_ref();
    let negative = digits[0] == b'-';
    let start = usize::from(negative || digits[0] == b'+');
    let mut value = T::from(0);
    for &byte in &digits[start..] {
        let digit = T::from(byte - b'0');
        let scaled = value * T::from(10);
        value = if negative {
            scaled - digit
        } else {
            scaled + digit
        };
    }
    value
}

const INPUT_BUFFER_BYTES: usize = 4096;

#[cfg(windows)]
#[link(name = "msvcrt")]
extern "C" {
    #[link_name = "_read"]
    fn input_read(fd: i32, data: *mut u8, size: u32) -> i32;
}

#[cfg(not(windows))]
extern "C" {
    #[link_name = "read"]
    fn input_read(fd: i32, data: *mut u8, size: usize) -> isize;
}

struct TokenInput {
    buffer: [u8; INPUT_BUFFER_BYTES],
    position: usize,
    length: usize,
}

impl TokenInput {
    fn new() -> Self {
        Self {
            buffer: [0; INPUT_BUFFER_BYTES],
            position: 0,
            length: 0,
        }
    }

    fn byte(&mut self) -> Option<u8> {
        if self.position == self.length {
            loop {
                // SAFETY: the live writable array is passed with its exact bounded length.
                let count = unsafe {
                    #[cfg(windows)]
                    {
                        input_read(0, self.buffer.as_mut_ptr(), INPUT_BUFFER_BYTES as u32)
                    }
                    #[cfg(not(windows))]
                    {
                        input_read(0, self.buffer.as_mut_ptr(), INPUT_BUFFER_BYTES)
                    }
                };
                if count > 0 {
                    self.position = 0;
                    self.length = count as usize;
                    break;
                }
                if count == 0 {
                    return None;
                }
                let error = io::Error::last_os_error();
                if error.kind() != io::ErrorKind::Interrupted {
                    panic!("stdin read failed: {error}");
                }
            }
        }
        let byte = self.buffer[self.position];
        self.position += 1;
        Some(byte)
    }
}

struct InputWord {
    inline: [u8; 32],
    length: usize,
    spill: Vec<u8>,
}

impl InputWord {
    #[inline]
    fn push(&mut self, byte: u8) {
        if self.length < self.inline.len() {
            self.inline[self.length] = byte;
        } else {
            if self.spill.is_empty() {
                self.spill.extend_from_slice(&self.inline);
            }
            self.spill.push(byte);
        }
        self.length += 1;
    }
}

impl AsRef<[u8]> for InputWord {
    fn as_ref(&self) -> &[u8] {
        if self.length <= self.inline.len() {
            &self.inline[..self.length]
        } else {
            &self.spill
        }
    }
}

impl std::ops::Deref for InputWord {
    type Target = str;
    fn deref(&self) -> &str {
        std::str::from_utf8(self.as_ref()).unwrap()
    }
}

impl PartialEq<&str> for InputWord {
    fn eq(&self, other: &&str) -> bool {
        self.as_ref() == other.as_bytes()
    }
}

impl Iterator for TokenInput {
    type Item = InputWord;
    #[inline]
    fn next(&mut self) -> Option<InputWord> {
        let mut first = self.byte()?;
        while first.is_ascii_whitespace() {
            first = self.byte()?;
        }
        let mut word = InputWord {
            inline: [0; 32],
            length: 0,
            spill: Vec::new(),
        };
        word.push(first);
        while let Some(byte) = self.byte() {
            if byte.is_ascii_whitespace() {
                break;
            }
            word.push(byte);
        }
        Some(word)
    }
}

// Run the algorithm directly and flush Rust's global output before returning to C.
#[no_mangle]
pub extern "C" fn main() -> i32 {
    solve_entry();
    std::io::Write::flush(&mut std::io::stdout()).unwrap();
    0
}
