// ---------------
// Reflection.java
// ---------------

interface I
    {}

interface J extends I
    {}

abstract class A implements I
    {}

class B
    {}

class C implements I {
    public C (int i)
        {}}

class D implements I {
    private D ()
        {}}

class E implements I
    {}

final class Reflection {
    public static void test1 () {
        try {
            I x = (I) Class.forName("J").newInstance();
            assert false;}
        catch (ClassCastException e) {
            assert false;}
        catch (ClassNotFoundException e) {
            assert false;}
        catch (IllegalAccessException e) {
            assert false;}
        catch (InstantiationException e) {
            assert e.toString().equals("java.lang.InstantiationException: J");}}

    public static void test2 () {
        try {
            I x = (I) Class.forName("A").newInstance();
            assert false;}
        catch (ClassCastException e) {
            assert false;}
        catch (ClassNotFoundException e) {
            assert false;}
        catch (IllegalAccessException e) {
            assert false;}
        catch (InstantiationException e) {
            assert e.toString().equals("java.lang.InstantiationException");}}

    public static void test3 () {
        try {
            I x = (I) Class.forName("B").newInstance();
            assert false;}
        catch (ClassCastException e) {
            assert e.toString().equals("java.lang.ClassCastException: B cannot be cast to I");}
        catch (ClassNotFoundException e) {
            assert false;}
        catch (IllegalAccessException e) {
            assert false;}
        catch (InstantiationException e) {
            assert false;}}

    public static void test4 () {
        try {
            I x = (I) Class.forName("C").newInstance();
            assert false;}
        catch (ClassCastException e) {
            assert false;}
        catch (ClassNotFoundException e) {
            assert false;}
        catch (IllegalAccessException e) {
            assert false;}
        catch (InstantiationException e) {
            assert e.toString().equals("java.lang.InstantiationException: C");}}

    public static void test5 () {
       try {
            I x = (I) Class.forName("D").newInstance();
            assert false;}
        catch (ClassCastException e) {
            assert false;}
        catch (ClassNotFoundException e) {
            assert false;}
        catch (IllegalAccessException e) {
            assert e.toString().equals("java.lang.IllegalAccessException: class Reflection cannot access a member of class D with modifiers \"private\"");}
        catch (InstantiationException e) {
            assert false;}}

    public static void test6 () {
        try {
            I x = (I) Class.forName("E").newInstance();
            assert x.getClass() == E.class;}
        catch (ClassCastException e) {
            assert false;}
        catch (ClassNotFoundException e) {
            assert false;}
        catch (IllegalAccessException e) {
            assert false;}
        catch (InstantiationException e) {
            assert false;}}

    public static void test7 () {
        try {
            Object x = Class.forName("F").newInstance();
            assert false;}
        catch (ClassCastException e) {
            assert false;}
        catch (ClassNotFoundException e) {
            assert e.toString().equals("java.lang.ClassNotFoundException: F");}
        catch (IllegalAccessException e) {
            assert false;}
        catch (InstantiationException e) {
            assert false;}}

    public static void main (String[] args) {
        System.out.println("Reflection.java");
        test1();
        test2();
        test3();
        test4();
        test5();
        test6();
        test7();
        System.out.println("Done.");}}
