use std::io::{self, BufRead, BufWriter, Write};

const MAX_SALARY: i32 = 1_000_000_000;

#[derive(Clone)]
struct Employee {
    parent: i32,
    offset: i32,
    low: i32,
    high: i32,
}

fn find(staff: &mut [Employee], vertex: usize) -> usize {
    let parent = staff[vertex].parent;
    if parent < 0 {
        return vertex;
    }
    let parent = parent as usize;
    let root = find(staff, parent);
    staff[vertex].offset += staff[parent].offset;
    staff[vertex].parent = root as i32;
    root
}

fn apply(staff: &mut [Employee], first: usize, second: usize, difference: i32) -> bool {
    let mut left = find(staff, first);
    let mut right = find(staff, second);
    let mut shift = staff[first].offset - staff[second].offset - difference;
    if left == right {
        return shift == 0;
    }

    // A root stores the negative component size, so the larger root stays in place.
    if staff[left].parent > staff[right].parent {
        std::mem::swap(&mut left, &mut right);
        shift = -shift;
    }
    // Translate the child's allowed range into the root's coordinates.
    staff[left].low = staff[left].low.max(staff[right].low - shift);
    staff[left].high = staff[left].high.min(staff[right].high - shift);
    if staff[left].low > staff[left].high {
        return false;
    }
    staff[left].parent += staff[right].parent;
    staff[right].parent = left as i32;
    staff[right].offset = shift;
    true
}

fn main() {
    let stdin = io::stdin();
    let mut input = stdin.lock();
    let mut line = String::new();
    input.read_line(&mut line).unwrap();
    let mut header = line
        .split_ascii_whitespace()
        .map(|token| token.parse::<usize>().unwrap());
    let people = header.next().unwrap();
    let statements = header.next().unwrap();
    let mut staff = vec![
        Employee {
            parent: -1,
            offset: 0,
            low: 0,
            high: MAX_SALARY
        };
        people
    ];
    staff[0].high = 0;
    let mut output = BufWriter::new(io::stdout().lock());
    for index in 0..statements {
        line.clear();
        input.read_line(&mut line).unwrap();
        let mut fields = line.split_ascii_whitespace();
        let first = fields.next().unwrap().parse().unwrap();
        let second = fields.next().unwrap().parse().unwrap();
        let difference = fields.next().unwrap().parse().unwrap();
        if !apply(&mut staff, first, second, difference) {
            writeln!(output, "Impossible after {} statements", index + 1).unwrap();
            return;
        }
    }
    writeln!(output, "Possible").unwrap();
    for employee in 0..people {
        let root = find(&mut staff, employee);
        writeln!(output, "{}", staff[root].low + staff[employee].offset).unwrap();
    }
}
