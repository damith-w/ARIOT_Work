import java.util.Map;
import java.util.Stack;

/**
 * Created by damith on 12/7/16.
 */
public class Not extends Operation{
    public Not()
    {
        super("NOT");
    }

    public Not copy()
    {
        return new Not();
    }

    @Override
    public int parse(String[] tokens, int pos, Stack<Expression> stack)
    {
        int i = findNextExpression(tokens, pos+1, stack);
        Expression right = stack.pop();

        this.rightOperand = right;
        stack.push(this);

        return i;
    }

    @Override
    public boolean interpret(final Map<String, ?> bindings)
    {
        return !this.rightOperand.interpret(bindings);
    }
}
