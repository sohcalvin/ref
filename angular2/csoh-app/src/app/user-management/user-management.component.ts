import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-user-management',
  templateUrl: './user-management.component.html',
  styleUrls: ['./user-management.component.css']
})
export class UserManagementComponent implements OnInit {
  private showDialog :boolean= false;
  constructor() { }

  ngOnInit() {
  }

  // popoverNewUserForm(target: HTMLElement) : void{
  // 	console.log(target);
  // }

}
