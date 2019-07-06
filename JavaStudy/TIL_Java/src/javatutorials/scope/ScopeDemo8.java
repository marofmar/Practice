package javatutorials.scope;

class C2 {
	int v = 10;
	
	void m() {
		int v = 20; 
		//System.out.println(v);
		System.out.println(this.v);
	}
}

public class ScopeDemo8 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		C2 c1 = new C2();
		c1.m();

	}

}
