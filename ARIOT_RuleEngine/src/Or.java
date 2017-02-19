import java.util.Map;
import java.util.Stack;

/**
 * Created by damith on 12/8/16.
 */
public class Or extends Operation{
    public Or()
    {
        super("OR");
    }

    public Or copy()
    {
        return new Or();
    }

    @Override
    public int parse(String[] tokens, int pos, Stack<Expression> stack)
    {
        Expression left = stack.pop();
        int i = findNextExpression(tokens, pos+1, stack);
        Expression right = stack.pop();

        this.leftOperand = left;
        this.rightOperand = right;

        stack.push(this);

        return i;
    }

    @Override
    public boolean interpret(Map<String, ?> bindings)
    {
        return leftOperand.interpret(bindings) || rightOperand.interpret(bindings);
    }
}
