#![no_main]

const LIMB_DIGITS: usize = 9;

#[cfg_attr(windows, link(name = "msvcrt"))]
extern "C" {
    fn getchar() -> i32;
    fn putchar(character: i32) -> i32;
}

fn read_byte() -> i32 {
    // SAFETY: getchar has no pointer arguments and reads the standard stream.
    unsafe { getchar() }
}

fn write_byte(byte: u8) {
    // SAFETY: putchar accepts a byte promoted to int and has no pointers.
    unsafe {
        putchar(i32::from(byte));
    }
}

fn write_number(value: i64) {
    const DIGITS: usize = 20;
    let mut remaining = value.unsigned_abs();
    if value < 0 {
        write_byte(b'-');
    }
    let mut buffer = [0u8; DIGITS];
    let mut start = buffer.len();
    loop {
        start -= 1;
        buffer[start] = b'0' + (remaining % 10) as u8;
        remaining /= 10;
        if remaining == 0 {
            break;
        }
    }
    for &digit in &buffer[start..] {
        write_byte(digit);
    }
}

const BASE: u64 = 1_000_000_000;
type Big = Vec<u32>;

fn trim(value: &mut Big) {
    while value.len() > 1 && value.last() == Some(&0) {
        value.pop();
    }
}

fn multiply(a: &[u32], b: &[u32]) -> Big {
    let mut result = vec![0; a.len() + b.len()];
    for (i, &left) in a.iter().enumerate() {
        let mut carry = 0;
        for (j, &right) in b.iter().enumerate() {
            // (BASE-1)^2 plus both carries fits exactly in u64.
            let value = u64::from(result[i + j]) + carry + u64::from(left) * u64::from(right);
            result[i + j] = (value % BASE) as u32;
            carry = value / BASE;
        }
        let mut at = i + b.len();
        while carry != 0 {
            let value = u64::from(result[at]) + carry;
            result[at] = (value % BASE) as u32;
            carry = value / BASE;
            at += 1;
        }
    }
    trim(&mut result);
    result
}

fn small_product(a: &[u32], factor: u32) -> Big {
    let mut result = Vec::with_capacity(a.len() + 1);
    let mut carry = 0;
    for &limb in a {
        let value = u64::from(limb) * u64::from(factor) + carry;
        result.push((value % BASE) as u32);
        carry = value / BASE;
    }
    if carry != 0 {
        result.push(carry as u32);
    }
    trim(&mut result);
    result
}

fn add(a: &[u32], b: &[u32]) -> Big {
    let mut result = Vec::with_capacity(a.len().max(b.len()) + 1);
    let mut carry = 0;
    for i in 0..a.len().max(b.len()) {
        let value = carry + u64::from(*a.get(i).unwrap_or(&0)) + u64::from(*b.get(i).unwrap_or(&0));
        result.push((value % BASE) as u32);
        carry = value / BASE;
    }
    if carry != 0 {
        result.push(carry as u32);
    }
    result
}

fn power_shift(a: &[u32], digits: usize) -> Big {
    if a.len() == 1 && a[0] == 0 {
        return vec![0];
    }
    let factor = 10u32.pow((digits % LIMB_DIGITS) as u32);
    let value = small_product(a, factor);
    if digits < LIMB_DIGITS {
        return value;
    }
    let mut result = vec![0; digits / LIMB_DIGITS];
    result.extend_from_slice(&value);
    result
}

fn at_least(a: &[u32], b: &[u32]) -> bool {
    if a.len() != b.len() {
        return a.len() > b.len();
    }
    for (&left, &right) in a.iter().rev().zip(b.iter().rev()) {
        if left != right {
            return left > right;
        }
    }
    true
}

fn decimal() -> (Big, usize) {
    let mut byte = read_byte();
    while byte >= 0 && byte <= b' ' as i32 {
        byte = read_byte();
    }
    if byte == b'+' as i32 {
        byte = read_byte();
    }
    let mut digits = Vec::new();
    let (mut fraction, mut places) = (false, 0i64);
    while byte > b' ' as i32 && byte != b'e' as i32 && byte != b'E' as i32 {
        if byte == b'.' as i32 {
            fraction = true;
        } else {
            digits.push((byte - b'0' as i32) as u8);
            if fraction {
                places += 1;
            }
        }
        byte = read_byte();
    }
    if byte == b'e' as i32 || byte == b'E' as i32 {
        byte = read_byte();
        let negative = byte == b'-' as i32;
        if negative || byte == b'+' as i32 {
            byte = read_byte();
        }
        let mut exponent = 0;
        while (b'0' as i32..=b'9' as i32).contains(&byte) {
            exponent = exponent * 10 + i64::from(byte - b'0' as i32);
            byte = read_byte();
        }
        places -= if negative { -exponent } else { exponent };
    }
    let (mut first, mut end) = (0, digits.len());
    while first + 1 < end && digits[first] == 0 {
        first += 1;
    }
    // Remove zero padding before allocating arbitrary-precision limbs.
    while end > first + 1 && digits[end - 1] == 0 {
        end -= 1;
        places -= 1;
    }
    let mut value = Vec::with_capacity((end - first + LIMB_DIGITS - 1) / LIMB_DIGITS);
    while end > first {
        let start = end - (end - first).min(LIMB_DIGITS);
        let mut limb = 0;
        for &digit in &digits[start..end] {
            limb = limb * 10 + u32::from(digit);
        }
        value.push(limb);
        end = start;
    }
    trim(&mut value);
    if places < 0 {
        value = power_shift(&value, (-places) as usize);
        places = 0;
    }
    (value, places as usize)
}

fn payout() -> i64 {
    const TOTAL: u32 = 1000;
    const OUTCOMES: u32 = 3;
    const MAXIMUM_ODD: u32 = 100;
    let (mut numerator, mut denominator) = (vec![1], vec![0]);
    for _ in 0..OUTCOMES {
        let (value, scale) = decimal();
        denominator = add(
            &multiply(&denominator, &value),
            &power_shift(&numerator, scale),
        );
        numerator = multiply(&numerator, &value);
    }
    let twice = small_product(&numerator, 2 * TOTAL);
    let (mut low, mut high) = (0, TOTAL * MAXIMUM_ODD / OUTCOMES + 1);
    while low + 1 < high {
        let middle = (low + high) / 2;
        // Compare P with middle-1/2 exactly: ties round upward.
        if at_least(&twice, &small_product(&denominator, 2 * middle - 1)) {
            low = middle;
        } else {
            high = middle;
        }
    }
    i64::from(low)
}

#[no_mangle]
pub extern "C" fn main() -> i32 {
    write_number(payout());
    write_byte(b'\n');
    0
}
