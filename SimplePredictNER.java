// package ner_work;

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

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.parser.Parser;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

public class SimplePredictNER {

    static String STREET_NAME           = "STREET_NAME";
    static String HOUSE_NO              = "HOUSE_NO";
    static String SUITE_NO              = "SUITE_NO";

    private CRFClassifier getModel(String modelPath) {
        /*
         * This returns a classifier model
         */
        return CRFClassifier.getClassifierNoExceptions(modelPath);
    }

    @Deprecated
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

    static HashMap<String, String> string2XMLDocument(String content){

        /*
         * 
         * 
         * 
         */

        // print("content: "+content);

        String xml = "<item>" + content+"</item>";

        HashMap<String, String> resultMap = new HashMap<String, String>();

        Document doc = Jsoup.parse(xml, "", Parser.xmlParser());
        for (Element item : doc.select("item")) {
            Elements children = item.children();
            for (Element child : children) {
                // System.out.println(child.tag() + " : " + child.text());
                // System.out.println(child.text());

                String cTag     = ""+child.tag();
                String cValue   = child.text();

                if(resultMap.containsKey(cTag)){
                    cValue = "" + resultMap.get(cTag) + " " + cValue;
                    resultMap.put(cTag, cValue);
                } else{
                    resultMap.put(cTag, cValue);
                }
            }
        }

        return resultMap;
    }

    public static HashMap<String, String> getEntities(CRFClassifier model, String input){

        /*
         * 
         * 
         * 
         */
        
        input = input.trim();
        // System.out.println(input+" ==> "+model.classifyToString(input));
        String result = model.classifyToString(input);

        // <HOUSE_NO>1626</HOUSE_NO><STREET_NAME>-1630 NESS AVE</STREET_NAME>

        List<String> resultParts = Arrays.asList(result.split(" "));
        // print(resultParts);

        HashMap<String, String> resultMap = new HashMap<String, String>();

        resultMap.put(STREET_NAME, "");
        resultMap.put(HOUSE_NO, "");
        resultMap.put(SUITE_NO, "");

        // resultMap.put(SUITE_AND_HOUSE_NO, "");
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

        // print("");

        return resultMap;
    }

    public HashMap<String, String> getEntities2(CRFClassifier model, String input){

        /*
         * 
         * 
         * 
         */
        
        String xmlContent = model.classifyWithInlineXML(input);

        // print(xmlContent);

        HashMap<String, String> resultMap = string2XMLDocument(xmlContent);

        return resultMap;
    }

    static void printMap(HashMap<String, String> map){

        /*
         * 
         * 
         * 
         */


        for (Map.Entry<String, String> entry : map.entrySet()) {
            String key = entry.getKey();
            Object value = entry.getValue();
            
            if(value.toString().trim().length() == 0){
                continue;
            }

            print(key + " : " + value);
        }
    }

    // static String MODEL_PATH            = "Ecolab_address_ner_model_Ver1.model.ser.gz";

    public String getTokens(String content){

        /*
         * 
         * 
         * 
         */

        // String content = String.join(" ", args);

        // doTagging(model, content);
        HashMap<String, String> result = getEntities2(model, content);
        // print(result);
        // printMap(result);

        StringBuffer sb = new StringBuffer("");

        sb.append("STREET_NAME="+result.get(STREET_NAME));
        sb.append("\nHOUSE_NO="+result.get(HOUSE_NO));
        sb.append("\nSUITE_NO="+result.get(SUITE_NO));

        return sb.toString();
    }

    private static SimplePredictNER instance;

    private String modelFilename = null;
    private CRFClassifier model = null;

    public static SimplePredictNER getInstance(String modelFilename) {

        /*
         * 
         * 
         * 
         */

        if(instance != null)
            return instance
            
        instance                    = new SimplePredictNER();
        instance.modelFilename      = modelFilename;
        instance.model              = instance.getModel(instance.modelFilename);

        print("Getting singleton instance");
        
        return instance;
    }

    public static void main(String[] args){

        // String content = "55/57 BAHNHOFSTRASSE";

        // String content = String.join(" ", args);

        // SimplePredictNER singletonInstance = SimplePredictNER.getInstance(args[0]);

        // // doTagging(model, content);
        // HashMap<String, String> result = singletonInstance.getEntities2(singletonInstance.model, content);
        // // print(result);
        // printMap(result);

        // print("STREET_NAME="+result.get(STREET_NAME));
        // print("HOUSE_NO="+result.get(HOUSE_NO));
        // print("SUITE_NO="+result.get(SUITE_NO));
        

        // string2XMLDocument("<HOUSE_NO>150</HOUSE_NO> <STREET_NAME>GLADSTONE AVE N</STREET_NAME>");

    }
}



/*
 * 

# Compiling the Java file
javac -cp "jars/*:." SimplePredictNER.java

# Running the class
java -cp "jars/*:." SimplePredictNER.java Ecolab_address_ner_model_Ver1.model.ser.gz


 */