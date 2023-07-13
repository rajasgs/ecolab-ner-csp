import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;
import javax.xml.parsers.SAXParser;
import javax.xml.parsers.SAXParserFactory;

import org.xml.sax.helpers.DefaultHandler;

import java.io.ByteArrayInputStream;
import java.io.File;
import java.io.IOException;

/***
 * 
 * 
 *
 * 

 https://stackoverflow.com/questions/15947051/convert-a-string-to-a-xml-element-java
 
 */

import java.io.StringReader;
import org.xml.sax.InputSource;
import org.xml.sax.SAXException;
import org.w3c.dom.Document;

public class XMLParser {

    static void print(Object obj){
        System.out.println(obj);
    }

    public static void parse2() throws Exception {
        DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
        factory.setValidating(true);
        factory.setIgnoringElementContentWhitespace(true);
        DocumentBuilder builder = factory.newDocumentBuilder();
        File file = new File("test.xml");
        Document doc = builder.parse(file);
        // Do something with the document here.

        print(doc);
    }

    // static void parse(){

    //     String content = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><message><warning>Hello World</warning></message>";

    //     try {
    //         SAXParserFactory factory = SAXParserFactory.newInstance();
    //         SAXParser saxParser = factory.newSAXParser();
    //         DefaultHandler handler = new DefaultHandler();
    //         String result = saxParser.parse(new InputSource(new StringReader(content)), handler); 
    //     } catch(Exception  saxe){
    //         print("Error while parsing ");
    //         saxe.printStackTrace();
    //     }
    // }
    
    public static void main(String[] args) throws Exception {
        parse2();
    }
}
