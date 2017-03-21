import {BackendService}  from './backend.service';
import { NgModule }      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppComponent }  from './app.component';

import { Http,HttpModule, JsonpModule } from '@angular/http';

// FormsModule,
@NgModule({
  imports:      [  
    BrowserModule,
    HttpModule
  ],
  declarations: [ AppComponent ],
  providers : [ BackendService ],
  bootstrap:    [ AppComponent ]
})
export class AppModule { }
