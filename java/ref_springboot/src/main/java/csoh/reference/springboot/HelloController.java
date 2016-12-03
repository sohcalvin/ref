package csoh.reference.springboot;

/**
 * Created by calvinsoh on 25/9/2016.
 */


import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;

@RestController
public class HelloController {

    @RequestMapping("/")
    public String index() {
        return "Greetings from Spring Bootx!";
    }

}