import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { CTableComponent } from './ctable/ctable.component';
import { CDialogComponent } from './cdialog/cdialog.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';


@NgModule({
  imports: [
    CommonModule,
    BrowserAnimationsModule
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
