package schizoconnect;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Set;


public class SchizoTests {

    public static void main(String[] args) throws Exception{
    			
		List<String> files = Arrays.asList("MetaData","Cobre","FBirn","MCIC","NU","Nusdast","BrainGluSchi");		
		String[][][] tables = new String[files.size()][][];
		for(int i=0; i<files.size(); i++) 
			tables[i] = getTable(files.get(i)+".txt");
		
		int nrows = 1, row = 1;
		for(int k=1; k<tables.length; k++) nrows += tables[k].length-1;
		List<Integer> columns = Arrays.asList(1,3,4,5,7,8);
		String[][] postTables = new String[nrows][columns.size()];
		for(int j=0; j<columns.size(); j++) postTables[0][j] = tables[1][0][columns.get(j)];
		
		for(int k=1; k<tables.length; k++) 
			for(int i=1; i<tables[k].length; i++, row++) 
				for(int j=0; j<columns.size(); j++)
					try { postTables[row][j] = tables[k][i][columns.get(j)]; }
					catch(Exception e) { postTables[row][j] = null; }

		Map<String,Integer> assessmentDic = new HashMap<String,Integer>();
		Map<String,Set<String>> assessmentOverlap = new HashMap<String,Set<String>>();
		for(int i=1; i<postTables.length; i++) {
			String[] entry = postTables[i];
			if(assessmentDic.containsKey(entry[3])) { 
				assessmentOverlap.get(entry[3]).add(entry[0]);
				assessmentDic.put(entry[3], assessmentDic.get(entry[3])+1);
			} else {
				assessmentOverlap.put(entry[3],new HashSet<String>());
				assessmentDic.put(entry[3],1);
			}
		}
		
		Map<Integer,List<String>> orderedOverlap = new HashMap<Integer,List<String>>();
		for(int i=1; i<files.size(); i++) orderedOverlap.put(i, new ArrayList<String>());
		for(Entry<String,Set<String>> entry : assessmentOverlap.entrySet()) 
				orderedOverlap.get(entry.getValue().size()).add(entry.getKey());
		for(Entry<Integer,List<String>> entry : orderedOverlap.entrySet()) 
			System.out.println(entry.getKey()+"=>"+entry.getValue().size());
	}

	private static String[][] getTable(String filename) throws IOException {
		List<String[]> table = new ArrayList<String[]>();
		BufferedReader br = new BufferedReader(new FileReader(filename));
        String line, delimiter = ",";
	    while ((line=br.readLine())!=null && line.contains(delimiter))
	    	table.add(line.split(delimiter));
		br.close();
		String[][] result = new String[table.size()][];
		for(int i=0; i<table.size(); i++) result[i] = table.get(i);
		return result;
	}
}