import java.util.HashMap;
import java.util.Map;

/**
 * Created by damith on 12/8/16.
 */
public class Main {
    public static void main( String[] args )
    {
        // create a singleton container for operations
        Operations operations = Operations.INSTANCE;

        // register new operations with the previously created container
        operations.registerOperation(new And());
        operations.registerOperation(new Equals());
        operations.registerOperation(new Not());
        operations.registerOperation(new GreaterThan());
        operations.registerOperation(new Or());
        operations.registerOperation(new LessThan());

        // defines the triggers when a rule should fire
        Expression ex1 = ExpressionParser.fromString("temp < 50 AND vibration < 100");
        Expression ex2 = ExpressionParser.fromString("temp = 501");

        // define the possible actions for rules that fire
        ActionDispatcher anomaly001 = new anomaly001_Dispatcher();
        ActionDispatcher anomaly002 = new anomaly002_Dispatcher();

        String id1 = "0001";
        String id2 = "0002";

        // create the rules and link them to the according expression and action
        Rule rule1 = new Rule.Builder()
                .withExpression(ex1)
                .withDispatcher(anomaly001)
                .withDeviceId(id1)
                .build();

        Rule rule2 = new Rule.Builder()
                //.withExpression(ex1)
                .withExpression(ex2)
                .withDispatcher(anomaly002)
                .withDeviceId(id2)
                .build();

        Rule rule3 = new Rule.Builder()
                .withExpression(ex2)
                .withDispatcher(anomaly002)
                .build();

        System.out.println(rule1.getDevice_id());
        // add all rules to a single container
        Rules rules = new Rules();
        rules.addRule(rule1);
        rules.addRule(rule2);
        //rules.addRule(rule3);

        // for test purpose define a variable binding ...
        Map<String, String> bindings = new HashMap<>();
        bindings.put("temp", "50");
        bindings.put("vi", "5000");
        // ... and evaluate the defined rules with the specified bindings
        boolean triggered = rules.eval(bindings);
        //System.out.println("Action triggered: "+triggered);
    }
}
