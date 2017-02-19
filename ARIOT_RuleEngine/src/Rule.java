import java.util.ArrayList;
import java.util.List;
import java.util.Map;

/**
 * Created by damith on 12/7/16.
 */
public class Rule {
    private List<Expression> expressions;
    private ActionDispatcher dispatcher;
    private String device_id;

    public String getDevice_id(){
        return this.device_id;
    }

    public static class Builder
    {
        private List<Expression> expressions = new ArrayList<>();
        private ActionDispatcher dispatcher = new NullActionDispatcher();
        private String device_id = "";

        public Builder withExpression(Expression expr)
        {
            expressions.add(expr);
            return this;
        }

        public Builder withDispatcher(ActionDispatcher dispatcher)
        {
            this.dispatcher = dispatcher;
            return this;
        }

        public Builder withDeviceId(String device_id)
        {
            this.device_id = device_id;
            return this;
        }

        public Rule build()
        {
            return new Rule(expressions, dispatcher, device_id);
        }
    }

    private Rule(List<Expression> expressions, ActionDispatcher dispatcher, String device_id)
    {
        this.expressions = expressions;
        this.dispatcher = dispatcher;
        this.device_id = device_id;
    }

    public boolean eval(Map<String, ?> bindings)
    {
        boolean eval = false;
        for (Expression expression : expressions)
        {
            eval = expression.interpret(bindings);
            if (eval)
                dispatcher.fire();
        }
        return eval;
    }
}
