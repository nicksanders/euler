
fn main() {

    let s = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8];
    let d = [0, 3, 6, 6, 5, 5, 5, 7, 6, 6];
    let h = 7;
    let t = 8;

    let mut total = 0;

    for i in (1..1000) {
        let c: usize = i % 10; // singles digit
        let b: usize = ((i % 100) - c) / 10; // tens digit
        let a: usize = ((i % 100) - (b * 10) - c) / 10; // hundreds digit

        if a != 0 {
            total += s[a] + h;
            if b != 0 || c != 0 {
                total += 3; // and
            }
        }

        if b == 0 || b == 1 {
            total += s[b * 10 + c];
        } else {
            total += d[b] + s[c];
        }

    }

    total += s[1] + t; // one thousand

    println!("{}", total);

}
