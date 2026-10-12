use std::io::{self, Read};

const MAX_ROPE: u32 = 30000;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let mut next = || it.next().unwrap().parse::<f64>().unwrap();
    let (ax, ay, bx, by) = (next(), next(), next(), next());
    let (cx, cy) = (next(), next());
    let mut rope = 0;
    for digit in it.next().unwrap().bytes() {
        if digit < b'0' || digit > b'9' {
            continue;
        }
        rope = MAX_ROPE.min(rope * 10 + (digit - b'0') as u32);
        if rope == MAX_ROPE {
            break;
        }
    }
    let rope = rope as f64;
    let (dx, dy) = (bx - ax, by - ay);
    // the nearest point of the bed: C projected onto AB, kept inside it
    let length = dx * dx + dy * dy;
    let t = if length == 0.0 {
        0.0
    } else {
        (((cx - ax) * dx + (cy - ay) * dy) / length).clamp(0.0, 1.0)
    };
    let nearest = (ax + t * dx - cx).hypot(ay + t * dy - cy);
    let farthest = (ax - cx).hypot(ay - cy).max((bx - cx).hypot(by - cy));
    println!("{:.2}", (nearest - rope).max(0.0));
    println!("{:.2}", (farthest - rope).max(0.0));
}
