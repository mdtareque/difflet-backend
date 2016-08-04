import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.UnsupportedEncodingException;
import java.util.ArrayList;
import java.util.regex.Matcher;
import java.util.regex.Pattern;


public class ExtractProperties {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub

		String filePath = "/home/harsha/IRE/index/primary/";
		
			
			BufferedReader in = new BufferedReader (new InputStreamReader(new FileInputStream("/home/harsha/Project/difflet-backend/parts/country"),	"UTF-8"));
	        String eachLine ;   
	        
	        Pattern resRegx = Pattern.compile("<http://dbpedia.org/resource/(.*?)>");
	        Pattern propRegx = Pattern.compile("<http://dbpedia.org/property/(.*?)>");
	        Pattern valueRegx = Pattern.compile("<.*?> <.*?> (.*)");
	        
	        String entity="";
	        ArrayList<String> properties = new ArrayList<String>();
	        
	        while( (eachLine = in.readLine()) != null) 
	        {
	        	
	        	Matcher matcher1 = resRegx.matcher(eachLine);
	        	String curEntity = null;
	        	if (matcher1.find())
	        	{	curEntity = matcher1.group(1);
	        	}
	        	
	        	
	        	if(entity != curEntity) {
	        		if(properties!=null) {
	        			writeToFile(entity,properties);
	        			properties.clear();
	        		}
	        		entity = curEntity;
	        				
	        	}
	        	
	        	Matcher matcher2 = propRegx.matcher(eachLine);
	        	Matcher matcher3 = valueRegx.matcher(eachLine);
	        	
	        	String property = new String();
	        	if (matcher2.find() && matcher3.find()) {
	        		String value = matcher3.group(1);
	        		value=sanitize(value);
	        		properties.add(matcher2.group(1) +" "+ value);
	        	}
	        	
	        } 
	        
	        in.close();
		    
	}

	private static String sanitize(String value) {
		// TODO Auto-generated method stub
		Pattern linkRegx = Pattern.compile("^<http://dbpedia.org/resource/(.*?)>.*");
		Pattern quoteRegx = Pattern.compile("^\\\"(.*?)\\\"");
        
		if(value.charAt(0) == '<') {
			
			Matcher matcher = linkRegx.matcher(value);
        	if (matcher.find())
        	{	
        		value = matcher.group(1);
        	    System.out.println(matcher.group(1));
        	}
		}
		else
		if(value.charAt(0) == '\"') {
			
			Matcher matcher = quoteRegx.matcher(value);
        	if (matcher.find())
        	{	
        		value = matcher.group(1);
        	    System.out.println(matcher.group(1));
        	}
		}
		
		return value;
		
	}

	private static void writeToFile(String entity, ArrayList<String> properties) {
		// TODO Auto-generated method stub
		
		if(properties == null || entity== "") return;
		
		try {
			BufferedWriter out = new BufferedWriter(new FileWriter("/home/harsha/Project/difflet-backend/index/"+entity,true));
			
			for(String line:properties) {
				out.write(line+"\n");
			}
			out.close();
		} catch (UnsupportedEncodingException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	       
	}

}
