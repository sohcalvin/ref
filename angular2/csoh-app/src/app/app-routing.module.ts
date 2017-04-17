import { RouterModule, Routes } from '@angular/router';
import { NgModule } from '@angular/core';
import { DashboardComponent } from './dashboard/dashboard.component';
import { PageNotFoundComponent } from './page-not-found/page-not-found.component';
import { UserFormComponent } from './user-form/user-form.component';
const appRoutes: Routes = [
  { path: 'dashboard', component: DashboardComponent }
  ,{ path: 'admin', component: UserFormComponent }
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
  imports: [
    RouterModule.forRoot(appRoutes)
    
  ],
  exports: [
    RouterModule
  ]
})
export class AppRoutingModule {}
