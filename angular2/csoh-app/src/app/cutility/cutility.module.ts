import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { CTableComponent } from './ctable/ctable.component';
import { CDialogComponent } from './cdialog/cdialog.component';

@NgModule({
  imports: [
    CommonModule
  ],
  declarations: [
  	CTableComponent,
  	CDialogComponent
  ],
  exports: [
  	CTableComponent,
  	CDialogComponent
  ]
})
export class CUtilityModule { }
