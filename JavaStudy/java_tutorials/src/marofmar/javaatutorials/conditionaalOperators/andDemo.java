package marofmar.javaatutorials.conditionaalOperators;

public class andDemo {

	public static void main(String[] args) {
		if (true&&true) {
			System.out.println(1);
		}
		if (true &&false) {
			System.out.println(2);
		}
		
		if (false && false) {
			System.out.println(3);
		}
		
		String id = args[0];
		String password = args[1];
		if (id.equals("Hello") && password.equals("World!")) {
			System.out.println("right");
		} else {
			System.out.println("wrong");
		}
		
	}

}
