import java.util.ArrayList;
import java.util.List;
import java.util.Map;

/**
 * Created by damith on 12/8/16.
 */
public class Rules {

    List<Rule> rule_stack = new ArrayList<>();

    public void addRule(Rule rule1) {
        rule_stack.add(rule1);
    }

    public boolean eval(Map<String, String> bindings) {
        for(int i=0;i<rule_stack.size();i++){
            rule_stack.get(i).eval(bindings);

        }
        return false;
    }
}
