import java.util.Properties;
import edu.stanford.nlp.ie.crf.CRFClassifier;
import edu.stanford.nlp.ling.CoreLabel;
import edu.stanford.nlp.sequences.SeqClassifierFlags;
import edu.stanford.nlp.util.StringUtils;

import java.sql.Timestamp;
import java.util.Calendar;

public class PredictNER1 {

    public static CRFClassifier getModel(String modelPath) {
        return CRFClassifier.getClassifierNoExceptions(modelPath);
    }

    public static void doTagging(CRFClassifier model, String input){
        input = input.trim();
        System.out.println(input+" ==> "+model.classifyToString(input));
        model.classifyToString(input);
    }

    public static void main(String[] args){

        CRFClassifier model = getModel("/home/ashish6-singhal/Documents/NER/ecolab_address_ner_model.model.ser.gz");

        //String[] tests = new String[]{"552 The Holloway Street Rd", "1 CALLE SAN GERONIMO","22503 State Highway 249","142 Co-Op Way","NO. 1 JALAN SITAR 33/6","MARSHFIELD BANK","Ulica Stanisława Wyspiańskiego 14","8 ZAMKOWA","6800 Abercorn St","3100 OLENTANGY RIVER RD","594 ALBANY AVE","1B Marchfield Park","2360 E PERSHING BLVD","TERRACE ROAD","320 INGERSOLL AVE","1350 HOLIDAY LN","802 BRANDI LN","361000","100102","21 MICKIEWICZA","Plac Słowiański 17","204 DEARBORN CT STE 103","272000","Passower Chaussee 111","101302","202A LEA","202A LEA","202A UL. J. LEA","311100","10744 GOLD CENTER DR","1916 State Route 65","4500 S DOBSON RD","1001 GREAT SOUTHWEST PKWY SW","Golf Course","Bachstr. 4","6050 GORGAS RD","6050 GORGAS RD BUILDING 2302","Brook Bldg","39","101 LAFAYETTE ST","3920 DUTCHMANS LN","1021 W BROAD ST","ST. MARYS STREET","501 Main St","Im Emscherbruch 11","1108 Chestnut St","2601 WEST WINDSOR DR","1910 WELLS RD","1910 WELLS RD SPC VC-04","2518 ALLEN BLVD","1615 PLEASANT HILL RD","8 MEKSYKAŃSKA","72 POPLAR ST","314118","100 HIGHWAY 332 W STE 143","LONDON WALL","314118","404 S FIGUEROA ST","150000","405 ALPHA BLVD","Ulica Janikowska 33","MILL LANE","Szyb Gg 1 59-150","Ashgrove Road W","2801 Smith Ave","5308 LIBERTY AVE","314118","UL. MARIANA BUBLEWICZA 4 BRAMA NR 7","794 LUCKY EAGLE DR","3636 N RIDGE RD","UL. DŁUGI TARG 35/38","BELLFIELD AVENUE","19801 OBSERVATION DR","314118","37/45 KRAKOWSKA","611 E MARCEAU ST","111 N Wells Rd","314118","45 TUSZEWSKA","OLD SHIRE LANE","OLD SHIRE LANE","Ulica Stanisławowska 38/44","42B UL. PUŁAWSKA","100 Rue Charlemagne Dr","6063 AVE ISLA VERDE","200000","210000","15 DUNLOP RD","215337","4277 W 150TH ST","100000","4 LINDEGO","517 Beulah Ave","28 SZPITALNA","2 AL. KASZTANOWA","Ulica Willowa 4","Aleja Powstańców Wielkopolskich 72","5 HILLMANS WAY","5 HILLMANS WAY","5 HILLMANS WAY HILLMANS WAY","BRYANSTON STREET","BRYANSTON STREET","517002","D2 BUSINESS PARK","HOLDEN ROAD","313000","7 MORCINKA","301 S HILLS VLG","FOXBRIDGE WAY","1714 S Euclid Ave","Manchester Airport Manchester Airport . .Manchester Church","Ulica Strefowa 2 43-100","425 8TH ST","1200 NADEAU RD","Ulica Poznańska 109","396 S Drummond St","Ulica Łowicka 27/1","750 KEARNY ST","Pikesville Carrier A","Ste 2","Ulica Jana Ewangelisty Purkyniego 10","UL. 28 CZERWCA 1956 R. 194/202","UL. 28 CZERWCA 1956 R. 194/202","201 W LAYTON PKWY","BUILDING 34","Ulica Ignacego Daszyńskiego 1","29 UL. BOLESŁAWA PRUSA","6067 Wilshire Blvd","168 ROBINSON ROAD","96 AL. ZWYCIĘSTWA","1500 MEDICAL AVE","1 AMERICAN LN","AVENIDA BEIRUTE, 870","115 Proctor Ave","25 Cove Rd","BOUNDARY ROAD","Ulica Gwardii Ludowej 23","204 DEARBORN CT STE 103","Ulica Grunwaldzka 37K","100 Campus Ctr","Ulica Przemysłowa 47 43-100","87 AL. PIŁSUDSKIEGO","MARSHFIELD BANK","2636 Wilson Blvd","BRENT CROSS SHOPPING CENTRE","BRENT CROSS SHOPPING CENTRE","BRENT CROSS SHOPPING CENTRE","BRENT CROSS SHOPPING CENTRE","Ulica Jagiellońska 72","314118","1A MARSH CLOSE","Ulica Przemysłowa 47 43-100","47A MALCZEWSKIEGO","47A MALCZEWSKIEGO","50A DOMANIEWSKA","12C POLECZKI","300 5TH AVE","300 5TH AVE","Ulica Augustyna Szamarzewskiego 91","314118","2402 Erringer Rd","515 15TH ST NW","Aleje Jerozolimskie 134","2399 COTTMAN AVE","DOLGWILI ROAD","10B 3 MAJA","730 Noble St","730 Noble St","730 Noble St","730 NOBLE ST","45160 Seeley Dr","89 EBERSTÄDTER STR.","26 ENGELDORFER STR.","2 IMMENDORFER STR.","COMMERCIAL STREET","Ulica Monte Cassino 2","10 GALILEO-GALILEI STR.","8 MOTORYZACYJNA","8 UL. MOTORYZACYJNA","2811 NW 10th St","THE ASTON TRIANGLE","23 WITTEKINDSTR.","Ulica Wodna 15","22 MAŁACHOWSKIEGO","36 UL. MAŁACHOWSKIEGO STANISŁAWA","3586 Rhea County Hwy","Aleja Walentego Roździeńskiego 188B","Ulica Marii Skłodowskiej-Curie 24A","Ulica Elizy Orzeszkowej 17","40 WOLTERSDORFER STR.","525 SW MORRISON ST","176 N COMMERCE WAY","41H UL. OBORNICKA","Ulica Toruńska 222 87-805","Radzikowice 1C","7540 GARNERS FERRY RD","Ulica Aleksandra Ostrowskiego 9","21/2 UL. MAŁA ODRZAŃSKA","2525 W 4TH AVE","300 Ted Turner Dr NW","Dworzec Gdański Stacja"};
        //String[] tests = new String[]{"552 The Holloway Street Rd", "1 CALLE SAN GERONIMO"};
        String[] tests = new String[]{"Rua De Pequim 112"};
        java.util.Date date = new java.util.Date();
        Timestamp timestamp1 = new Timestamp(date.getTime());
        for (int i=0; i<1; i++){
            System.out.println("I -> "+i);
        for (String item: tests){
            doTagging(model, item);
        }}

        java.util.Date date2 = new java.util.Date();
        Timestamp timestamp2 = new Timestamp(date2.getTime());

        long milliseconds = timestamp2.getTime() - timestamp1.getTime();
        double seconds = (double)milliseconds/1000;

        System.out.println("Time Taken: "+milliseconds);
        System.out.println("Timestamp1: "+date);
        System.out.println("Timestamp2: "+date2);
    }
}



/*
 * 

# Compiling the Java file


# Running the class
java -cp "jars/*:." PredictNER1.java


 */