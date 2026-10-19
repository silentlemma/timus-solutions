use std::io::{self, Read};

struct Palindromes {
    odd: Vec<usize>,
    even: Vec<usize>,
}
impl Palindromes {
    fn new(word: &[u8]) -> Self {
        let size = word.len();
        let mut odd = vec![0; size];
        let (mut left, mut right) = (0_isize, -1_isize);
        for center in 0..size {
            let index = center as isize;
            let mut radius = if index > right {
                1
            } else {
                odd[(left + right - index) as usize].min((right - index + 1) as usize)
            };
            while center >= radius
                && center + radius < size
                && word[center - radius] == word[center + radius]
            {
                radius += 1;
            }
            odd[center] = radius;
            if index + radius as isize - 1 > right {
                left = index - radius as isize + 1;
                right = index + radius as isize - 1;
            }
        }
        let mut even = vec![0; size];
        left = 0;
        right = -1;
        for center in 0..size {
            let index = center as isize;
            let mut radius = if index > right {
                0
            } else {
                even[(left + right - index + 1) as usize].min((right - index + 1) as usize)
            };
            while center > radius
                && center + radius < size
                && word[center - radius - 1] == word[center + radius]
            {
                radius += 1;
            }
            even[center] = radius;
            if index + radius as isize - 1 > right {
                left = index - radius as isize;
                right = index + radius as isize - 1;
            }
        }
        Self { odd, even }
    }
    fn palindrome(&self, start: usize, end: usize) -> bool {
        let length = end - start;
        let center = (start + end) / 2;
        if length % 2 != 0 {
            self.odd[center] >= length / 2 + 1
        } else {
            self.even[center] >= length / 2
        }
    }
}

fn solve(word: &[u8]) -> (i32, i32) {
    let size = word.len();
    let radii = Palindromes::new(word);
    let mut maximum = vec![-1_i32; size + 1];
    let mut first = vec![-1_isize; size / 2 + 1];
    let mut last = vec![-1_isize; size / 2 + 1];
    maximum[0] = 0;
    let mut highest = -1_i32;
    for end in 1..=size {
        if end >= 2 && maximum[end - 2] >= 0 {
            let value = maximum[end - 2] as usize;
            if first[value] < 0 {
                first[value] = (end - 2) as isize;
            }
            last[value] = (end - 2) as isize;
            highest = highest.max(value as i32);
        }
        for value in [highest, highest - 1] {
            if value < 0 {
                continue;
            }
            let level = value as usize;
            if first[level] >= 0
                && (!radii.palindrome(first[level] as usize, end)
                    || !radii.palindrome(last[level] as usize, end))
            {
                maximum[end] = value + 1;
                break;
            }
        }
    }
    if maximum[size] < 0 {
        return (-1, -1);
    }
    (if radii.palindrome(0, size) { 2 } else { 1 }, maximum[size])
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let word = input.split_whitespace().next().unwrap().as_bytes();
    let (minimum, maximum) = solve(word);
    if minimum < 0 {
        println!("-1");
    } else {
        println!("{} {}", minimum, maximum);
    }
}
