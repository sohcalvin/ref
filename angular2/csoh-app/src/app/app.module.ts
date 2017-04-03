import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import { RouterModule, Routes } from '@angular/router';

import { AppComponent } from './app.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { PageNotFoundComponent } from './page-not-found/page-not-found.component';

const appRoutes: Routes = [
  { path: 'dashboard', component: DashboardComponent }
  // { path: 'hero/:id',      component: HeroDetailComponent },
  // {
  //   path: 'heroes',
  //   component: HeroListComponent,
  //   data: { title: 'Heroes List' }
  // },
  // ,{ path: '',
  //   redirectTo: '/heroes',
  //   pathMatch: 'full'
  // }
  ,{ path: '',
    component: PageNotFoundComponent
  }
  ,{ path: '**', component: PageNotFoundComponent }
];


@NgModule({
  declarations: [
    AppComponent,
    DashboardComponent,
    PageNotFoundComponent
  ],
  imports: [
     BrowserModule
    ,FormsModule
    ,HttpModule
    ,RouterModule.forRoot(appRoutes)    
    
   
  ],
  providers: [ ],
  bootstrap: [AppComponent]
})
export class AppModule { }
