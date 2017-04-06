import { Injectable } from '@angular/core';
import { Http, Response }       from '@angular/http';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/catch';
import 'rxjs/add/operator/map';

@Injectable()
export class HttpDataService {

  constructor(private http : Http) { }

  public getDbInfo() : Observable<JSON[]>{
  	// console.log("getDbInfo" + this.http);
  	return this.http.get("assets/t.json")
            .map(response => response.json())
            .catch(this.handleError);

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
