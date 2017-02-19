import java.util.Map;

/**
 * Created by damith on 12/7/16.
 */
public interface Expression {
    public boolean interpret(final Map<String, ?> bindings);
}
