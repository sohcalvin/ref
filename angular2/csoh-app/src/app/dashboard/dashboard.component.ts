import { Component, OnInit, ChangeDetectorRef } from '@angular/core';
import { HttpDataService } from '../http-data.service';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
  
  private data = undefined; 
  private sections = [];

  constructor(private httpDataService : HttpDataService) { }

  ngOnInit(){
  	this.refresh();
  }

  refresh() {
  	this.httpDataService.getDbInfo()
  	.subscribe(
      	j => this.data = j
      ,error => console.log(<any>error));
  }


}
