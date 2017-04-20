import { Component, OnInit } from '@angular/core';
import { User } from '../user';
import { HttpDataService } from "../../http-data.service";


@Component({
  selector: 'user-form',
  templateUrl: './user-form.component.html',
  styleUrls: ['./user-form.component.css']
})
export class UserFormComponent implements OnInit {
	roles : string[] = [ "recruiters"];

	user : User = new User("--email--","","","",[]);

  	constructor(private httpDataService : HttpDataService) { }

  	ngOnInit() {
  	}
	
	postNewUser(){
		this.httpDataService.postNewUser(this.user)
		.subscribe(j=> console.log(j),
		error => console.log(<any>error));
	}

 
}
