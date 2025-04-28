package lab_3;

public class InOrderTest {
	public static void main(String[] args) {
		FunList consInst = new Cons(0)
				.append(new Cons(1))
				.append(new Cons(3));
		System.out.println(consInst.insertInOrder(2));

		FunList emptyInst = Empty.uniqueInstance().append(new Cons(3));
		System.out.println(emptyInst.insertInOrder(1));
	}
}
