import {BackendService}  from './backend.service';
import { NgModule}      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppComponent }  from './app.component';
import { FormsModule }   from '@angular/forms'; //need this for 2way binding
import { Http,HttpModule, JsonpModule } from '@angular/http';
import {NgbModule} from '@ng-bootstrap/ng-bootstrap';


// FormsModule,
@NgModule({
  imports:      [  
    BrowserModule,
    HttpModule, FormsModule,
    NgbModule.forRoot()
  ],
  declarations: [ AppComponent ],
  providers : [ BackendService ],
  bootstrap:    [ AppComponent ]
})
export class AppModule { }
