import { Component } from '@angular/core';
import { BackendService } from './backend.service';

@Component({
  selector: 'my-app',
  template: `
  <label class="btn btn-primary" (click)="doSomething()">abc</label>
  <textarea [(ngModel)]="command" class="form-control" rows="5" id="comment"></textarea>
 
  <div><pre>{{output}}</pre></div>
  `

})

export class AppComponent {

  command: String;
  output: String;
  constructor(private backendService: BackendService) { }

  doSomething(): void {
    console.log("something clicked " + this.command);
    this.backendService.sendCommand(this.command)
      .subscribe(
      json => this.output = json.toString(),
      error => console.log(<any>error));
  }

}
