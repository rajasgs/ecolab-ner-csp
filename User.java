/*
 * 
 *
 
Source:
    https://opencsv.sourceforge.net/apidocs/index.html?com/opencsv/bean/CsvBindByName.html


 * 
 * 
 */

import com.opencsv.bean.CsvBindByName;


public class User {

    @CsvBindByName
    public int id;

    @CsvBindByName
    public String name;
    
    @CsvBindByName
    public String email;
    
    @CsvBindByName(column = "country")
    public String countryCode;

    // getters and setters omitted for brevity
}