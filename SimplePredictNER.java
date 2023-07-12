package ner_work;

/*
 * 
 *
 
Source:
    https://attacomsian.com/blog/java-read-parse-csv-file


 * 
 * 
 */


import java.util.Properties;
import edu.stanford.nlp.ie.crf.CRFClassifier;
import edu.stanford.nlp.ling.CoreLabel;
import edu.stanford.nlp.sequences.SeqClassifierFlags;
import edu.stanford.nlp.util.StringUtils;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.sql.Timestamp;
import java.util.Arrays;
import java.util.Calendar;
import java.util.HashMap;
import java.util.Map;
import java.util.LinkedList;
import java.util.List;
import java.io.FileWriter;

public class PredictNER {

    static String MODEL_PATH        = "ecolab_address_ner_model_csp.model.ser.gz";

    static String STREET_NAME       = "STREET_NAME";
    static String HOUSE_NO          = "HOUSE_NO";
    static String SUITE_NO          = "SUITE_NO";

    public static CRFClassifier getModel(String modelPath) {
        return CRFClassifier.getClassifierNoExceptions(modelPath);
    }

    public static void doTagging(CRFClassifier model, String input){
        input = input.trim();
        // System.out.println(input+" ==> "+model.classifyToString(input));
        String result = model.classifyToString(input);

        // print(model.classify(input));

        print(result);
    }

    static void print(Object obj){
        System.out.println(obj);
    }



    public static HashMap<String, String> getEntities(CRFClassifier model, String input){
        input = input.trim();
        // System.out.println(input+" ==> "+model.classifyToString(input));
        String result = model.classifyToString(input);

        List<String> resultParts = Arrays.asList(result.split(" "));
        // print(resultParts);

        HashMap<String, String> resultMap = new HashMap<String, String>();


        resultMap.put(STREET_NAME, "");
        resultMap.put(HOUSE_NO, "");
        for (String object: resultParts) {

            // print("part : " + object);

            List<String> KeyValueParts = Arrays.asList(object.split("/"));

            String value = KeyValueParts.get(0);
            String key   = KeyValueParts.get(1);

            // print(key);

            if(key.equalsIgnoreCase(STREET_NAME)){
                String prevValue = resultMap.get(STREET_NAME);

                String newValue = prevValue + " " + value; 
                resultMap.put(STREET_NAME, newValue);

                // print(resultMap);
            } else if (key.equalsIgnoreCase(HOUSE_NO)){

                String prevValue = resultMap.get(HOUSE_NO);

                String newValue = prevValue + " " + value; 
                resultMap.put(HOUSE_NO, newValue);

            } else if (key.equalsIgnoreCase(SUITE_NO)){

                String prevValue = resultMap.get(SUITE_NO);

                String newValue = prevValue + " " + value; 
                resultMap.put(SUITE_NO, newValue);

            }
            
        }

        resultMap.put(STREET_NAME, (resultMap.getOrDefault(STREET_NAME, "")).trim());
        resultMap.put(HOUSE_NO, (resultMap.getOrDefault(HOUSE_NO, "")).trim());
        resultMap.put(SUITE_NO, (resultMap.getOrDefault(SUITE_NO, "")).trim());

        print("");

        return resultMap;
    }


    static void printMap(HashMap<String, String> map){
        for (Map.Entry<String, String> entry : map.entrySet()) {
            String key = entry.getKey();
            Object value = entry.getValue();
            
            if(value.toString().trim().length() == 0){
                continue;
            }

            print(key + " : " + value);
        }
    }

    // static 

    public static void main(String[] args){

        CRFClassifier model = getModel(MODEL_PATH);

        String content = "22 DRUMCONDRA ROAD UPPER";

        // doTagging(model, content);
        HashMap<String, String> result = getEntities(model, content);
        // print(result);
        printMap(result);

    }
}



/*
 * 

# Compiling the Java file
javac -cp "/home/ashish/corenlp/stanford-corenlp-4.5.2/*" PredictNER.java

# Running the class
java -cp "jars/*:." SimplePredictNER.java


 */