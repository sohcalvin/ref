import { Component, OnInit } from '@angular/core';
import { User } from '../user';
import { HttpDataService } from '../../http-data.service';

@Component({
  selector: 'user-list',
  templateUrl: './user-list.component.html',
  styleUrls: ['./user-list.component.css']
})
export class UserListComponent implements OnInit {
	userList : User[];

  	constructor(private httpService : HttpDataService) { }

  	ngOnInit() {
  		this.refresh();
  	}

  	refresh(){
  		this.httpService.getUserList().subscribe(
      	j => { 
      		this.userList= [];
      		for(var i in j){
      			let u = j[i];
      			let user = new User(u["email"], u["firstName"], u["lastName"], u["password"], u["roles"]);
      			this.userList.push(user);
      		} 	

      	}
      ,error => console.log(<any>error));
  	}

  	getUserListAsTableData(){
  		var tabData = {
  			"id" : "userlist",
  			"header_keys" : ["name", "email", "roles"],
  			"data" : this.userList
  		};
  		return tabData;

  	}

}
