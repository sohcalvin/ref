import { Component, OnInit } from '@angular/core';
import { HttpDataService } from '../http-data.service';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
  
  private data:JSON[] = [];

  constructor(private httpDataService : HttpDataService) { }

  ngOnInit() {
  	this.httpDataService.getDbInfo()
  	.subscribe(
      this.setData ,
      // json => console.log(json.toString()),
      error => console.log(<any>error));
  }

  setData(jsonList) {
  	this.data = jsonList;
  	console.log(this.data);
  }

}
