import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';

import { AppRoutingModule} from './app-routing.module';
import { AppComponent } from './app.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { PageNotFoundComponent } from './page-not-found/page-not-found.component';
import { HttpDataService } from './http-data.service';
// import { CTableComponent } from './ctable/ctable.component';
import { UserFormComponent } from './user-management/user-form/user-form.component';
import { UserListComponent } from './user-management/user-list/user-list.component';
import { UserManagementComponent } from './user-management/user-management.component';
import { CUtilityModule } from "./cutility/cutility.module";

@NgModule({
  declarations: [
    AppComponent,
    DashboardComponent,
    PageNotFoundComponent,
    UserFormComponent,
    UserListComponent,
    UserManagementComponent
  ],
  imports: [
     BrowserModule
    ,FormsModule
    ,HttpModule
    ,AppRoutingModule
    ,CUtilityModule  
    
   
  ],
  providers: [ HttpDataService ],
  bootstrap: [AppComponent]
})
export class AppModule { }
