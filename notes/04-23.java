// -----------
// Mon, 23 Apr
// -----------

abstract class A {
    abstract void f (int);}

class B extends A {
    void f (int) {...}};

class T {
    public static void main (...) {
        A x = new B;
        x.f(2);      // B.f

/*
three consequences to an abstract method
    1. must mark the class abstract
    2. children must define the method
    3. can't define the method in the parent
*/

class A {
    void f (int) {...}
    final void g (int) {...}
    abstract void h (int);}
