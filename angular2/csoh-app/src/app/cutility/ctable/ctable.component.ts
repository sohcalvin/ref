import { Component, OnInit, Input,OnChanges } from '@angular/core';


@Component({
  selector: 'ctable',
  templateUrl: './ctable.component.html',
  styleUrls: ['./ctable.component.css']
})
export class CTableComponent implements OnInit,OnChanges {
	@Input() tableData={};  // Please do not reference this directly in template
	@Input() tableStyle = ['table'];
	@Input() columnStyle=[];

	/** table data fields **/
	title : String;
	header_labels : String[];
	header_keys : String[];
	data : any[];

  	constructor() { }

  	ngOnInit() {
  	}

  	ngOnChanges(){
  		this.title = this.tableData['title'];
  		this.header_labels = this.tableData['header_labels']? this.tableData['header_labels']: [];
  		this.header_keys = this.tableData['header_keys'];
  		this.data =  this.tableData['data'];
  	}


}
