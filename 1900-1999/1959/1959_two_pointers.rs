use std::fmt::Write;
use std::io::{self, Read};

struct Modes {
    frequency: Vec<usize>,
    previous: Vec<usize>,
    following: Vec<usize>,
    head: Vec<usize>,
    maximum: usize,
}

impl Modes {
    fn new(alphabet: usize, capacity: usize) -> Self {
        Self {
            frequency: vec![0; alphabet + 1],
            previous: vec![0; alphabet + 1],
            following: vec![0; alphabet + 1],
            head: vec![0; capacity + 1],
            maximum: 0,
        }
    }
    fn change(&mut self, value: usize, add: bool) {
        let old = self.frequency[value];
        if old != 0 {
            let (left, right) = (self.previous[value], self.following[value]);
            if left != 0 {
                self.following[left] = right;
            } else {
                self.head[old] = right;
            }
            if right != 0 {
                self.previous[right] = left;
            }
        }
        let count = if add { old + 1 } else { old - 1 };
        self.frequency[value] = count;
        if count != 0 {
            let first = self.head[count];
            self.previous[value] = 0;
            self.following[value] = first;
            if first != 0 {
                self.previous[first] = value;
            }
            self.head[count] = value;
        } else {
            self.previous[value] = 0;
            self.following[value] = 0;
        }
        self.maximum = self.maximum.max(count);
        while self.maximum > 0 && self.head[self.maximum] == 0 {
            self.maximum -= 1;
        }
    }
    fn mode(&self) -> usize {
        self.head[self.maximum]
    }
}

fn restore(text: &mut [usize], pattern: &mut [usize]) {
    let (n, m) = (text.len(), pattern.len());
    let gap = n - m;
    let alphabet = *text.iter().chain(pattern.iter()).max().unwrap();
    if text.contains(&0) {
        let mut counter = Modes::new(alphabet, m);
        for (index, value) in text.iter_mut().enumerate() {
            if index < m {
                counter.change(pattern[index], true);
            }
            if index > gap {
                counter.change(pattern[index - gap - 1], false);
            }
            if *value == 0 {
                *value = counter.mode();
            }
        }
    } else if pattern.contains(&0) {
        let width = gap + 1;
        let mut counter = Modes::new(alphabet, width);
        for &value in &text[..width] {
            counter.change(value, true);
        }
        for (index, value) in pattern.iter_mut().enumerate() {
            if *value == 0 {
                *value = counter.mode();
            }
            if index + 1 < m {
                counter.change(text[index], false);
                counter.change(text[index + width], true);
            }
        }
    }
}

fn print_row(output: &mut String, values: &[usize]) {
    for (i, value) in values.iter().enumerate() {
        if i > 0 {
            output.push(' ');
        }
        write!(output, "{}", value).unwrap();
    }
    output.push('\n');
}

fn take<T: std::str::FromStr>(words: &mut std::str::SplitWhitespace<'_>) -> T {
    words.next().unwrap().parse().ok().unwrap()
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_whitespace();
    let n: usize = take(&mut words);
    let mut text: Vec<usize> = (0..n).map(|_| take(&mut words)).collect();
    let m: usize = take(&mut words);
    let mut pattern: Vec<usize> = (0..m).map(|_| take(&mut words)).collect();
    restore(&mut text, &mut pattern);
    let mut output = String::new();
    print_row(&mut output, &text);
    print_row(&mut output, &pattern);
    print!("{output}");
}
