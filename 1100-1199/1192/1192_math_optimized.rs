#![no_main]

const INPUT_FIELDS: i32 = 2;

#[cfg_attr(windows, link(name = "msvcrt"))]
extern "C" {
    fn scanf(format: *const std::ffi::c_char, ...) -> i32;
    fn getchar() -> i32;
    fn printf(format: *const std::ffi::c_char, ...) -> i32;
}

const PI: f64 = 3.1415926535;
const HALF_TURN: f64 = 180.0;
const GRAVITY: f64 = 10.0;

fn retention_delta(token: &mut [u8]) -> Option<f64> {
    let exponent_start = token
        .iter()
        .position(|&byte| byte == b'e' || byte == b'E')
        .unwrap_or(token.len());
    let exponent = if exponent_start == token.len() {
        0
    } else {
        let text = std::str::from_utf8(&token[exponent_start + 1..]).ok()?;
        text.parse::<i64>().unwrap_or_else(|_| {
            if text.starts_with('-') {
                i64::MIN
            } else {
                i64::MAX
            }
        })
    };
    let coefficient = &token[..exponent_start];
    let first = coefficient
        .iter()
        .position(|byte| byte.is_ascii_digit() && *byte != b'0')?;
    let integer_digits = coefficient
        .iter()
        .take_while(|&&byte| byte != b'.')
        .filter(|byte| byte.is_ascii_digit())
        .count();
    let leading_zeros = coefficient[..first]
        .iter()
        .filter(|byte| byte.is_ascii_digit())
        .count();
    let leading_power = (integer_digits as i64)
        .saturating_sub(leading_zeros as i64)
        .saturating_sub(1)
        .saturating_add(exponent);
    if leading_power == 0 && token[first] == b'1' {
        // For 1 <= K < 2, subtract the units digit before rounding to f64.
        // This also works for scientific notation and a long fractional tail.
        token[first] = b'0';
        std::str::from_utf8(token).ok()?.parse::<f64>().ok()
    } else {
        Some(std::str::from_utf8(token).ok()?.parse::<f64>().ok()? - 1.0)
    }
}

#[no_mangle]
pub extern "C" fn main() -> i32 {
    let (mut speed, mut angle) = (0.0f64, 0.0f64);
    // SAFETY: the two %lf fields receive live pointers to f64 variables.
    let fields = unsafe {
        scanf(
            b"%lf %lf\0".as_ptr().cast(),
            &mut speed as *mut f64,
            &mut angle as *mut f64,
        )
    };
    if fields != INPUT_FIELDS {
        return 1;
    }
    let mut token = Vec::new();
    loop {
        // SAFETY: getchar takes no pointers and returns one byte or EOF.
        let byte = unsafe { getchar() };
        if byte < 0 || (byte as u8).is_ascii_whitespace() {
            if !token.is_empty() || byte < 0 {
                break;
            }
        } else {
            token.push(byte as u8);
        }
    }
    let retention = match std::str::from_utf8(&token)
        .ok()
        .and_then(|text| text.parse::<f64>().ok())
    {
        Some(value) => value,
        None => return 1,
    };
    let flight = speed * speed * (2.0 * angle * PI / HALF_TURN).sin() / GRAVITY;
    let distance = if speed == 0.0 || angle == 0.0 {
        0.0
    } else if retention == 1.0 {
        // A positive decimal loss can disappear when K itself is rounded.
        let delta = match retention_delta(&mut token) {
            Some(value) => value,
            None => return 1,
        };
        flight + flight / delta
    } else if retention.is_infinite() {
        flight
    } else if retention <= f64::MAX / flight {
        // Keep the ordinary f64 expression and its existing judge rounding.
        flight * retention / (retention - 1.0)
    } else {
        // Avoid an overflowing numerator when the final ratio is near one.
        flight * (retention / (retention - 1.0))
    };
    // SAFETY: the static format expects the promoted double supplied here.
    unsafe {
        printf(b"%.2f\n\0".as_ptr().cast(), distance);
    }
    0
}
