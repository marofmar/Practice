package marofmar.javatutorials.methodd;

public class returnDemo3 {
	public static String[] getMembers() {
		String[] members = {"Carol", "Bryson", "Yujin"};
		return members;
	}

	public static void main(String[] args) {
		String[] members = getMembers();
		System.out.println(getMembers()); //hmm why print result [Ljava.lang.String;@7852e922? 

	}

}
