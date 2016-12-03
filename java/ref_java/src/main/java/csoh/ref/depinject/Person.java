package csoh.ref.depinject;
public class Person {
    private Email email = new Email();

    public void sendMessage(String mess) {
        email.sendMessage("Person sending : " + mess);
    }
}

