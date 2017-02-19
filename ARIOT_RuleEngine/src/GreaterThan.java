import java.util.Map;
import java.util.Stack;

/**
 * Created by damith on 12/8/16.
 */
public class GreaterThan extends Operation{
    public GreaterThan(){super(">");}

    @Override
    public GreaterThan copy() {return new GreaterThan();}

    @Override
    public int parse(String[] tokens, int pos, Stack<Expression> stack) {
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
    public boolean interpret(Map<String, ?> bindings) {
        Variable v = (Variable)this.leftOperand;
        Object obj = bindings.get(v.getName());

        if (obj == null)
            return false;

        BaseType<?> type = (BaseType<?>)this.rightOperand;

        if (Float.valueOf(type.getValue().toString()) < Float.valueOf(obj.toString())) {
            return true;
        }

        return false;
    }
}
