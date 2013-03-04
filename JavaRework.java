import java.nio.charset.Charset;
import java.io.BufferedReader;
import java.io.IOException;
import java.nio.file.*;

public class JavaRework {
    
    private static final int LINE_SEARCH = 25;
    private String[][] testArray = new String[100][100];
    private int highestPoint = 0;
    private int veryHighestPoint = 0;
    
    public JavaRework() {

        System.out.println(getBinaryMap(15));
        
        String fileName = "triangle.txt";
        Charset charset = Charset.forName("US-ASCII");
        Path file = Paths.get(fileName); 
        int counter = 0;        
        
        try (BufferedReader reader = Files.newBufferedReader(file, charset)) {
            String line = null;
            while ((line = reader.readLine()) != null) {
                testArray[counter] = line.split(" ");
                counter++;
            }    
        }
        catch (IOException x) {
            System.err.format("IOException: %s%n", x);
        }      
    }
    
    private void calculateSequence() {
        int tempNum = 0;
        int highNum = 0;
        String[] tempList = new String[LINE_SEARCH];
        String[] highList = new String[LINE_SEARCH];
        
        for(int x = 0; x < 100; x++) {
            tempNum = 0;
            tempList = getHighestSequence(99, x);
            for(String i : tempList) {
                tempNum += Integer.parseInt(i);
            }
            if(tempNum > highNum) {
                highNum = tempNum;
                highList = tempList; 
                veryHighestPoint = highestPoint;
            }
        }
    }
    
    private String getBinaryMap(int toBinary) {
        String binaryNumber = Integer.toBinaryString(toBinary);
        return binaryNumber;
    }
    
    private String[] getHighestSequence(int rowCheck, int columnCheck) {
        int total = 0;
        int tempTotal = 0;
        String[] highestSequence = new String[LINE_SEARCH];
        String[] tempSequence = new String[LINE_SEARCH];
        long mapperCount = 0;
        String[] mapper = new String[LINE_SEARCH];
        char[] binMap = new char[LINE_SEARCH];
        int counter = 0;
        int highestPoint = 0;
        int currentColumn = 0;
        int currentRow = 0;
        int binMapCounter = 1;
        
        for(int i = 0; i < 33554432; i++) {
            currentColumn = columnCheck;
            currentRow = rowCheck;
            getBinaryMap(i).getChars(0, LINE_SEARCH, binMap, 0);
            mapper[0] = Integer.toString(columnCheck);
            
            for(int z : binMap) {
                binMapCounter = 1;
                currentRow -= 1;
                currentColumn -= (z - 48);
                if(currentColumn >= currentRow) {
                    mapper[binMapCounter] = String.valueOf(currentRow);
                }
                else if (currentColumn < 0) {
                    mapper[binMapCounter] = "0";
                }
                else {
                    mapper[binMapCounter] = String.valueOf(currentColumn);
                }
                binMapCounter++;
            }
            
            for(int moveUp = rowCheck; moveUp >= (rowCheck - LINE_SEARCH); i--) {
                tempSequence[counter] = 
                    testArray[moveUp][Integer.parseInt(mapper[counter])];
                counter++;
            }
            
            for(String x : tempSequence) {
                tempTotal += Integer.parseInt(x);
            }
            
            if(tempTotal > total) {
                total = tempTotal;
                highestSequence = tempSequence;
                setHighestPoint(Integer.parseInt(mapper[LINE_SEARCH - 1]));
            }
            
            tempSequence = null;
            tempTotal = 0;
            counter = 0;
            mapper = null;
        }
        return highestSequence;
    }
    
    private void setHighestPoint(int highestPoint) {
        this.highestPoint = highestPoint;
    }
    
}