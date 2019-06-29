package marofmar.javatutorials.methodd;

public class returnDemo {
	public static int one() {
		return 1;
		return 2;
		return 3;
	}
// not gonna even compile. "return" shuts down everything comes after.
	public static void main(String[] args) {
		System.out.println(one());

	}

}
