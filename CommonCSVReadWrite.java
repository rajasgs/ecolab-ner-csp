

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

public class CommonCSVReadWrite {

    static void print(Object obj){
        System.out.println(obj);
    }

    static void test(){
        try {
            // create a reader
            Reader reader = Files.newBufferedReader(Paths.get("users.csv"));

            // read csv file
            Iterable<CSVRecord> records = CSVFormat.DEFAULT.parse(reader);
            for (CSVRecord record : records) {
                print("Record #: " + record.getRecordNumber());
                print("ID: " + record.get(0));
                print("Name: " + record.get(1));
                print("Email: " + record.get(2));
                print("Country: " + record.get(3));

                print("");
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
java -cp "jars/*:." CommonCSVReadWrite.java


 */