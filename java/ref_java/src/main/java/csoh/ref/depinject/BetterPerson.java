package csoh.ref.depinject;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

@Component
public class BetterPerson {
    private MessageService messageService;
    @Autowired
    public BetterPerson(MessageService messageService){
        this.messageService = messageService;
    }


    public void sendMessage(String message){
        messageService.sendMessage("BetterPersion sending : " + message);
    }

}
