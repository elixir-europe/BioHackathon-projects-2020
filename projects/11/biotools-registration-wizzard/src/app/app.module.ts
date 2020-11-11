import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
// Material Components
import {MatStepperModule, MatStepperIntl} from '@angular/material/stepper';
import { MatSliderModule } from '@angular/material/slider';
import {MatButtonModule} from '@angular/material/button';
import {MatFormFieldModule} from '@angular/material/form-field';
import {MatInputModule} from '@angular/material/input';
import {MatCheckboxModule} from '@angular/material/checkbox';


//
import {HttpClientModule} from '@angular/common/http';

// Local components
import { ToolRegistrationComponent } from './tool-registration/tool-registration.component';
import { FormsModule, FormBuilder, ReactiveFormsModule } from '@angular/forms';
import { EdamMapComponent } from './tool-registration/edam-map/edam-map.component';
import { MatVerticalStepperScrollerDirective } from './core/mat-vertical-stepper-scroller.directive';


@NgModule({
  declarations: [
    AppComponent,
    ToolRegistrationComponent,
    EdamMapComponent,
    MatVerticalStepperScrollerDirective,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MatStepperModule,
    MatSliderModule,
    MatButtonModule,
    FormsModule,
    ReactiveFormsModule,
    MatFormFieldModule,
    MatInputModule,
    MatCheckboxModule,
    HttpClientModule
  ],
  providers: [
    MatStepperIntl,
    FormBuilder
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
