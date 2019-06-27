package marofmar.javatutorials.methodd;

public class methodDemo4 {
	public static String numbering(int init, int limit) {
		int i = init;
		String output = "";
		while (i < limit) {
			output += i;
			i ++;
		}
		// not return!
		return output;
	}
	

	public static void main(String[] args) {
		String result = numbering(1, 5);
		System.out.println(result);

	}

}
