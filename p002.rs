
fn main() {

    let mut nums = vec![1, 2];

    loop {
        let v = nums[nums.len() - 2] + nums[nums.len() - 1];

        if v < 4000000 {
            nums.push(v);
        } else {
            break;
        }
    }

    println!("{}", nums.into_iter().filter(|&n| n % 2 == 0).fold(0, |sum, x| sum + x));

}
