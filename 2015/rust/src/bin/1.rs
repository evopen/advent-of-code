use std::os::unix::prelude::OsStrExt;

fn main() {
    let args = std::env::args_os();
    let input = unsafe { args.skip(1).next().unwrap_unchecked() };
    let mut floors = 0;
    for c in input.as_bytes() {
        match c {
            b'(' => floors += 1,
            b')' => floors -= 1,
            _ => panic!("Invalid input"),
        }
    }
    println!("Santa is on floor {}", floors);
}
