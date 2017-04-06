import { Component, OnInit, ChangeDetectorRef } from '@angular/core';
import { HttpDataService } from '../http-data.service';


@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
  
  private data = {"by_tenant" : []}; 
  private by_tenant = [];
  constructor(private httpDataService : HttpDataService
  	, public changeDetector : ChangeDetectorRef ) { }

  ngOnInit() {
  	this.httpDataService.getDbInfo()
  	.subscribe(
      this._setData ,
      error => console.log(<any>error));
  }

  _setData(json) {
  	
  	this.data = json;
  	this.by_tenant = json.by_tenant;
  	// this.changeDetector.detectChanges();
  	console.log(this.by_tenant + "<<<<<");
  }

}
