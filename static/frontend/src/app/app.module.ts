import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import {NgbModule} from '@ng-bootstrap/ng-bootstrap';


import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';


import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

import { ReactiveFormsModule } from '@angular/forms';

import { Interceptor } from './interceptor'
import { CookieService } from 'ngx-cookie-service';
import { LoginComponent } from './components/login/login.component';

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    ReactiveFormsModule,
    HttpClientModule,
    NgbModule
    

  ],
  providers: [
    { provide: HTTP_INTERCEPTORS,
      useClass: Interceptor, 
      multi: true },
      CookieService,
  ],

  bootstrap: [AppComponent]
})
export class AppModule { }
