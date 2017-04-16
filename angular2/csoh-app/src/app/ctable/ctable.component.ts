import { Component, OnInit, Input } from '@angular/core';


@Component({
  selector: 'ctable',
  templateUrl: './ctable.component.html',
  styleUrls: ['./ctable.component.css']
})
export class CtableComponent implements OnInit {
	@Input() tableData: any=[];
	@Input() tableStyle = ['table'];
	@Input() columnStyle=[];

  	constructor() { }

  	ngOnInit() {
  	}

}
