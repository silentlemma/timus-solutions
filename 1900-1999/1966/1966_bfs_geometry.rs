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
const BUFFER_SIZE: usize = 512;
const INPUT_RADIX: i32 = 10;

struct Input {
    bytes: [u8; BUFFER_SIZE],
    start: usize,
    end: usize,
}

impl Input {
    fn new() -> Self {
        Self {
            bytes: [0; BUFFER_SIZE],
            start: 0,
            end: 0,
        }
    }

    fn byte(&mut self) -> Option<u8> {
        if self.start == self.end {
            // The runtime receives the pointer and size of the live buffer.
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

    fn number(&mut self) -> Option<i32> {
        let mut byte = self.byte()?;
        while byte.is_ascii_whitespace() {
            byte = self.byte()?;
        }
        let sign = if byte == b'-' {
            byte = self.byte()?;
            -1
        } else {
            1
        };
        let mut value = 0;
        while byte.is_ascii_digit() {
            value = value * INPUT_RADIX + i32::from(byte - b'0');
            byte = self.byte().unwrap_or(b' ');
        }
        Some(sign * value)
    }
}

fn send(bytes: &[u8]) -> c_int {
    // The answer slice remains initialized for the duration of the call.
    let written = unsafe { write(STDOUT, bytes.as_ptr().cast(), bytes.len() as _) };
    c_int::from(written as usize != bytes.len())
}

const MAX_POINTS: usize = 200;

#[derive(Clone, Copy, Default)]
struct Point {
    x: i16,
    y: i16,
}

#[derive(Clone, Copy, Default)]
struct Segment {
    left: Point,
    right: Point,
    low: i16,
    high: i16,
}

impl Segment {
    fn new(a: Point, b: Point) -> Self {
        let (left, right) = if a.x <= b.x { (a, b) } else { (b, a) };
        Self {
            left,
            right,
            low: a.y.min(b.y),
            high: a.y.max(b.y),
        }
    }

    fn side(self, point: Point) -> i64 {
        let left_x = i64::from(self.left.x);
        let left_y = i64::from(self.left.y);
        let dx = i64::from(self.right.x) - left_x;
        let dy = i64::from(self.right.y) - left_y;
        dx * (i64::from(point.y) - left_y) - dy * (i64::from(point.x) - left_x)
    }

    fn spans(self, other: Self) -> bool {
        let (a, b) = (self.side(other.left), self.side(other.right));
        a.min(b) <= 0 && a.max(b) >= 0
    }

    fn meets(self, other: Self) -> bool {
        self.left.x <= other.right.x
            && other.left.x <= self.right.x
            && self.low <= other.high
            && other.low <= self.high
            && self.spans(other)
            && other.spans(self)
    }

    fn contains(self, point: Point) -> bool {
        self.left.x <= point.x
            && point.x <= self.right.x
            && self.low <= point.y
            && point.y <= self.high
            && self.side(point) == 0
    }
}

fn all_reachable(points: &[Point], endpoints: &[bool], tracks: &mut [Segment]) -> bool {
    for (&point, &endpoint) in points.iter().zip(endpoints) {
        if !endpoint && !tracks.iter().any(|&track| track.contains(point)) {
            return false;
        }
    }
    // The prefix is the BFS queue. Check each reached segment only against
    // unvisited ones and move each discovery to the end of the prefix.
    let (mut head, mut reached) = (0, 1);
    while head < reached && reached < tracks.len() {
        let current = tracks[head];
        for index in reached..tracks.len() {
            if current.meets(tracks[index]) {
                tracks.swap(index, reached);
                reached += 1;
            }
        }
        head += 1;
    }
    reached == tracks.len()
}

fn solve(input: &mut Input) -> Option<bool> {
    let count = input.number()? as usize;
    let track_count = input.number()? as usize;
    let mut points = [Point::default(); MAX_POINTS];
    let points = points.get_mut(..count)?;
    for point in points.iter_mut() {
        *point = Point {
            x: input.number()? as i16,
            y: input.number()? as i16,
        };
    }
    let mut tracks = [Segment::default(); MAX_POINTS];
    let mut endpoints = [false; MAX_POINTS];
    let tracks = tracks.get_mut(..track_count)?;
    for track in tracks.iter_mut() {
        let a = input.number()? as usize - 1;
        let b = input.number()? as usize - 1;
        endpoints[a] = true;
        endpoints[b] = true;
        *track = Segment::new(points[a], points[b]);
    }
    Some(all_reachable(points, &endpoints[..count], tracks))
}

#[no_mangle]
extern "C" fn main() -> c_int {
    match solve(&mut Input::new()) {
        Some(true) => send(b"YES\n"),
        Some(false) => send(b"NO\n"),
        None => 1,
    }
}
