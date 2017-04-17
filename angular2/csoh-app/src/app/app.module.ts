import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';

import { AppRoutingModule} from './app-routing.module';
import { AppComponent } from './app.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { PageNotFoundComponent } from './page-not-found/page-not-found.component';
import { HttpDataService } from './http-data.service';
import { CtableComponent } from './ctable/ctable.component';
import { UserFormComponent } from './user-form/user-form.component';
;

@NgModule({
  declarations: [
    AppComponent,
    DashboardComponent,
    PageNotFoundComponent,
    CtableComponent,
    UserFormComponent
  ],
  imports: [
     BrowserModule
    ,FormsModule
    ,HttpModule
    ,AppRoutingModule   
    
   
  ],
  providers: [ HttpDataService ],
  bootstrap: [AppComponent]
})
export class AppModule { }
