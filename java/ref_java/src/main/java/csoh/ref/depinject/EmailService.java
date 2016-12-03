package csoh.ref.depinject;

public class EmailService implements MessageService {

    public void sendMessage( String message){
        System.out.printf("EmailService> %s\n", message);
    }
}