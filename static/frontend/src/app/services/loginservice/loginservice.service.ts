import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';



@Injectable({
  providedIn: 'root'
})
export class LoginserviceService {

  constructor(private http:HttpClient) { }

  loginUser(email, password){
    let values = {email:email, password:password}
    let loginUrl:string = '/api/account/user/login/'
    return this.http.post(loginUrl, values)
  }

}
