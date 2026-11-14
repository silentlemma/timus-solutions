#![no_main]

use std::ffi::{c_int, c_void};

#[cfg(unix)]
extern "C" {
    fn read(fd: c_int, buffer: *mut c_void, count: usize) -> isize;
    fn write(fd: c_int, buffer: *const c_void, count: usize) -> isize;
}

#[cfg(windows)]
#[link(name = "msvcrt")]
extern "C" {
    #[link_name = "_read"]
    fn read(fd: c_int, buffer: *mut c_void, count: u32) -> c_int;
    #[link_name = "_write"]
    fn write(fd: c_int, buffer: *const c_void, count: u32) -> c_int;
}

const STDIN: c_int = 0;
const STDOUT: c_int = 1;
const INPUT_BLOCK: usize = 4_096;

const MAX_CAMPS: usize = 200;

#[derive(Clone, Copy)]
struct Point(f64, f64);

fn distance(a: Point, b: Point) -> f64 {
    let dx = a.0 - b.0;
    let dy = a.1 - b.1;
    let squared = dx * dx + dy * dy;
    if squared.is_normal() {
        squared.sqrt()
    } else {
        dx.hypot(dy)
    }
}

fn shortest_path(input: &str) -> f64 {
    let mut words = input.split_ascii_whitespace();
    let count: usize = words.next().unwrap().parse().unwrap();
    let mut cycle = [Point(0.0, 0.0); 2 * MAX_CAMPS];
    for point in &mut cycle[..count] {
        point.0 = words.next().unwrap().parse().unwrap();
        point.1 = words.next().unwrap().parse().unwrap();
    }

    cycle.copy_within(..count, count);
    let mut edge = [0.0; 2 * MAX_CAMPS];
    for (i, pair) in cycle[..2 * count].windows(2).enumerate() {
        edge[i] = distance(pair[0], pair[1]);
    }
    let (mut left, mut right) = ([0.0; MAX_CAMPS + 1], [0.0; MAX_CAMPS + 1]);
    for span in 1..count {
        // Preserve the cyclic successor before overwriting the first arc.
        left[count] = left[0];
        right[count] = right[0];
        for start in 0..count {
            let end = start + span;
            let chord = distance(cycle[start], cycle[end]);
            let new_left = (left[start + 1] + edge[start]).min(right[start + 1] + chord);
            let new_right = (left[start] + chord).min(right[start] + edge[end - 1]);
            left[start] = new_left;
            right[start] = new_right;
        }
    }
    left[..count]
        .iter()
        .chain(&right[..count])
        .fold(f64::INFINITY, |best, &length| best.min(length))
}

fn read_input() -> Option<Vec<u8>> {
    let mut data = Vec::new();
    let mut block = [0; INPUT_BLOCK];
    loop {
        // The runtime can write up to INPUT_BLOCK bytes into this array.
        let size = unsafe { read(STDIN, block.as_mut_ptr().cast(), INPUT_BLOCK as _) };
        if size <= 0 {
            return (size == 0).then_some(data);
        }
        data.extend_from_slice(&block[..size as usize]);
    }
}

#[no_mangle]
extern "C" fn main() -> c_int {
    let Some(input) = read_input() else {
        return 1;
    };
    let Ok(text) = std::str::from_utf8(&input) else {
        return 1;
    };
    let best = shortest_path(text);
    let output = format!("{best:.3}\n");
    let mut bytes = output.as_bytes();
    while !bytes.is_empty() {
        // The initialized output remains live until the runtime returns.
        let written = unsafe { write(STDOUT, bytes.as_ptr().cast(), bytes.len() as _) };
        if written <= 0 {
            return 1;
        }
        bytes = &bytes[written as usize..];
    }
    0
}
