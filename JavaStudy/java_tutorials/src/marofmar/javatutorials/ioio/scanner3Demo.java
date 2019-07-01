package marofmar.javatutorials.ioio;

import java.util.Scanner; 
import java.io.*; 

public class scanner3Demo {

	public static void main(String[] args) {
		try {
			File file = new File("out.rtf");
			Scanner sc = new Scanner(file);
			while(sc.hasNextInt()) {
				System.out.println(sc.nextInt()*1000);
			}
			sc.close();
		} catch(FileNotFoundException e) {
			e.printStackTrace(); 
		}

	}

}
