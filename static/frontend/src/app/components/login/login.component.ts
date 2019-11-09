import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { LoginserviceService } from '../../services/loginservice/loginservice.service';


@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  form: FormGroup = new FormGroup({
    email: new FormControl('', Validators.required),
    password: new FormControl('', Validators.required)
  })

  constructor(private route: Router,
              private login: LoginserviceService) { }

  ngOnInit() {
  }

  loginUser():void{
    this.login.loginUser(this.form.value.email, this.form.value.password).subscribe( 
      data => {
        console.log(data, 'testing login databells')
        localStorage.setItem('Authorization', String(data))

    });
  }

}
