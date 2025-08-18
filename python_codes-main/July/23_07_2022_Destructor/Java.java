
class Main{

	int x = 10;
	String y = "Harshal";

	Main(int p, String q){
	
		this.x = p;
		this.y = q;
	}

	public static void main(String[] args){
	
		Main obj = new Main(20,"Prajwal");
		System.out.println(obj.x);
		System.out.println(obj.y);
	}
}
