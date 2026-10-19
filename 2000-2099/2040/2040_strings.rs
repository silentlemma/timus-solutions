use std::io::{self, Read, Write};

const MAX_INPUT: usize = 5_000_000 + 16;
// bit 4 is clear in 'a' and 'b'; it marks the positions that add a palindrome
const MARK: u8 = 4;

fn main() {
    // one buffer of fixed capacity: the word, and then the answer in its place
    let mut data = Vec::with_capacity(MAX_INPUT);
    io::stdin().read_to_end(&mut data).unwrap();
    let start = data.iter().position(|b| b.is_ascii_lowercase()).unwrap_or(data.len());
    let end = data[start..]
        .iter()
        .position(|b| !b.is_ascii_lowercase())
        .map_or(data.len(), |k| start + k);
    let n = end - start;
    // node 0 is the imaginary root of length -1, node 1 the empty string
    let mut length = vec![0i32; n + 2];
    let mut link = vec![0u32; n + 2];
    let mut next = [vec![0u32; n + 2], vec![0u32; n + 2]];
    length[0] = -1;
    let word = &mut data[start..end];
    let (mut last, mut used) = (1u32, 2u32);
    for pos in 0..n {
        let c = word[pos];
        let letter = (c - b'a') as usize;
        let mut parent = last as usize;
        loop {
            let before = pos as i64 - 1 - length[parent] as i64;
            if before >= 0 && word[before as usize] & !MARK == c {
                break;
            }
            parent = link[parent] as usize;
        }
        let mut current = next[letter][parent];
        if current == 0 {
            current = used;
            used += 1;
            let cur = current as usize;
            length[cur] = length[parent] + 2;
            next[letter][parent] = current;
            if length[cur] == 1 {
                link[cur] = 1;
            } else {
                let mut candidate = link[parent] as usize;
                loop {
                    let before = pos as i64 - 1 - length[candidate] as i64;
                    if before >= 0 && word[before as usize] & !MARK == c {
                        break;
                    }
                    candidate = link[candidate] as usize;
                }
                link[cur] = next[letter][candidate];
            }
            word[pos] |= MARK;
        }
        last = current;
    }
    for b in word.iter_mut() {
        *b = if *b & MARK != 0 { b'1' } else { b'0' };
    }
    let stdout = io::stdout();
    let mut w = stdout.lock();
    w.write_all(&data[start..end]).unwrap();
    w.write_all(b"\n").unwrap();
}
