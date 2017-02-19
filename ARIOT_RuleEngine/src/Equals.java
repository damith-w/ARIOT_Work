import java.util.Map;
import java.util.Stack;

/**
 * Created by damith on 12/7/16.
 */
public class Equals extends Operation {
    public Equals()
    {
        super("=");
    }

    @Override
    public Equals copy()
    {
        return new Equals();
    }

    @Override
    public int parse(final String[] tokens, int pos, Stack<Expression> stack)
    {
        if (pos-1 >= 0 && tokens.length >= pos+1)
        {
            String var = tokens[pos-1];

            this.leftOperand = new Variable(var);
            this.rightOperand = BaseType.getBaseType(tokens[pos+1]);
            stack.push(this);

            return pos+1;
        }
        throw new IllegalArgumentException("Cannot assign value to variable");
    }

    @Override
    public boolean interpret(Map<String, ?> bindings)
    {

        Variable v = (Variable)this.leftOperand;
        Object obj = bindings.get(v.getName());
        if (obj == null)
            return false;

        BaseType<?> type = (BaseType<?>)this.rightOperand;

        if ((Math.abs(Float.valueOf(type.getValue().toString()) - Float.valueOf(obj.toString())) < 0.001)) {
            return true;
        }
        return false;
    }
}
