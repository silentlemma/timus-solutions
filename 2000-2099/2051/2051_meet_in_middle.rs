use std::io::{self, Read, Write};

#[derive(Clone, Copy)]
struct Point {
    time: i64,
    height: i64,
}
type Curve = Vec<Point>;

fn contacts_of(upper: &[Point], lower: &[Point], duration: i64) -> Curve {
    let (mut i, mut j, mut time) = (0, 0, 0);
    let mut contacts = Vec::new();
    loop {
        while i + 2 < upper.len() && upper[i + 1].time <= time {
            i += 1;
        }
        while j + 2 < lower.len() && lower[j + 1].time <= time {
            j += 1;
        }
        let (a, b, c, d) = (upper[i], upper[i + 1], lower[j], lower[j + 1]);
        let hn = a.height * (b.time - time) + b.height * (time - a.time);
        let gn = c.height * (d.time - time) + d.height * (time - c.time);
        let (hd, gd) = (b.time - a.time, d.time - c.time);
        if hn * gd == gn * hd && time > 0 && time < duration {
            contacts.push(Point {
                time,
                height: hn / hd,
            });
        }
        if time == duration {
            return contacts;
        }
        time = b.time.min(d.time);
    }
}

fn augment(curve: &[Point], contacts: &[Point]) -> Curve {
    let mut result = Vec::with_capacity(curve.len() + contacts.len());
    let (mut i, mut j) = (0, 0);
    while i < curve.len() || j < contacts.len() {
        if j == contacts.len() || (i < curve.len() && curve[i].time < contacts[j].time) {
            result.push(curve[i]);
            i += 1;
        } else if i == curve.len() || contacts[j].time < curve[i].time {
            result.push(contacts[j]);
            j += 1;
        } else {
            result.push(curve[i]);
            i += 1;
            j += 1;
        }
    }
    result
}

fn areas(curve: &[Point], boundaries: &[i64]) -> Vec<i64> {
    let mut result = Vec::new();
    let (mut total, mut region) = (0, 1);
    for pair in curve.windows(2) {
        let (a, b) = (pair[0], pair[1]);
        total += (a.height + b.height) * (b.time - a.time);
        if b.time == boundaries[region] {
            result.push(total);
            total = 0;
            region += 1;
        }
    }
    result
}

fn choose(weights: &[i64]) -> u32 {
    let left_count = weights.len() / 2;
    let scale = 1_i64 << left_count;
    let target = weights.iter().sum::<i64>() / 2;
    let mut keys = Vec::with_capacity(1 << left_count);
    keys.push(0);
    for (bit, &weight) in weights.iter().take(left_count).enumerate() {
        let step = weight * scale + (1_i64 << bit);
        let old_size = keys.len();
        for index in 0..old_size {
            keys.push(keys[index] + step);
        }
    }
    keys.sort_unstable();
    let (mut previous, mut right_sum) = (0_u32, 0_i64);
    for index in 0_u32..(1_u32 << (weights.len() - left_count)) {
        let gray = index ^ (index >> 1);
        if index != 0 {
            let changed = gray ^ previous;
            let bit = changed.trailing_zeros() as usize;
            let weight = weights[left_count + bit];
            right_sum += if gray & changed != 0 { weight } else { -weight };
        }
        previous = gray;
        let need = target - right_sum;
        let position = keys.partition_point(|&key| key < need * scale);
        if position < keys.len() && keys[position] / scale == need {
            return (keys[position] & (scale - 1)) as u32 | (gray << left_count);
        }
    }
    0
}

fn add(curve: &mut Curve, p: Point) {
    if curve.last().is_some_and(|last| last.time == p.time) {
        return;
    }
    while curve.len() >= 2 {
        let (a, b) = (curve[curve.len() - 2], curve[curve.len() - 1]);
        if (b.height - a.height) * (p.time - b.time) != (p.height - b.height) * (b.time - a.time) {
            break;
        }
        curve.pop();
    }
    curve.push(p);
}

fn solve(duration: i64, original_upper: &[Point], original_lower: &[Point]) -> [Curve; 2] {
    let contacts = contacts_of(original_upper, original_lower, duration);
    let mut boundaries = vec![0];
    boundaries.extend(contacts.iter().map(|p| p.time));
    boundaries.push(duration);
    let upper = augment(original_upper, &contacts);
    let lower = augment(original_lower, &contacts);
    let ua = areas(&upper, &boundaries);
    let la = areas(&lower, &boundaries);
    let weights: Vec<i64> = ua.iter().zip(&la).map(|(a, b)| a - b).collect();
    let mask = choose(&weights);
    let mut result = [Vec::new(), Vec::new()];
    let (mut hi, mut lo) = (0, 0);
    for region in 0..boundaries.len() - 1 {
        let destination = if mask & (1_u32 << region) != 0 { 0 } else { 1 };
        let end = boundaries[region + 1];
        while hi < upper.len() && upper[hi].time <= end {
            add(&mut result[destination], upper[hi]);
            hi += 1;
        }
        while lo < lower.len() && lower[lo].time <= end {
            add(&mut result[1 - destination], lower[lo]);
            lo += 1;
        }
        hi -= 1;
        lo -= 1;
    }
    result
}

fn read_curve(fields: &mut std::str::SplitWhitespace<'_>) -> Curve {
    let count: usize = fields.next().unwrap().parse().unwrap();
    (0..count)
        .map(|_| Point {
            time: fields.next().unwrap().parse().unwrap(),
            height: fields.next().unwrap().parse().unwrap(),
        })
        .collect()
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut fields = input.split_whitespace();
    let duration = fields.next().unwrap().parse().unwrap();
    let upper = read_curve(&mut fields);
    let lower = read_curve(&mut fields);
    let mut out = io::BufWriter::new(io::stdout().lock());
    for curve in solve(duration, &upper, &lower) {
        writeln!(out, "{}", curve.len()).unwrap();
        for p in curve {
            writeln!(out, "{} {}", p.time, p.height).unwrap();
        }
    }
}
