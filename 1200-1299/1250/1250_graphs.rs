use std::io::{self, Read};

const HEADER: usize = 4;

// marks in free (clearing it) every cell reachable from start through cells
// where free is set, moving along the given steps; returns them
fn flood(start: usize, free: &mut [bool], steps: &[isize]) -> Vec<usize> {
    let mut reached = vec![start];
    let mut stack = vec![start];
    free[start] = false;
    while let Some(c) = stack.pop() {
        for &d in steps {
            let n = c as isize + d;
            if n >= 0 && (n as usize) < free.len() && free[n as usize] {
                free[n as usize] = false;
                reached.push(n as usize);
                stack.push(n as usize);
            }
        }
    }
    reached
}

fn main() {
    let mut input = Vec::new();
    io::stdin().read_to_end(&mut input).unwrap();
    // four numbers, then the map characters; anything else is skipped
    let mut k = 0;
    let mut head = [0usize; HEADER];
    for slot in head.iter_mut() {
        while !input[k].is_ascii_digit() {
            k += 1;
        }
        while k < input.len() && input[k].is_ascii_digit() {
            *slot = *slot * 10 + (input[k] - b'0') as usize;
            k += 1;
        }
    }
    let [w, h, x, y] = head;
    let cells: Vec<u8> = input[k..]
        .iter()
        .copied()
        .filter(|&c| c == b'#' || c == b'.')
        .collect();
    // the map padded by a ring of outside cells
    let pw = w + 2;
    let size = (w + 2) * (h + 2);
    let (mut land, mut sea) = (vec![false; size], vec![false; size]);
    for i in 0..h {
        for j in 0..w {
            let c = cells[i * w + j];
            land[(i + 1) * pw + j + 1] = c == b'#';
            sea[(i + 1) * pw + j + 1] = c == b'.';
        }
    }
    let p = pw as isize;
    let step4 = [1, -1, p, -p];
    let step8 = [1, -1, p, -p, p + 1, p - 1, -p + 1, -p - 1];
    // the sacred sea: sea cells joined to the drowning point by 8 directions
    let mut free = vec![true; size];
    let start = y * pw + x;
    if sea[start] {
        for c in flood(start, &mut sea, &step8) {
            free[c] = false;
        }
    }
    // an eight-connected sea stops every four-connected path, so what the
    // outside cannot reach without crossing the sacred sea lies inside it
    for c in flood(0, &mut free, &step4) {
        land[c] = false;
    }
    let mut count = 0;
    for c in 0..size {
        if land[c] {
            count += 1;
            flood(c, &mut land, &step4);
        }
    }
    println!("{}", count);
}
