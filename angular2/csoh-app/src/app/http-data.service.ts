import { Injectable } from '@angular/core';
import { Http, Response, RequestOptions, Headers}       from '@angular/http';
import { Observable } from 'rxjs/Observable';
import { User } from "./user-management/user";
import 'rxjs/add/operator/catch';
import 'rxjs/add/operator/map';

@Injectable()
export class HttpDataService {
    private urlPostNewUser="assets/summary.json";

  constructor(private http : Http) { }

  public getDbInfo() : Observable<JSON[]>{
  	return this.http.get("assets/summary.json")
            .map(response => response.json())
            .catch(this.handleError);

  }

  public getUserList() : Observable<JSON[]>{
    return this.http.get("assets/userlist.json")
            .map(response => response.json())
            .catch(this.handleError);

  }
  
  public postNewUser(user : User) : Observable<JSON[]>{
    let bodyString = JSON.stringify(user); // Stringify payload
    let headers    = new Headers({ 'Content-Type': 'application/json' }); // ... Set content type to JSON
    let options    = new RequestOptions({ headers: headers }); // Create a request option

    return this.http.post(this.urlPostNewUser, bodyString, options) // ...using post request
                         .map((res:Response) => res.json()) // ...and calling .json() on the response to return data
                         .catch((error:any) => Observable.throw(error.json().error || 'Server error')); //...errors if any
    

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
