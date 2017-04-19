import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { CTableComponent } from './ctable/ctable.component';

@NgModule({
  imports: [
    CommonModule
  ],
  declarations: [
  	CTableComponent
  ],
  exports: [
  	CTableComponent
  ]
})
export class CUtilityModule { }
