
fn main() {

    let mut num = 2520;

    loop {
        let mut success = true;
        for i in (11..21) {
            if num % i != 0 {
                success = false;
                break;
            }
        }

        if success {
            break;
        }

        num += 2520;
    }

    println!("{}", num);

}
