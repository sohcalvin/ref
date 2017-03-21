// import { FormsModule } from '@angular/forms';
// import { HttpModule, JsonpModule } from '@angular/http';
import { Injectable,OnInit } from '@angular/core';
import { Headers, Http,Response } from '@angular/http';

import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/catch';
import 'rxjs/add/operator/map';

@Injectable()
export class BackendService {//implements OnInit  {

    constructor(private http : Http) {
        console.log("Constructing HttpService");
    }

    // ngOnInit(){
    //     console.log("OnInit in HttpSerice");
    // }

    getPage(): Observable<JSON[]> {
        console.log("Getting page");
        return this.http.get("t.json")
            .map(response => response.json())
            .catch(this.handleError);
    }
    public printSome():void{
        console.log("Backend service reached");
    }
    private handleError(error: Response | any) {
        // In a real world app, you might use a remote logging infrastructure
        let errMsg: string;
        if (error instanceof Response) {
            const body = error.json() || '';
            const err = body || JSON.stringify(body);
            errMsg = `${error.status} - ${error.statusText || ''} ${err}`;
        } else {
            errMsg = error.message ? error.message : error.toString();
        }
        console.error(errMsg);
        return Observable.throw(errMsg);
    }


}