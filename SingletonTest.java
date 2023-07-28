

public final class SingletonTest {

    private static SingletonTest instance;
    private String filename = null;
    
    private SingletonTest() {     
           
    }
    
    public static SingletonTest getInstance(String filename) {
        if(instance == null) {
            instance = new SingletonTest();
            instance.filename = filename;
        }
        
        return instance;
    }

    static void print(Object obj){
        System.out.println(obj);
    }

    public void printFilename(){
        print(filename);
    }

    // getters and setters
}



/*
 * 

# Compiling the Java file
javac -cp "jars/*:." SingletonTest.java

# Running the class
java -cp "jars/*:." SingletonTest.java


 */