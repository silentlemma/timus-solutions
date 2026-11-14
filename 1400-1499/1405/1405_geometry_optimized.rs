#![no_main]

use std::f64::consts::PI;
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

const CENTIMETRES: i32 = 100;
const MIN_ROPE: i32 = CENTIMETRES;
const MAX_ROPE: i32 = 50 * CENTIMETRES;
const MIN_SEPARATION: i32 = 2 * MIN_ROPE;
const DECIMAL_PLACES: usize = 4;
const MAX_TREES: usize = 1_000;
const BUFFER_SIZE: usize = 512;
const OUTPUT_SIZE: usize = 20;
const DECIMAL: i32 = 10;
const STDIN: c_int = 0;
const STDOUT: c_int = 1;

#[derive(Clone, Copy)]
struct Point(i16, i16);

impl Point {
    fn x_distance(self, other: Self) -> i32 {
        i32::from(self.0) - i32::from(other.0)
    }

    fn distance_squared(self, other: Self) -> i32 {
        let dx = self.x_distance(other);
        let dy = i32::from(self.1) - i32::from(other.1);
        dx * dx + dy * dy
    }
}

fn nearest(point: Point, neighbors: impl Iterator<Item = Point>, upper: i32) -> i32 {
    let mut best = upper;
    for other in neighbors {
        let dx = point.x_distance(other);
        if dx * dx >= best {
            break;
        }
        best = best.min(point.distance_squared(other));
    }
    best
}

fn largest_squared_sum(points: &mut [Point]) -> f64 {
    points.sort_unstable_by_key(|p| p.0);
    let mut eligible = [(Point(0, 0), 0); MAX_TREES];
    let mut count = 0;
    for (i, &point) in points.iter().enumerate() {
        // Neighbors farther away in x cannot improve the current bound.
        let left = nearest(
            point,
            points[..i].iter().rev().copied(),
            MAX_ROPE * MAX_ROPE,
        );
        let bound = nearest(point, points[i + 1..].iter().copied(), left);
        if bound >= MIN_ROPE * MIN_ROPE {
            eligible[count] = (point, bound);
            count += 1;
        }
    }
    let candidates = &mut eligible[..count];
    candidates.sort_unstable_by(|a, b| b.1.cmp(&a.1));
    let mut best: f64 = 0.0;
    let minimum = f64::from(MIN_ROPE);
    for (i, &(point, a_squared)) in candidates.iter().enumerate() {
        for &(other, b_squared) in &candidates[i + 1..] {
            let upper = f64::from(a_squared + b_squared);
            if upper <= best {
                break;
            }
            let separation_squared = point.distance_squared(other);
            if separation_squared < MIN_SEPARATION * MIN_SEPARATION {
                continue;
            }
            let (a, b) = (f64::from(a_squared).sqrt(), f64::from(b_squared).sqrt());
            let distance = f64::from(separation_squared).sqrt();
            if distance >= a + b {
                best = upper;
                break;
            }
            // On the boundary a + b = distance, test both endpoints.
            let large_a = a.min(distance - minimum);
            let large_b = b.min(distance - minimum);
            let small_a = distance - large_b;
            let small_b = distance - large_a;
            best = best
                .max(large_a * large_a + small_b * small_b)
                .max(small_a * small_a + large_b * large_b);
        }
    }
    best
}

struct Input {
    bytes: [u8; BUFFER_SIZE],
    start: usize,
    end: usize,
}

impl Input {
    fn byte(&mut self) -> Option<u8> {
        if self.start == self.end {
            // The buffer holds every byte requested from the runtime.
            let size = unsafe { read(STDIN, self.bytes.as_mut_ptr().cast(), BUFFER_SIZE as _) };
            if size <= 0 {
                return None;
            }
            self.start = 0;
            self.end = size as usize;
        }
        let byte = self.bytes[self.start];
        self.start += 1;
        Some(byte)
    }

    fn centimetres(&mut self) -> Option<i32> {
        let mut byte = self.byte()?;
        while byte.is_ascii_whitespace() {
            byte = self.byte()?;
        }
        let sign = if byte == b'-' { -1 } else { 1 };
        if matches!(byte, b'+' | b'-') {
            byte = self.byte()?;
        }
        let mut whole = 0;
        while byte.is_ascii_digit() {
            whole = whole * DECIMAL + i32::from(byte - b'0');
            byte = self.byte().unwrap_or(b' ');
        }
        let mut fraction = 0;
        if byte == b'.' {
            // Coordinates are given to the centimetre.
            let mut factor = CENTIMETRES / DECIMAL;
            byte = self.byte().unwrap_or(b' ');
            while byte.is_ascii_digit() {
                fraction += i32::from(byte - b'0') * factor;
                factor /= DECIMAL;
                byte = self.byte().unwrap_or(b' ');
            }
        }
        Some(sign * (whole * CENTIMETRES + fraction))
    }
}

fn answer(input: &mut Input) -> Option<u64> {
    let count = (input.centimetres()? / CENTIMETRES) as usize;
    let mut points = [Point(0, 0); MAX_TREES];
    let points = points.get_mut(..count)?;
    for point in points.iter_mut() {
        *point = Point(input.centimetres()? as i16, input.centimetres()? as i16);
    }
    Some((PI * largest_squared_sum(points)).round() as u64)
}

#[no_mangle]
extern "C" fn main() -> c_int {
    let mut input = Input {
        bytes: [0; BUFFER_SIZE],
        start: 0,
        end: 0,
    };
    let Some(mut area) = answer(&mut input) else {
        return 1;
    };
    let mut output = [b'\n'; OUTPUT_SIZE];
    let mut start = OUTPUT_SIZE - 1;
    let base = DECIMAL as u64;
    for _ in 0..DECIMAL_PLACES {
        start -= 1;
        output[start] = b'0' + (area % base) as u8;
        area /= base;
    }
    start -= 1;
    output[start] = b'.';
    loop {
        start -= 1;
        output[start] = b'0' + (area % base) as u8;
        area /= base;
        if area == 0 {
            break;
        }
    }
    let bytes = &output[start..];
    // The output remains valid for the entire write.
    if unsafe { write(STDOUT, bytes.as_ptr().cast(), bytes.len() as _) } as usize == bytes.len() {
        0
    } else {
        1
    }
}
