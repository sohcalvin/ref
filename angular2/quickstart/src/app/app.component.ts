import { Component } from '@angular/core';
import {BackendService } from './backend.service';

@Component({
  selector: 'my-app',
  template: `<h1>Hello {{name}}</h1>
  <div (click) = "doSomething()">abc</div>
  `
  
})

export class AppComponent  { 
 
  name = 'Angular'; 
  constructor(private backendService :BackendService){}

  doSomething( ) :void {
    console.log("something clicked " + this.backendService);
    this.backendService.getPage()
     .subscribe(
                     json => console.log(json),
                     error =>  console.log( <any>error));    
  }

}
