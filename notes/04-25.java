// -----------
// Wed, 25 Apr
// -----------

class A1 {
    ...}

class T {
    public static void main (...) {
        A1 x = new A1();
        A1 y = new A1();
        s.o.p(x == y);   // false

        Class c1 = A1.class;
        Class c2 = A1.class;
        s.o.p(c1 == c2);     // true

        Class c3 = x.getClass();
        s.o.p(c1 == c3);     // true

        Class c4 = Class.forName("A1"); // ClassNotFoundException
        s.o.p(c1 == c4);     // true

        Object o = c4.newInstance();
            // InstantiationException (abstract class, interface, no default constr)
            // IllegalAccessException (private contr)

        A1 z = (A1) o; // ClassCastException


































class A1 {...}

class T {
    public static void main (...) {
        A1 x = new A1();
        A1 y = new A1();
        s.o.p(x == y);   // false

        Class c1 = A1.class;
        Class c2 = A1.class;
        s.o.p(c1 == c2);     // true

        Class c3 = x.getClass();
        s.o.p(c1 == c3)      // true

        Class c4 = Class.forName("A1"); // ClassNotFoundException
        s.o.p(c1 == c4);     // true

        Object o = c4.newInstance(); // IllegalAccessExcpetion (private constr)
                                     // InstantialException (abstract class, interface, no def constr)
        A1 z = (A1) o; // ClassCastException













































class A {...}

class T {
    public static void main (...) {
        A x = new A();
        A y = new A();
        s.o.p(x == y);

        Class c1 = A.class;
        Class c2 = A.class;
        s.o.p(c1 == c2);

        Class c3 = x.getClass();
        s.o.p(c1 == c3);

        Class c4 = Class.forName("A"); // ClassNotFoundException
        s.o.p(c1 == c4);

        Object o = c4.newInstance(); // InstantiationException (interface, abstract, no constr)
                                     // IllegalAccessException (private)

        A z = (A) o; // ClassCastException
