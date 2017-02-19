import com.fourspaces.couchdb.Database;
import com.fourspaces.couchdb.Document;
import com.fourspaces.couchdb.Session;

import java.net.UnknownHostException;

/**
 * Created by damith on 12/15/16.
 */
public class CouchDBConnection {

    private String host;
    private int port;
    private String dbName;
    private Session dbSession;
    private Database db;

    public CouchDBConnection() throws UnknownHostException {
        try {
            this.host = host;
            this.port = port;
            this.dbName = dbName;

            dbSession = new Session(host,port);
            db = dbSession.getDatabase(dbName);
        }catch (Exception e) {
            e.printStackTrace();
        }
    }

    public void writeCouchDB(Document doc){
        db.saveDocument(doc);
    }

    public Database getDatabase(){
        return this.db;
    }
}
