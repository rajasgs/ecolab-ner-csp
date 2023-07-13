

/*
 * 
 * 
 * 


https://jsoup.org/apidocs/org/jsoup/nodes/Element.html
 */

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.parser.Parser;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

public class XMLParserSoup {

    public static void main(String[] args) {
        String xml = "<item><HOUSE_NO>150</HOUSE_NO> <STREET_NAME>GLADSTONE AVE N</STREET_NAME></item>";

        Document doc = Jsoup.parse(xml, "", Parser.xmlParser());
        for (Element item : doc.select("item")) {
            Elements children = item.children();
            for (Element child : children) {
                System.out.println(child.tag() + " : " + child.text());
                // System.out.println(child.text());
            }
        }
    }
}