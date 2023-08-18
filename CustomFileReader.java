

/*
Created on 

@author: Raja CSP Raman

source:
    https://stackoverflow.com/questions/4677411/iterating-over-the-content-of-a-text-file-line-by-line-is-there-a-best-practic

    https://commons.apache.org/proper/commons-io/javadocs/api-release/org/apache/commons/io/LineIterator.html

    https://mvnrepository.com/artifact/org.apache.commons/commons-lang3/3.12.0
*/


import java.io.BufferedReader;
import java.io.FileReader;
import java.util.LinkedList;
import java.util.List;

public class CustomFileReader {

    private static final String fileName = "address.txt";

    static void print(Object obj){
        System.out.println(obj);
    }

    public static List<String> getContentsOfFile(String fileName){
        
        List<String> contents = new LinkedList<String>();

        try {
            BufferedReader br = new BufferedReader(new FileReader(fileName));

            for (String line = br.readLine(); line != null; line = br.readLine()) {
                // print(line);

                contents.add(line);
            }
        } catch (Exception e) {
            print("Error ");
            return null;
        }
        

        return contents;
    }
 
    public static void main(String[] args) throws Exception{
        List<String> contents = getContentsOfFile(fileName);

        print(contents);
    }
}
