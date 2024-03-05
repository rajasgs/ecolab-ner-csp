public class ClassA {
    
    static void print(Object obj){
        System.out.println(obj);
    }

    public void hello(){
        print("Inside Hello non-static method");
    }

    static void helloStatic(){
        print("Inside Hello static method");
    }
}

/*
 * 

# Compiling the Java file
javac -cp "jars/*:." ClassA.java

# Running the class
java ClassA


 */