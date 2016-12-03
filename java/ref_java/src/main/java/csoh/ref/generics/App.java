package csoh.ref.generics;
public class App{
    public static void main(String[] args){
        Environment e = new UnixEnvironment();
        Diagnostic<Environment> d = new Diagnostic<Environment>(e);
        System.out.println(d.run());
        ((UnixEnvironment)e).setHealthy(false);
        System.out.println(d.run());
    }
}
class Diagnostic<E extends Environment> {
    private E env = null;
    public Diagnostic(E e){
        env = e;
    }
    public String run(){
        return env.ping()? "Healthy" : "Sick";
    }
}
interface Environment {
    boolean ping();
}
class UnixEnvironment implements Environment{
    boolean healthy = true;
    public void setHealthy(boolean h){ healthy = h;}

    public boolean ping(){
        return healthy;
    }
}


