package csoh.ref.depinject;
import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.*;

@Configuration
@ComponentScan
public class App {

    @Bean
    MessageService emailService() {
        return new EmailService();
    }
    public static void main(String[] args) {
        /* 1) What's the problem with this design? */
        Person p = new Person();
        p.sendMessage("Hello");


        /* 2) Use interface : MessageService */
        MessageService ms = new EmailService();
        BetterPerson bp = new BetterPerson(ms);
        bp.sendMessage("Hello");

        /*3) Dependency injection

         BetterPerson bp = dependecyFramework.getInstance(BetterPerson.class);
         bp.sendMessage("mmmmm");

         a) needs dependency framework configuration so that it knows how to
            instantiate the EmailService and BetterPerson

            BetterPerson also needs to anotate @Inject ...

            Advantage
             Testing and Mocking the message service


         */
        ApplicationContext context = new AnnotationConfigApplicationContext(App.class);
        BetterPerson bp2 = context.getBean(BetterPerson.class);
        bp2.sendMessage("Hello");





    }
}


