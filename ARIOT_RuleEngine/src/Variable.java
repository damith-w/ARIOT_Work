import java.util.Map;

/**
 * Created by damith on 12/7/16.
 */
public class Variable implements Expression {

    private String name;

    public Variable(String name){
        this.name = name;
    }

    public String getName(){
        return this.name;
    }

    @Override
    public boolean interpret(Map<String, ?> bindings) {
        return true;
    }
}
