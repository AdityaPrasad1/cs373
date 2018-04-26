// -----------
// Wed, 25 Apr
// -----------

class A {
    ...}

class T {
    public static void main (...) {
        A x = new A();
        A y = new A();
        s.o.p(x == y);                 // false

        Class c1 = A.class;
        Class c2 = A.class;
        s.o.p(c1 == c2);               // true

        Class c3 = x.getClass();
        s.o.p(c1 == c3);               // true

        Class c4 = Class.forName("A"); // ClassNotFoundException
        s.o.p(c1 == c4);               // true

        Object o = c4.newInstance();   // InstantiationException (abstract class, interface, no default constr)
                                       // IllegalAccessException (private contr)

        A z = (A) o; // ClassCastException
