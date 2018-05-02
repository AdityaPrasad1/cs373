// ---------------------
// SingletonPattern.java
// ---------------------

class Singleton {
    private static final Singleton _only = new Singleton();

    private Singleton ()
        {}

    public static Singleton only () {
        return _only;}

    public String f () {
        return "Singleton.f()";}}

class Singleton2 {
    private static Singleton2 _only;

    private Singleton2 ()
        {}

    public static Singleton2 only () {
        if (Singleton2._only == null)
            Singleton2._only = new Singleton2();
        return Singleton2._only;}

    public String f () {
        return "Singleton2.f()";}}

class Singleton3 {
    private Singleton3 ()
        {}

    private static class Holder {
        private static final Singleton3 _only = new Singleton3();}

    public static Singleton3 only () {
        return Holder._only;}

    public String f () {
        return "Singleton3.f()";}}

public final class SingletonPattern {
    public static void test () {
//      Singleton x = new Singleton();                    // error
    	assert(Singleton.only()     == Singleton.only());
    	assert(Singleton.only().f() == "Singleton.f()");}

    public static void main (String[] args) {
        System.out.println("SingletonPattern.java");
        test();
        System.out.println("Done.");}}
