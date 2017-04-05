import { Component, OnInit } from '@angular/core';
import { HttpDataService } from '../http-data.service';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {

  constructor(private httpDataService : HttpDataService) { }

  ngOnInit() {
  	this.httpDataService.getDbInfo()
  	.subscribe(
      // json => this.output = json.toString(),
      json => console.log(json.toString()),
      error => console.log(<any>error));
  }

}
