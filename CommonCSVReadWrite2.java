

/*
 * 
 *
 
Source:
    https://mvnrepository.com/artifact/org.apache.commons/commons-csv/1.8

    https://attacomsian.com/blog/read-write-csv-files-apache-commons-csv


 * 
 * 
 */

import java.io.IOException;
import java.io.Reader;
import java.nio.file.Files;
import java.nio.file.Paths;

import org.apache.commons.csv.CSVRecord;
import org.apache.commons.csv.CSVFormat;


public class CommonCSVReadWrite2 {

    static void print(Object obj){
        System.out.println(obj);
    }

    static void test(){
        try {
            // create a reader
            Reader reader = Files.newBufferedReader(Paths.get("users-with-header.csv"));
        
            // create csv bean reader
            CsvToBean csvToBean = new CsvToBeanBuilder(reader)
                    .withType(User.class)
                    .withIgnoreLeadingWhiteSpace(true)
                    .build();
        
            // iterate through users
            for (User user : (Iterable<User>) csvToBean) {
                System.out.println("ID: " + user.getId());
                System.out.println("Name: " + user.getName());
                System.out.println("Email: " + user.getEmail());
                System.out.println("Country: " + user.getCountryCode());
            }
        
            // close the reader
            reader.close();
        
        } catch (IOException ex) {
            ex.printStackTrace();
        }
    }
    
    public static void main(String[] args){
        test();
    }
}


/*
 * 

# Compiling the Java file


# Running the class
java -cp "jars/*:." CommonCSVReadWrite2.java


 */