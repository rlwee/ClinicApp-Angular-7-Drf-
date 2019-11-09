import * as _ from 'lodash';
import { Injectable } from '@angular/core';
import {HttpEvent,
        HttpInterceptor,
        HttpHandler,
        HttpRequest,
        HttpHeaders} from '@angular/common/http';
import { Observable } from 'rxjs';
import { tap } from 'rxjs/operators';
import { CookieService } from 'ngx-cookie-service';


@Injectable({
    providedIn: 'root'
})
export class Interceptor implements HttpInterceptor{

    constructor(
                private cookieService: CookieService){}

    intercept (r: HttpRequest<any>, n: HttpHandler) : Observable <HttpEvent <any>> {
        const token = localStorage.getItem('Autorization')
        if ( localStorage.getItem('Authorization') == null ){
            
            const req = r.clone({
            
                headers: r.headers.set('X-CSRFToken', this.cookieService.get('csrftoken'))

            });
        

        return n.handle(req).pipe(tap(
            resp => {
                if (resp instanceof Interceptor) 
                return resp;
            }
        ));
        }


        else if ( localStorage.getItem('Authorization') != null ){
            
                const req = r.clone({

                    setHeaders: { 'X-CSRFToken': this.cookieService.get('csrftoken'),
                                  'Authorization': 'Token ' + localStorage.getItem('Authorization')
                                }

                });
            

            return n.handle(req).pipe(tap(
                resp => {
                    if (resp instanceof Interceptor) 
                    return resp;
                }
            ));
        }
       

       
    }

    
}
