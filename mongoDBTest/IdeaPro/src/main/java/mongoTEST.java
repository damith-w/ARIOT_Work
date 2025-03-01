package main.java;

import com.mongodb.MongoClient;
import com.mongodb.DB;
import com.mongodb.DBCollection;
import com.mongodb.BasicDBObject;
import com.mongodb.DBCursor;

public class mongoTEST {

    public static void main(String args[]){

        try{

            // Creating a connection to mongodb server as a client
            MongoClient mongoClient = new MongoClient( "localhost" , 27017 );
            System.out.println("Mongo client connected successfully");

            // Connect to your databases --> db_name = "testDatabase"
            // If the requested DB is not there, This will create the DB for you.
            DB db = mongoClient.getDB( "testDatabase111" );
            System.out.println("Connect to database successfully");

            String collectionName = "testCollection11";

            // Getting the collection
            // If requested collection is not there, This will create the collection
            DBCollection coll1 = db.getCollection(collectionName);
            System.out.println("Collection selected successfully");

            // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            //      Measure time taken for a code chunk
            // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            long startTime = System.currentTimeMillis();

            // Put your code here and execute


            long stopTime = System.currentTimeMillis();
            long timeTaken = stopTime - startTime;
            System.out.println("Time taken to finish the execution:  "+timeTaken+" ms");

            // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            //          Insert a document into database
            // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

           /* BasicDBObject doc = new BasicDBObject("_id", "0000002").
                    append("device_id", 0000002).
                    append("test_value", 100).
                    append("year", 2016).
                    append("month", 06).
                    append("day", 30).
                    append("hour", 12).
                    append("minute", 24).
                    append("second", 46).
                    append("milli_second", 22);

            coll1.insert(doc);
            System.out.println("Document inserted successfully");*/

            // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            //          Find all the documents in the database.
            // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

           /* DBCursor cursor = coll1.find();
            int i = 1;

            while (cursor.hasNext()) {
                System.out.println("Inserted Document: "+i);
                System.out.println(cursor.next());
                i++;
            }*/

            // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            //          Find a specific document from the database (whereQuary)
            // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            /*BasicDBObject whereQuery = new BasicDBObject();
            whereQuery.put("title", "MongoDB");
            DBCursor cursor1 = coll1.find(whereQuery);
            while(cursor1.hasNext()) {
                System.out.println(cursor1.next());
            }*/

        }catch(Exception e){
            System.err.println( e.getClass().getName() + ": " + e.getMessage() );
        }
    }

}
