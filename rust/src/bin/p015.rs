
fn route_num(cube_size: usize) -> u64 {
    let mut l: Vec<u64> = vec![1; cube_size];
    for i in (0..cube_size) {
        for j in (0..i) {
            if j > 0 {
                l[j] = l[j] + l[j - 1];
            } else {
                l[j] = l[j] + 1;
            }
            // println!("j - {}", l[j]);
        }
        if i > 0 {
            l[i] = 2 * l[i - 1];
        } else {
            l[i] = 2;
        }
        // println!("i - {}", l[i]);
    }
    l[cube_size - 1]
}

fn main() {
    println!("{}", route_num(20));
}
